/* Built-in smoke checks; intentionally uses only Node.js core modules. */
'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const required = [
  'index.html',
  'style.css',
  'script.js',
  'manifest.webmanifest',
  'sw.js',
  'icon.svg',
  'server.js'
];

for (const file of required) {
  assert.ok(fs.existsSync(path.join(root, file)), 'Missing required file: ' + file);
}

const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
assert.match(html, /href="\.\/style\.css"/, 'index.html should load style.css');
assert.match(html, /src="\.\/script\.js"/, 'index.html should load script.js');
assert.match(html, /id="map"/, 'Map container should exist');
assert.match(html, /id="searchForm"/, 'Place search form should exist');
assert.match(html, /id="routeForm"/, 'Route planner form should exist');

const sw = fs.readFileSync(path.join(root, 'sw.js'), 'utf8');
assert.match(sw, /style\.css/, 'Service worker should cache the stylesheet');
assert.match(sw, /script\.js/, 'Service worker should cache the app script');

console.log('WayFind smoke checks passed.');
