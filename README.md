# WayFind

**Find your way.** WayFind is a responsive, mobile-friendly place discovery and route-planning web app designed to work on phones, tablets, and desktop browsers.

## Features

- Interactive, touch-friendly map powered by Leaflet and OpenStreetMap tiles.
- Search for a place or address and show it on the map.
- Optional browser geolocation; location permission is requested only after the user presses the location button.
- Route planning for driving, walking, and cycling, with estimated distance and duration.
- Quick search shortcuts for cafés, food, parks, and hospitals.
- Save and revisit places using local device storage.
- Responsive mobile layout, share link action, installable PWA manifest, and lightweight app-shell caching.
- No API key or account required for this starter version.

## Run locally

Open `index.html` through a local web server (recommended) or deploy the repository as a static site. Browser geolocation and service workers require a secure context such as HTTPS or localhost.

For example, with Python installed:

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

## Deploy with GitHub Pages

1. Open **Settings → Pages** in this repository.
2. Choose **Deploy from a branch**.
3. Select `main` and `/ (root)`, then save.
4. Wait for GitHub Pages to publish the site.

The site is static and does not require a build step.

## Important service notes

- Map tiles: OpenStreetMap. Keep visible attribution and follow the [tile usage policy](https://operations.osmfoundation.org/policies/tiles/).
- Place search: the public Nominatim endpoint is used for direct, user-submitted searches. It is rate-limited and intended for moderate use; this demo deliberately does not implement autocomplete. Read the [Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/).
- Routes: the public OSRM demo endpoint is best-effort and may be unavailable or rate-limited. It is not an SLA-backed production routing service. For a public or commercial launch, choose a supported provider or host services according to their terms.
- The app shell can be cached, but live map tiles, place search, and routing require internet access.
- The app opens external Google Maps directions only when the user presses the directions button. Route estimates are informational; follow road signs and local safety guidance.

## Privacy

WayFind does not send location automatically. Geolocation is requested only after a user action. Saved places are stored in that browser's local storage and can be cleared from the Saved places section. Searches are sent to the configured public place-search service; routing coordinates are sent to the routing service. Review provider policies before production use.

## Suggested production roadmap

- Replace public demo endpoints with production-supported map, geocoding, and routing providers.
- Add automated tests and accessibility audits.
- Add optional accounts and cross-device saved places only if needed, with clear consent and secure backend rules.
- Add curated accessible-place information and verified opening hours through a licensed data source.
