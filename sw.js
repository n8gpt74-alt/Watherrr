const CACHE_NAME = 'aquatrack-pro-v2';
const ASSETS = [
  './',
  './apps-variation-3.html',
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
          return caches.match('./apps-variation-3.html');
        }
      })
  );
});

// Push уведомления
self.addEventListener('push', (event) => {
  const data = event.data ? event.data.json() : {};
  const title = data.title || 'AquaTrack';
  const options = {
    body: data.body || 'Пора пить воду! 💧',
    icon: 'icon-192.png',
    badge: 'icon-72.png',
    vibrate: [100, 50, 100],
    data: {
      url: './apps-variation-3.html',
      timestamp: Date.now()
    },
    actions: [
      {
        action: 'add_250',
        title: '+250 мл',
        icon: 'icon-72.png'
      },
      {
        action: 'add_500',
        title: '+500 мл',
        icon: 'icon-72.png'
      },
      {
        action: 'dismiss',
        title: 'Позже',
        icon: 'icon-72.png'
      }
    ],
    tag: 'water-reminder',
    renotify: true
  };

  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});

// Клик по уведомлению
self.addEventListener('notificationclick', (event) => {
  event.notification.close();

  if (event.action === 'add_250' || event.action === 'add_500') {
    const amount = event.action === 'add_250' ? 250 : 500;
    
    // Сообщаем основному приложению
    event.waitUntil(
      clients.matchAll({ type: 'window', includeUncontrolled: true })
        .then((windowClients) => {
          // Отправляем сообщение всем клиентам
          windowClients.forEach(client => {
            client.postMessage({
              type: 'ADD_WATER',
              amount: amount
            });
          });
          
          // Если нет открытых клиентов, открываем приложение
          if (windowClients.length === 0) {
            return clients.openWindow('./apps-variation-3.html?action=add_' + amount);
          }
        })
    );
  } else {
    event.waitUntil(
      clients.openWindow('./apps-variation-3.html')
    );
  }
});

// Сообщения от основного приложения
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SCHEDULE_REMINDER') {
    const { delay, title, body } = event.data;
    
    // Планируем уведомление
    setTimeout(() => {
      self.registration.showNotification(title, {
        body: body,
        icon: 'icon-192.png',
        badge: 'icon-72.png',
        vibrate: [100, 50, 100],
        tag: 'scheduled-reminder',
        data: { url: './apps-variation-3.html' }
      });
    }, delay);
  }

  if (event.data && event.data.type === 'GET_VERSION') {
    event.ports[0].postMessage({ version: CACHE_NAME });
  }
});

// Фоновая синхронизация
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-water-data') {
    event.waitUntil(
      // Синхронизация данных при появлении соединения
      Promise.resolve()
    );
  }
});

// Periodic Background Sync (для регулярных напоминаний)
self.addEventListener('periodicsync', (event) => {
  if (event.tag === 'water-reminder-check') {
    event.waitUntil(
      // Проверка, пора ли отправлять напоминание
      Promise.resolve()
    );
  }
});
