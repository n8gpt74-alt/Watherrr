const CACHE_NAME = 'aquatrack-pro-v3';
const ASSETS = [
  './',
  './index.html',
  './manifest.json'
];

// Установка Service Worker
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Кэширование ресурсов');
        return cache.addAll(ASSETS);
      })
      .then(() => self.skipWaiting())
  );
});

// Активация Service Worker
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames
            .filter((name) => name !== CACHE_NAME)
            .map((name) => caches.delete(name))
        );
      })
      .then(() => self.clients.claim())
  );
});

// Перехват запросов
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        if (response) {
          return response;
        }
        return fetch(event.request)
          .then((response) => {
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            const responseToCache = response.clone();
            caches.open(CACHE_NAME)
              .then((cache) => {
                cache.put(event.request, responseToCache);
              });
            return response;
          });
      })
      .catch(() => {
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html');
        }
      })
  );
});

// Push уведомления
self.addEventListener('push', (event) => {
  const data = event.data ? event.data.json() : {};
  const title = data.title || 'AquaTrack — Пора пить воду!';
  
  const options = {
    body: data.body || '💧 Не забывайте поддерживать водный баланс!',
    icon: './icon-192.png',
    badge: './icon-72.png',
    vibrate: [200, 100, 200, 100, 200],
    sound: 'notification-sound.mp3',
    tag: 'water-reminder-' + Date.now(),
    renotify: true,
    requireInteraction: false,
    silent: false,
    data: {
      url: './index.html',
      timestamp: Date.now(),
      type: 'water-reminder'
    },
    actions: [
      {
        action: 'add_250',
        title: '+250 мл',
        icon: './icon-72.png'
      },
      {
        action: 'add_500',
        title: '+500 мл',
        icon: './icon-72.png'
      },
      {
        action: 'snooze',
        title: 'Напомнить позже',
        icon: './icon-72.png'
      },
      {
        action: 'dismiss',
        title: 'Закрыть',
        icon: './icon-72.png'
      }
    ]
  };

  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});

// Клик по уведомлению
self.addEventListener('notificationclick', (event) => {
  event.notification.close();

  if (event.action === 'add_250') {
    event.waitUntil(
      clients.matchAll({ type: 'window', includeUncontrolled: true })
        .then((windowClients) => {
          windowClients.forEach(client => {
            client.postMessage({
              type: 'ADD_WATER',
              amount: 250
            });
          });
          if (windowClients.length === 0) {
            return clients.openWindow('./index.html?action=add_250');
          }
        })
    );
  } else if (event.action === 'add_500') {
    event.waitUntil(
      clients.matchAll({ type: 'window', includeUncontrolled: true })
        .then((windowClients) => {
          windowClients.forEach(client => {
            client.postMessage({
              type: 'ADD_WATER',
              amount: 500
            });
          });
          if (windowClients.length === 0) {
            return clients.openWindow('./index.html?action=add_500');
          }
        })
    );
  } else if (event.action === 'snooze') {
    // Отложить на 30 минут
    event.waitUntil(
      self.registration.showNotification('⏰ Напоминание отложено', {
        body: 'Напомню через 30 минут',
        icon: './icon-192.png',
        tag: 'snooze-reminder',
        data: { url: './index.html' }
      })
    );
  } else {
    event.waitUntil(
      clients.matchAll({ type: 'window', includeUncontrolled: true })
        .then((windowClients) => {
          if (windowClients.length > 0) {
            windowClients[0].focus();
          } else {
            return clients.openWindow('./index.html');
          }
        })
    );
  }
});

// Сообщения от основного приложения
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SCHEDULE_REMINDER') {
    const { delay, title, body } = event.data;
    
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

  if (event.data && event.data.type === 'GET_VERSION') {
    event.ports[0].postMessage({ version: CACHE_NAME });
  }

  if (event.data && event.data.type === 'SEND_PUSH') {
    const { title, body, icon, sound } = event.data;
    
    self.registration.showNotification(title, {
      body: body,
      icon: icon || './icon-192.png',
      badge: './icon-72.png',
      vibrate: [200, 100, 200, 100, 200],
      sound: sound || 'notification-sound.mp3',
      tag: 'custom-notification-' + Date.now(),
      requireInteraction: false,
      data: { url: './index.html' }
    });
  }
});

// Periodic Background Sync для регулярных напоминаний
self.addEventListener('periodicsync', (event) => {
  if (event.tag === 'water-reminder-check') {
    event.waitUntil(
      // Проверка времени и отправка уведомлений
      Promise.resolve()
    );
  }
});

// Фоновая синхронизация
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-water-data') {
    event.waitUntil(
      Promise.resolve()
    );
  }
});
