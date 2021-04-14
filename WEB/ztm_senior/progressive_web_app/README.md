# PWA

## HTTPS
- Requires HTTPS to run at all — some stuff that it's doing is sensitive
- Let's encrypt gives free certificates
- Cloudflare encrypts automatically and has a free plan to host files

## Manifest
- Contains stuff for splash screens, app icons etc.

## Service Worker
- Another worker, thread, background worker
- Programmable proxy, control per request behavior
- Intercepts request and checks whether communication with network is necessary
- He goes to Cache API and fetches stuff