import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ---- A1: Calendar Month Navigation ----
# Add calendarMonth state variable after let state = ...
content = content.replace(
    'let state = JSON.parse(JSON.stringify(defaultState));',
    'let state = JSON.parse(JSON.stringify(defaultState));\n    let calendarMonth = new Date().getMonth();\n    let calendarYear = new Date().getFullYear();'
)

# Replace renderCalendar to support month nav
old_render_cal = '''function renderCalendar() {
      const today = new Date();
      const year = today.getFullYear();
      const month = today.getMonth();'''

new_render_cal = '''function renderCalendar() {
      const today = new Date();
      const year = calendarYear;
      const month = calendarMonth;
      
      // Render month navigation
      const monthNames = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];
      const calCard = calendar.parentElement;
      let navEl = calCard.querySelector('.calendar-nav');
      if (!navEl) {
        navEl = document.createElement('div');
        navEl.className = 'calendar-nav';
        calCard.insertBefore(navEl, calCard.querySelector('.calendar-header'));
      }
      navEl.innerHTML = `
        <button class="calendar-nav-btn" id="calPrev"><svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg></button>
        <span class="calendar-nav-title">${monthNames[month]} ${year}</span>
        <button class="calendar-nav-btn" id="calNext"><svg viewBox="0 0 24 24"><path d="M9 18l6-6-6-6"/></svg></button>
      `;
      document.getElementById('calPrev').onclick = () => { calendarMonth--; if (calendarMonth < 0) { calendarMonth = 11; calendarYear--; } renderCalendar(); };
      document.getElementById('calNext').onclick = () => { calendarMonth++; if (calendarMonth > 11) { calendarMonth = 0; calendarYear++; } renderCalendar(); };'''

content = content.replace(old_render_cal, new_render_cal)

# ---- A2: Delete entries from history ----
# Find renderHistoryList and modify output to include delete button
old_history_item = "class=\"badge badge-success\">+${item.amount}"
new_history_item = "class=\"badge badge-success\">+${item.amount} мл</div>\n          <button class=\"history-delete-btn\" onclick=\"deleteEntry(${item.id})\" title=\"Удалить\"><svg viewBox=\"0 0 24 24\"><path d=\"M18 6L6 18M6 6l12 12\"/></svg></button"

content = content.replace(old_history_item, new_history_item)

# Remove the trailing "мл</div>" after our replacement since the original had it
content = content.replace(
    'мл</div>\n          <button class="history-delete-btn"',
    '</div>\n          <button class="history-delete-btn"'
)

# Add deleteEntry function before getDrinkIcon
content = content.replace(
    'function getDrinkIcon(type) {',
    '''window.deleteEntry = function(id) {
      const idx = state.history.findIndex(h => h.id === id);
      if (idx !== -1) {
        const entry = state.history[idx];
        if (entry.date === getTodayKey()) {
          state.currentAmount = Math.max(0, state.currentAmount - entry.amount);
          state.entries = Math.max(0, state.entries - 1);
        }
        state.history.splice(idx, 1);
        state.streak = calculateStreak();
        saveData();
        updateUI();
        updateProgressRing();
        renderHistoryList();
        showToast('Запись удалена');
      }
    };

    function getDrinkIcon(type) {'''
)

# ---- A4: Haptic feedback ----
# Add haptic to addWater function
content = content.replace(
    "state.currentAmount += effectiveAmount;",
    "state.currentAmount += effectiveAmount;\n      if (navigator.vibrate) navigator.vibrate(50);"
)

# ---- A5: Animated counter ----
# Replace direct textContent update with animated counter
content = content.replace(
    "currentAmountEl.textContent = state.currentAmount;",
    """// Animate counter
      const target = state.currentAmount;
      const current = parseInt(currentAmountEl.textContent) || 0;
      if (current !== target) {
        const diff = target - current;
        const steps = Math.min(Math.abs(diff), 20);
        const stepSize = diff / steps;
        let step = 0;
        const counterInterval = setInterval(() => {
          step++;
          const val = Math.round(current + stepSize * step);
          currentAmountEl.textContent = step >= steps ? target : val;
          if (step >= steps) clearInterval(counterInterval);
        }, 30);
      } else {
        currentAmountEl.textContent = target;
      }"""
)

# ---- A6: Weekly widget ----
# Add weekly widget HTML after the progress ring section
content = content.replace(
    '<!-- Drink Types -->',
    '''<!-- Weekly Stats -->
        <div class="card">
          <div class="card-title">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>
            Неделя
          </div>
          <div class="weekly-widget" id="weeklyWidget"></div>
        </div>

        <!-- Drink Types -->'''
)

# Add renderWeeklyWidget function before renderCalendar
content = content.replace(
    'function renderCalendar() {',
    '''function renderWeeklyWidget() {
      const widget = document.getElementById('weeklyWidget');
      if (!widget) return;
      const today = new Date();
      const todayKey = getTodayKey();
      const dayNames = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'];
      let html = '';
      
      for (let i = 6; i >= 0; i--) {
        const d = new Date(today);
        d.setDate(d.getDate() - i);
        const dateKey = d.toISOString().split('T')[0];
        const dayEntries = state.history.filter(h => h.date === dateKey);
        const total = dayEntries.reduce((sum, h) => sum + h.amount, 0);
        const pct = Math.min((total / state.goalAmount) * 100, 100);
        const isToday = dateKey === todayKey;
        const goalReached = total >= state.goalAmount;
        
        html += `<div class="weekly-bar">
          <div class="weekly-bar-fill ${isToday ? 'today-bar' : ''} ${goalReached ? 'goal-reached' : ''}" style="height: ${Math.max(pct, 3)}%"></div>
          <span class="weekly-bar-label">${dayNames[d.getDay()]}</span>
        </div>`;
      }
      widget.innerHTML = html;
    }

    function renderCalendar() {'''
)

# Call renderWeeklyWidget in updateUI
content = content.replace(
    "// Notification banner",
    "// Weekly widget\n      renderWeeklyWidget();\n\n      // Notification banner"
)

# ---- C3: Version bump ----
content = content.replace('2.0.0 Pro', '3.0.0 Pro')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! All UX features applied.")
