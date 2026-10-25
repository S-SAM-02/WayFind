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

- `index.html` — existing map interface.
- `style.css` — existing responsive layout and styles.
- `script.js` — existing map, place search, geolocation, routing, and interactions.
- `server.js` — small Node.js server for local development.
- `package.json` — project metadata and commands.
- `manifest.webmanifest` and `sw.js` — PWA metadata and app-shell caching.
- `tests/smoke-test.js` — basic project checks.
- `.github/workflows/ci.yml` — automatic checks on pushes and pull requests.

## New Python panorama prototype

The repository now also includes an early Flask-based WayFind AI prototype:

- `app.py` — image upload endpoint and basic image validation.
- `templates/index.html` — panorama upload interface and viewer.
- `static/style.css` — responsive styles for the Python interface.
- `requirements.txt` — Python dependencies.
- `uploads/` — local upload storage, excluded from Git.

The prototype accepts JPG/PNG files (maximum 20 MB) and displays suitable equirectangular panoramas using Pannellum. Its aspect-ratio check is only a heuristic; it cannot confirm that an image is a valid 360° panorama.

**Not implemented yet:** object/sign detection, OCR, automatic visual localization, AI-generated route instructions, and live camera navigation. These are planned development stages, not active features.

## Run the existing map application (Node.js)

1. Install Node.js 18 or newer from https://nodejs.org/.
2. Clone this repository.
3. Open a terminal in the project folder.
4. Run:

    ```bash
    npm start
    ```

5. Visit http://localhost:3000.

There are no npm packages to install. Run the built-in checks with:

    ```bash
    npm run check
    ```

The static frontend can also be published with GitHub Pages using the existing repository setup. GitHub Pages does not run the Python Flask backend.

## Run the Python panorama prototype

Python 3.11+ is recommended.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser. The Python app is separate from the existing Node.js map app; run one server at a time or use different ports.

The current Flask server is for local development only. Do not expose Flask's debug server publicly. For deployment, use a production WSGI server, appropriate upload access controls, and secure storage.

## External services and limitations

- **Map tiles:** OpenStreetMap. Keep attribution visible and follow the [tile usage policy](https://operations.osmfoundation.org/policies/tiles/).
- **Place search:** the public Nominatim endpoint is rate-limited and intended for moderate use. Read the [Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/).
- **Routing:** the public OSRM demo endpoint is best-effort and may be unavailable or rate-limited. It is not a production service with an uptime guarantee.
- **Panorama viewer:** Pannellum is loaded from jsDelivr in the prototype, so that viewer needs internet access.
- **No production guarantee:** before a public launch, choose map, geocoding, and routing providers whose terms, privacy requirements, costs, and capacity fit expected traffic.

## Privacy and safety

- The existing map app requests geolocation only after the user presses the location button.
- Searches and route coordinates may be sent to the configured public search/routing services.
- Uploaded panorama images are stored locally in `uploads/`; remove them when no longer needed.
- Do not upload images containing private or sensitive information.
- Do not rely on an unverified visual match for safety-critical navigation. Ask the user to confirm uncertain locations and directions.

## Working with a collaborator

1. Add your teammate under **Settings → Collaborators** in GitHub.
2. Both collaborators should pull the latest `main` branch before editing.
3. Use separate branches for larger features and open pull requests for review.
4. Avoid committing passwords, API keys, tokens, or private user data.

## Roadmap

1. Improve panorama validation and add tests.
2. Add sign/object detection and OCR with user correction.
3. Build a reference-image dataset for known campus locations.
4. Match uploaded scenes to known places with confidence thresholds.
5. Integrate pedestrian routing and generate turn-by-turn instructions.
6. Add mobile GPS, compass, camera capture, and live route updates.
7. Evaluate localization, OCR, route accuracy, and failure cases.
8. Add browser-based end-to-end and accessibility tests.
