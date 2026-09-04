const CACHE = 'little-light-en-v3';
const ASSETS = [
  './', './index.html', './manifest.webmanifest', './sw.js',
  './icons/icon-192.png', './icons/icon-512.png',
  './pages/page-01.jpg', './pages/page-02.jpg', './pages/page-03.jpg', './pages/page-04.jpg', './pages/page-05.jpg',
  './pages/page-06.jpg', './pages/page-07.jpg', './pages/page-08.jpg', './pages/page-09.jpg', './pages/page-10.jpg',
  './pages/page-11.jpg', './pages/page-12.jpg', './pages/page-13.jpg', './pages/page-14.jpg', './pages/page-15.jpg',
  './pages/page-16.jpg', './pages/page-17.jpg', './pages/page-18.jpg', './pages/page-19.jpg', './pages/page-20.jpg',
  './pages/page-21.jpg', './pages/page-22.jpg', './pages/page-23.jpg', './pages/page-24.jpg', './pages/page-25.jpg',
  './audio/page-01.mp3', './audio/page-02.mp3', './audio/page-04.mp3', './audio/page-05.mp3', './audio/page-06.mp3',
  './audio/page-08.mp3', './audio/page-10.mp3', './audio/page-12.mp3', './audio/page-14.mp3', './audio/page-16.mp3',
  './audio/page-18.mp3', './audio/page-20.mp3', './audio/page-22.mp3', './audio/page-24.mp3', './audio/page-25.mp3',
  './audio/page-turn.wav'
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(key => key !== CACHE).map(key => caches.delete(key))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          const copy = response.clone();
          caches.open(CACHE).then(cache => cache.put('./index.html', copy));
          return response;
        })
        .catch(() => caches.match('./index.html'))
    );
    return;
  }
  event.respondWith(
    caches.match(event.request).then(cached => cached || fetch(event.request).then(response => {
      const copy = response.clone();
      caches.open(CACHE).then(cache => cache.put(event.request, copy));
      return response;
    }))
  );
});
