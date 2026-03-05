import re

# 1. Update sw.js Message Listener
with open('sw.js', 'r', encoding='utf-8') as f:
    sw_content = f.read()

new_schedule_logic = """
  if (event.data && event.data.type === 'SCHEDULE_REMINDER') {
    const { delay, title, body } = event.data;
    
    // Experimental Notification Triggers API if supported
    if ('showTrigger' in Notification.prototype) {
      try {
        self.registration.showNotification(title, {
          body: body,
          icon: './icon-192.png',
          badge: './icon-72.png',
          vibrate: [200, 100, 200],
          sound: 'notification-sound.mp3',
          tag: 'water-reminder-' + Date.now(),
          showTrigger: new TimestampTrigger(Date.now() + delay),
          data: { url: './index.html' }
        });
        return;
      } catch(e) {
        console.warn('showTrigger failed, fallback to setTimeout', e);
      }
    }
    
    // Fallback
    setTimeout(() => {
      self.registration.showNotification(title, {
        body: body,
        icon: './icon-192.png',
        badge: './icon-72.png',
        vibrate: [200, 100, 200],
        sound: 'notification-sound.mp3',
        tag: 'scheduled-reminder',
        data: { url: './index.html' }
      });
    }, delay);
  }
"""

sw_content = re.sub(
    r'  if \(event\.data && event\.data\.type === \'SCHEDULE_REMINDER\'\) \{.*?\} \}, delay\);\n  \}',
    new_schedule_logic.strip(),
    sw_content,
    flags=re.DOTALL
)

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw_content)

# 2. Update index.html scheduleReminders
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

new_schedule_index = """
    function scheduleReminders() {
      if (Notification.permission !== 'granted') return;
      if (!state.settings.remindersEnabled) return;

      // Clear existing intervals (fallback)
      reminderIntervals.forEach(id => clearInterval(id));
      reminderIntervals = [];

      const times = state.settings.reminderTimes;
      const now = new Date();

      ['morning', 'day', 'evening'].forEach(period => {
         const timeStr = times[period];
         if(!timeStr) return;
         const [h, m] = timeStr.split(':').map(Number);
         let target = new Date(now.getFullYear(), now.getMonth(), now.getDate(), h, m, 0);
         
         if (target <= now) {
            // schedule for next day
            target.setDate(target.getDate() + 1);
         }
         const delay = target.getTime() - now.getTime();
         
         let text = period === 'morning' ? 'Пора пить воду! Начните день со стакана воды 💧' : 
                   (period === 'day' ? 'Не забывайте пить воду в течение дня 💧' : 'Последний приём воды перед сном 💧');
         let title = period === 'morning' ? '☀️ Доброе утро!' : (period === 'day' ? '🌞 День!' : '🌆 Вечер!');
         
         if (serviceWorkerRegistration && serviceWorkerRegistration.active) {
            serviceWorkerRegistration.active.postMessage({
              type: 'SCHEDULE_REMINDER',
              delay: delay,
              title: title,
              body: text
            });
         }
      });

      // Keep the interval fallback for open tabs
      const checkInterval = setInterval(() => {
        checkAndNotify(times);
      }, 60000);
      reminderIntervals.push(checkInterval);
    }
"""

html_content = re.sub(
    r'    function scheduleReminders\(\) \{.*?    \}',
    new_schedule_index.strip(),
    html_content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

