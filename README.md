# Bill Compass — website

The public site for **Bill Compass**, a bill tracker for iPhone, iPad and Mac.
Served by GitHub Pages at <https://billcompass.github.io>.

| Page | Purpose |
| --- | --- |
| `index.html` | Product page |
| `privacy.html` | Privacy policy — **required** by App Store Connect |
| `support.html` | Support — **required** by App Store Connect, and it must be a page rather than a `mailto:` link |

The app's own source lives in a separate, private repository. Nothing here
is generated from it at build time, so the site can be edited on its own.

## Editing

The pages are plain HTML and can be edited directly. They are also generated
by `build.py`, which holds the copy and the shared layout in one place —
change the text there and run `python3 build.py .` to rewrite all three.

`assets/icon.png` is a 256px copy of the app icon; replace it when the app
icon changes.

`.nojekyll` tells Pages to serve the files as they are rather than running
them through Jekyll.
