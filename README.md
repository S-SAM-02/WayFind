# WayFind Navigation

WayFind is a navigation-first web app prototype designed to help people orient themselves in unfamiliar cities. The interface is inspired by mobile turn-by-turn navigation: a full navigation canvas, a prominent next-turn card, a clear trip planner, and optional road-sign photo assistance.

## Main features

- Navigation-first black-and-gold UI with no embedded Google Maps or Google Maps redirect.
- Destination and starting point search using OpenStreetMap Nominatim.
- Driving routes, distances, travel-time estimates and maneuver-by-maneuver steps using the public OSRM demo service.
- Optional live GPS position tracking with explicit user permission.
- Road sign/landmark image upload and in-browser OCR using Tesseract.js; detected text can be edited before searching.
- Locally saved places and installable PWA shell.
- Responsive desktop and mobile layouts.
- Node.js static preview server with no npm runtime dependencies.

## Project structure

- `index.html` — main navigation interface.
- `style.css` — responsive navigation-first styling.
- `script.js` — route search, turn instructions, GPS watch, OCR and saved places.
- `server.js` — optional Node.js preview server.
- `package.json` — project commands.
- `manifest.webmanifest`, `sw.js`, `icon.svg` — PWA files.
- `tests/smoke-test.js` — structural checks.
- `.github/workflows/ci.yml` — CI workflow.
- `app.py`, `templates/`, `static/`, `requirements.txt` — separate experimental Flask panorama prototype; it is not used by the main navigation page.

## Run locally

Requires Node.js 18 or newer.

```bash
git clone https://github.com/S-SAM-02/WayFind.git
cd WayFind
npm start
```

Open http://localhost:3000. To run local checks:

```bash
npm run check
```

No `npm install` is required for the main static application.

## Deploy

For the current static frontend, use GitHub Pages:
1. Open **Settings → Pages**.
2. Choose **Deploy from a branch**.
3. Select `main` and `/(root)`.
4. Save and wait for GitHub Pages to publish.

GitHub Pages serves the static frontend; it does not run `server.js` or the Flask prototype. Geolocation and service workers require HTTPS or localhost.

## External data and accuracy

- **Search/geocoding:** public Nominatim. It is rate-limited and intended for moderate usage. Avoid autocomplete and follow its usage policy: https://operations.osmfoundation.org/policies/nominatim/
- **Routing:** public OSRM demo service, best-effort and not production SLA-backed. The current main app supports driving routing only.
- **Road data:** routes are computed from available community road-network data. Missing, outdated or restricted roads may produce incomplete routes.
- **No Google Maps UI:** the main site does not embed Google Maps or link users to Google Maps for route completion. OpenStreetMap-derived data is still required for road geometry and routing.
- **Photo assist:** OCR extracts visible text from a road-sign or landmark image. It does not identify exact image coordinates, guarantee the photographed location, detect all objects, or produce a route from pixels alone. The person using the app should review OCR results and confirm the destination.
- **Live guidance:** browser GPS tracking updates the next-step panel based on proximity to maneuver points. This is an early prototype, not a turn-by-turn navigation system proven safe for driving. The current implementation does not provide voice guidance or reliable off-route rerouting yet.

## Privacy and safety

- GPS is requested only after the user activates a location action or live guidance.
- Search queries and route coordinates are sent to the public services listed above.
- The OCR library is downloaded on demand. The image itself is processed in the browser by the OCR library and is not uploaded to a WayFind backend.
- Do not use the prototype while interacting with a phone in motion. Follow traffic laws, road signs and your surroundings.

## Collaboration

Add collaborators through GitHub repository Settings → Collaborators. Pull the latest main branch before editing and use a branch/PR for substantial features. Never commit API keys, secrets, or user location history.

## Next engineering milestones

1. Add route-matching against road geometry rather than only choosing the nearest upcoming maneuver.
2. Add off-route detection and safe rerouting with hysteresis.
3. Add speech announcements after extensive UX and accessibility testing.
4. Integrate licensed/supportable pedestrian and cycling providers.
5. Add image landmark localization only with reference datasets, uncertainty thresholds, and user confirmation.
6. Add browser/device integration tests and route accuracy tests before a public navigation launch.
