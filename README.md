# Bill Compass — website

The public site for **Bill Compass**, a bill tracker for iPhone, iPad and Mac.
Served by GitHub Pages at <https://billcompass-app.github.io>.

| Page | Purpose |
| --- | --- |
| `index.html` | Product page |
| `features.html` | A tour of every screen |
| `guide.html` | How to Use — step-by-step instructions |
| `sync.html` | Lifetime iCloud Sync: buying, restoring, troubleshooting |
| `faq.html` | Frequently asked questions |
| `privacy.html` | Privacy policy — **required** by App Store Connect |
| `support.html` | Support — **required** by App Store Connect, and it must be a page rather than a `mailto:` link |

The app's own source lives in a separate, private repository. Nothing here
is generated from it at build time, so the site can be edited on its own.

## Editing

The pages are plain HTML and can be edited directly. They are also generated
by `build.py`, which holds the copy and the shared layout in one place —
change the text there and run `python3 build.py .` to rewrite every page.

`assets/icon.png` is a 256px copy of the app icon; replace it when the app
icon changes.

`assets/screens/` holds the screenshots. They are taken from a Debug build
launched with `-BCScreenshotMode -launchSection <screen>` (and
`-billLayout grid|stickie` on iPad), which seeds a made-up household into a
store of its own, then scaled to 600px (iPhone) or 1100px (iPad) JPEGs.

`.nojekyll` tells Pages to serve the files as they are rather than running
them through Jekyll.
