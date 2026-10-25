# WayFind

**Find your way.** WayFind is a responsive place-discovery and route-planning web app built with HTML, CSS, JavaScript, Leaflet, and OpenStreetMap.

## Features

- Interactive, touch-friendly map with OpenStreetMap attribution.
- Search for a place or address and show it on the map.
- Optional browser geolocation, requested only after the user presses the location button.
- Route planning for driving, walking, and cycling with distance and duration estimates.
- Quick-search shortcuts for cafés, food, parks, and hospitals.
- Save and revisit places using local browser storage.
- Responsive layout for desktop, tablet, and mobile.
- Share link and installable Progressive Web App (PWA) support.
- Service-worker caching for the local app shell.
- Optional Node.js preview server with no third-party dependencies.
- No API key required for the starter version.

## Project structure

- `index.html` — semantic page structure and interface.
- `style.css` — responsive layout, theme, and component styles.
- `script.js` — map, place search, geolocation, routing, saved places, and interactions.
- `server.js` — small Node.js server for local development.
- `package.json` — project metadata and commands.
- `manifest.webmanifest` — installable PWA metadata.
- `sw.js` — service worker for app-shell caching.
- `icon.svg` — application icon.
- `tests/smoke-test.js` — basic project structure and syntax checks.
- `.github/workflows/ci.yml` — automatic checks on pushes and pull requests.

## Requirements

- Node.js 18 or newer (only needed for the optional local server and checks).
- A modern browser.
- Internet access for map tiles, geocoding, and route requests.

## Run locally with Node.js

1. Install Node.js 18 or newer from https://nodejs.org/.
2. Clone this repository.
3. Open a terminal in the project folder.
4. Run:

    npm start

5. Visit http://localhost:3000.

There are no npm packages to install. You can also run the built-in checks:

    npm run check

Browser geolocation and service workers work on secure contexts such as localhost and HTTPS. Opening the HTML file directly with a file URL is not recommended.

## Deploy with GitHub Pages

1. Open this repository's **Settings → Pages**.
2. Select **Deploy from a branch**.
3. Choose the `main` branch and `/(root)`, then save.
4. Wait for GitHub to publish the site.

The frontend is static, so GitHub Pages does not run `server.js` and does not need Node.js to build the site. The same HTML, CSS, JavaScript, manifest, icon, and service worker can be served as static files.

## External services and limitations

- **Map tiles:** OpenStreetMap. Keep attribution visible and follow the [tile usage policy](https://operations.osmfoundation.org/policies/tiles/).
- **Place search:** the public Nominatim endpoint is used for user-submitted searches. It is rate-limited and intended for moderate use. This demo deliberately avoids autocomplete. Read the [Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/).
- **Routing:** the public OSRM demo endpoint is best-effort and may be unavailable or rate-limited. It is not a production service with an uptime guarantee.
- **Internet required:** live map tiles, place search, and routing need internet access even when the app shell is cached.
- **No production guarantee:** before a public or commercial launch, select providers whose usage terms, capacity, privacy terms, and costs fit your expected traffic. Do not assume public demo endpoints can support heavy usage.

## Privacy

WayFind does not request location automatically. Geolocation is requested only after a user action. Saved places are stored in that browser's local storage and can be cleared from the Saved places section. Searches are sent to the configured public place-search service, and route coordinates are sent to the routing service. Review provider policies before a production launch.

## Working with a collaborator

1. Add your teammate under **Settings → Collaborators** in GitHub.
2. Both collaborators should pull the latest `main` branch before editing.
3. Use separate branches for larger features and open pull requests for review.
4. Avoid committing passwords, API keys, tokens, or private user data.

## Roadmap

- Choose supported production map, geocoding, and routing providers.
- Add browser-based end-to-end tests and accessibility checks.
- Add optional accounts and cross-device saved places only if required, with consent and secure backend rules.
- Add curated accessibility information and verified opening hours through a licensed data source.
