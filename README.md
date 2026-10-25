# WayFind Navigation

WayFind is a navigation-first web app prototype designed to help people orient themselves in unfamiliar cities. It combines a real interactive street map, a prominent next-turn card, a trip planner, live GPS location tracking, and optional photo-assisted road-sign text recognition.

## Main features

- **Real interactive street map:** MapLibre GL JS with a CARTO Dark Matter basemap based on OpenStreetMap data. No Google Maps embed, SDK, tile layer, or redirect is used.
- **Real route geometry:** driving routes from the public OSRM demo service, displayed as a highlighted road-following line on top of the map.
- **Map controls:** drag to pan, zoom buttons, start/destination markers, route-fit overview, and a 2D/tilted-perspective toggle.
- **Turn-by-turn panel:** maneuvers, road names when available, estimates, and current step highlighting.
- **GPS follow mode:** requests device location only after the user starts a location action or live guidance. During guidance the map follows the GPS point and can rotate based on GPS heading.
- **Photo assist:** in-browser OCR of a road-sign or landmark photo, with editable detected text before searching.
- **Locally saved places**, share link, responsive mobile layout and PWA shell.
- **No npm runtime dependencies** for the optional local static preview server.

## Project structure

- `index.html` — navigation interface.
- `style.css` — responsive black-and-gold theme, street-map layout and controls.
- `script.js` — geocoding, routing, map overlays, directions, GPS tracking, OCR and saved places.
- `server.js`, `package.json` — optional Node.js preview server and scripts.
- `manifest.webmanifest`, `sw.js`, `icon.svg` — PWA files.
- `tests/smoke-test.js` — source-structure checks.
- `.github/workflows/ci.yml` — CI workflow.
- `app.py`, `templates/`, `static/`, `requirements.txt` — separate experimental Flask panorama prototype; it is not the main navigation page.

## Run locally

Requires Node.js 18 or newer.

```bash
git clone https://github.com/S-SAM-02/WayFind.git
cd WayFind
npm start
```

Open http://localhost:3000. Run checks using:

```bash
npm run check
```

## Deploy the static application

1. Open repository **Settings → Pages**.
2. Choose **Deploy from a branch**.
3. Select `main` and `/(root)`.
4. Save and wait for the deployment to finish.

Geolocation and service workers require HTTPS or localhost. If an old interface remains after deployment, hard refresh the browser and, if needed, clear the site's cached data.

## Map data and service limits

- **Basemap:** CARTO Dark Matter GL style: `https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json`. It uses third-party map tiles/vector data and requires internet access. Keep the map's attribution visible and follow provider terms.
- **Geocoding:** the public Nominatim endpoint. It is rate-limited and intended for moderate use. Follow https://operations.osmfoundation.org/policies/nominatim/.
- **Routing:** the public OSRM demo service. It is best-effort, is not a production uptime guarantee, and currently supplies the app's driving profile. For production, use a provider with appropriate capacity and terms.
- **No Google Maps UI:** the main page does not embed or redirect to Google Maps. It does still use road-network data from external non-Google services.
- **Tilted mode:** the 3D-style camera is a pitched/rotated map view. It is not a photorealistic globe, full 3D terrain or building model.
- **Photo assist:** OCR reads visible text; it does not independently establish an exact location from a photo or generate road geometry from pixels.
- **Live GPS:** map-following and proximity-based turn estimates are a prototype. Production navigation needs stronger route-matching, off-route detection, rerouting, voice prompts, accessibility testing and real-device field testing.

## Privacy and safety

- GPS is requested only after user action.
- Searches and route coordinates are sent to configured public place-search and routing services.
- OCR libraries are loaded on demand and sign text is processed in the browser; no WayFind image upload backend is used by the main page.
- Do not use a phone while driving. Follow local traffic laws, signs and your surroundings. Do not rely on this prototype as the sole source for safety-critical navigation.

## Collaboration

Add collaborators in **Settings → Collaborators**. Pull the latest main branch before editing. Use separate branches for larger changes and never commit passwords, credentials or private location history.

## Next engineering milestones

1. Improve route matching and add off-route detection/rerouting.
2. Add spoken turn announcements after accessibility and safety tests.
3. Add walking/cycling profiles with a suitable provider.
4. Add landmark recognition only with verified reference datasets and uncertainty thresholds.
5. Add browser/device integration tests and route accuracy tests before public navigation launch.
