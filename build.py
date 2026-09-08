"""Rebuilds the Bill Compass site from the copy held in this file.

Three pages, two of which Apple requires before an app can be submitted —
a privacy policy and a support page — and a product page in front of them.
Everything the privacy page claims was checked against the source rather
than assumed: no third-party packages, no URLSession anywhere, and the
diagnostics report's own wording about what it does and does not include.
"""
import os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = ROOT
SUPPORT_EMAIL = "billcompass@hotmail.com"   # swap once the account exists
UPDATED = "6 September 2026"

CSS = """/* Bill Compass — site styles.
   The palette is the app's own: SurfaceBackground, SurfaceCard, the coral
   accent and SignalGreen, so the site and the app agree about colour. */
:root {
  --ground:#F8F5F0; --card:#FFFDFA; --ink:#241C2E; --muted:#7B6E86;
  --hair:#E4DAD0; --accent:#FF6F61; --gold:#C98A12; --green:#0B8F27;
  --display:"Bricolage Grotesque","Trebuchet MS",sans-serif;
  --body:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,"SF Mono",monospace;
}
@media (prefers-color-scheme:dark){
  :root{ --ground:#141520; --card:#1E2030; --ink:#F2ECE4; --muted:#9E94AE;
         --hair:#2E3044; --accent:#FF8A75; --gold:#FFC24B; --green:#28E14F; }
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--body);
     font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
.wrap{max-width:760px;margin:0 auto;padding:0 24px}
a{color:var(--accent)}
a:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:4px}

.topbar{border-bottom:1px solid var(--hair)}
.topbar .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;
              padding-top:18px;padding-bottom:18px}
.brand{display:flex;align-items:center;gap:11px;font-family:var(--display);
       font-weight:700;font-size:18px;color:var(--ink);text-decoration:none;letter-spacing:-.01em}
.brand img{width:30px;height:30px;border-radius:22.37%;display:block}
.topbar nav{display:flex;gap:20px;font-size:15px}
.topbar nav a{color:var(--muted);text-decoration:none}
.topbar nav a:hover,.topbar nav a[aria-current]{color:var(--ink)}

.hero{text-align:center;padding:64px 0 8px}
.hero img.icon{width:128px;height:128px;border-radius:22.37%;
  box-shadow:0 2px 6px rgba(40,20,50,.18),0 24px 48px -24px rgba(40,20,50,.45)}
h1{font-family:var(--display);font-weight:700;letter-spacing:-.025em;line-height:1.04;
   font-size:clamp(34px,6.5vw,54px);margin:26px 0 0;text-wrap:balance}
.tagline{margin:16px auto 0;max-width:34ch;color:var(--muted);font-size:19px}
.platforms{margin:24px 0 0;font-family:var(--mono);font-size:12.5px;letter-spacing:.1em;
           text-transform:uppercase;color:var(--muted)}
.storenote{display:inline-block;margin-top:28px;padding:9px 18px;border:1px solid var(--hair);
  border-radius:999px;font-size:14px;color:var(--muted);background:var(--card)}

section{padding:56px 0}
h2{font-family:var(--display);font-weight:700;letter-spacing:-.02em;line-height:1.12;
   font-size:clamp(25px,4vw,33px);margin:0 0 18px;text-wrap:balance}
h3{font-family:var(--display);font-weight:700;font-size:18px;margin:34px 0 8px;letter-spacing:-.01em}
p{margin:0 0 16px}
.lead{font-size:18.5px;color:var(--muted)}

.features{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));gap:26px;
          list-style:none;padding:0;margin:0}
.features li{background:var(--card);border:1px solid var(--hair);border-radius:14px;padding:20px 22px}
.features b{display:block;font-family:var(--display);font-size:16.5px;margin-bottom:5px}
.features span{color:var(--muted);font-size:15px}

.pledge{background:var(--card);border:1px solid var(--hair);border-left:3px solid var(--green);
        border-radius:12px;padding:22px 24px;margin:0 0 30px}
.pledge p:last-child{margin-bottom:0}
.stamp{font-family:var(--mono);font-size:11px;letter-spacing:.13em;text-transform:uppercase;
       color:var(--green);display:block;margin-bottom:7px}

.meta{font-family:var(--mono);font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;
      color:var(--muted);margin:0 0 10px}
dl{margin:0}
dt{font-family:var(--display);font-weight:700;font-size:17px;margin:26px 0 6px}
dd{margin:0 0 16px;color:var(--muted)}
ul.plain{padding-left:20px;color:var(--muted)}
ul.plain li{margin-bottom:8px}
code{font-family:var(--mono);font-size:.88em;background:var(--ground);border:1px solid var(--hair);
     padding:1px 5px;border-radius:4px}

footer{border-top:1px solid var(--hair);margin-top:34px}
footer .wrap{display:flex;flex-wrap:wrap;gap:14px 26px;justify-content:space-between;
             padding-top:28px;padding-bottom:44px;font-size:14.5px;color:var(--muted)}
footer a{color:var(--muted)}
@media (max-width:520px){
  .hero{padding-top:44px}
  .topbar nav{gap:14px;font-size:14px}
}
"""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700&family=IBM+Plex+Mono:wght@400&family=IBM+Plex+Sans:wght@400;500&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
"""

def topbar(current):
    def link(href, label):
        cur = ' aria-current="page"' if label == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f'''<header class="topbar"><div class="wrap">
  <a class="brand" href="index.html"><img src="assets/icon.png" alt=""> Bill Compass</a>
  <nav>{link("privacy.html","Privacy")}{link("support.html","Support")}</nav>
</div></header>'''

FOOTER = f'''<footer><div class="wrap">
  <span>Bill Compass — for iPhone, iPad and Mac</span>
  <span><a href="privacy.html">Privacy</a> · <a href="support.html">Support</a></span>
</div></footer>'''


INDEX = f'''
<div class="hero"><div class="wrap">
  <img class="icon" src="assets/icon.png" alt="The Bill Compass app icon">
  <h1>Never miss a bill again</h1>
  <p class="tagline">Every bill you owe, in one calm list — and a month you can see coming.</p>
  <p class="platforms">iPhone · iPad · Mac</p>
  <p class="storenote">Coming to the App Store</p>
</div></div>

<section><div class="wrap">
  <h2>What it does</h2>
  <ul class="features">
    <li><b>Overview</b><span>Everything still owed, soonest first, with how many days you have left. As a list, a grid, or a wall of paper notes.</span></li>
    <li><b>Calendar</b><span>The month laid out by date, so a heavy week is visible before it arrives.</span></li>
    <li><b>Reports</b><span>What the next 30, 60 and 90 days cost, and what each category takes over a year.</span></li>
    <li><b>History</b><span>Every payment you have recorded, grouped by month, including part payments and skipped cycles.</span></li>
    <li><b>Tags</b><span>Group bills your own way — Essentials, Household, Family — and see what each group costs.</span></li>
    <li><b>Reminders</b><span>A notification before a bill is due, with the lead time set per bill rather than one rule for all.</span></li>
  </ul>
</div></section>

<section><div class="wrap">
  <h2>It syncs, and it stays yours</h2>
  <div class="pledge">
    <span class="stamp">Privacy</span>
    <p>Bill Compass has no account, no server of ours, and no analytics. Your bills live on your device and sync through <b>your own iCloud</b>, which we cannot read. Nothing is collected, and nothing is sold.</p>
  </div>
  <p class="lead">Add a bill on your phone and it is on your Mac. Appearance stays per device on purpose — a Mac on a desk and a phone in bed are entitled to different answers.</p>
  <p><a href="privacy.html">Read the full privacy policy</a></p>
</div></section>
'''


PRIVACY = f'''
<section><div class="wrap">
  <p class="meta">Last updated {UPDATED}</p>
  <h1 style="font-size:clamp(30px,5.5vw,44px);margin-top:0">Privacy Policy</h1>

  <div class="pledge">
    <span class="stamp">The short version</span>
    <p>Bill Compass collects nothing. There is no account, no analytics, no advertising and no third-party code in the app. Your bills stay on your devices and in your own iCloud account, which the developer cannot access.</p>
  </div>

  <h3>What is collected</h3>
  <p>Nothing. Bill Compass does not gather usage data, device identifiers, crash reports, contacts, location or any other personal information, and it contains no analytics or advertising software.</p>

  <h3>Where your information lives</h3>
  <p>Bills, payments and tags are stored on your device. If you are signed in to iCloud, they also sync through Apple's CloudKit to your <em>private</em> iCloud database, so the same bills appear on your other devices. That database belongs to your Apple Account. The developer has no access to it and no way to read what is in it.</p>
  <p>Settings — the theme, light or dark, the background, how bills are arranged, your reminder preferences — are stored on the device they were chosen on and are not synced.</p>

  <h3>Reminders</h3>
  <p>If you turn reminders on, they are scheduled and delivered on your device by iOS or macOS. Nothing is sent anywhere to make a reminder appear, and no notification content leaves your device.</p>

  <h3>Photos</h3>
  <p>If you choose a photo as the app's background, it is copied into the app's own storage on that device and used only to draw the background. It is not synced and never leaves the device.</p>

  <h3>Backups you make yourself</h3>
  <p>Bill Compass can export your bills, payments and tags to a CSV file. That file goes wherever you send it and is then in your hands. The app does not upload it anywhere.</p>

  <h3>Diagnostics</h3>
  <p>The Diagnostics screen can copy a short report for pasting into a support email. It describes the app and the device — version, whether sync is on, how many records exist — and, in the app's own words, no bill names, amounts or notes are included. Nothing is sent automatically; you choose whether to share it.</p>

  <h3>Third parties</h3>
  <p>There are none. The app has no third-party libraries, no software development kits and no network requests of its own. The only network service it uses is Apple's iCloud, on your behalf, and that is covered by <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>.</p>

  <h3>Children</h3>
  <p>Bill Compass is a household finance tool, is not directed at children, and knowingly collects no information from anyone.</p>

  <h3>Deleting your information</h3>
  <ul class="plain">
    <li>Delete a bill in the app and it is gone from that device and from your iCloud.</li>
    <li>Delete the app to remove everything it stored on that device.</li>
    <li>To remove the synced copy, turn off iCloud for Bill Compass, or delete the app's iCloud data in your device's iCloud settings.</li>
    <li>Because nothing is collected, there is no account to close and nothing for the developer to delete on your behalf.</li>
  </ul>

  <h3>Changes to this policy</h3>
  <p>If this policy changes, the new version will be posted on this page with a new date at the top.</p>

  <h3>Contact</h3>
  <p>Questions about privacy: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a></p>
</div></section>
'''


SUPPORT = f'''
<section><div class="wrap">
  <h1 style="font-size:clamp(30px,5.5vw,44px);margin-top:0">Support</h1>
  <p class="lead">Questions, problems and suggestions are all welcome — there is one person reading, so please say which device and which version you are on.</p>

  <div class="pledge" style="border-left-color:var(--accent)">
    <span class="stamp" style="color:var(--accent)">Get in touch</span>
    <p style="margin-bottom:0"><a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a><br>
    <span style="color:var(--muted);font-size:15px">Settings → Diagnostics → Copy Report gives you a short summary of your app and device that helps a great deal. It contains no bill names, amounts or notes.</span></p>
  </div>

  <h2>Common questions</h2>
  <dl>
    <dt>Tapping a bill does nothing. Is it broken?</dt>
    <dd>No — that is deliberate, so scrolling can never settle a bill by accident. Touch and hold a bill to record a payment, edit it or skip a cycle. On a Mac, right-click or double-click.</dd>

    <dt>My bills have not appeared on my other device</dt>
    <dd>Both devices need to be signed in to the same Apple Account with iCloud Drive on. Syncing is handled by iCloud and is not instant — it can take a few minutes, and a device that has been asleep may need the app opened once. On iPhone and iPad you can pull down on the bill list to prompt a refresh. Settings → Diagnostics shows whether sync is on and when data was last sent and received.</dd>

    <dt>How do I record a payment?</dt>
    <dd>Touch and hold the bill and choose Record Payment. A full payment moves the bill on to its next cycle; a partial payment leaves it due and shows what is still owed. You can also record a payment from a day in the Calendar.</dd>

    <dt>A bill was not due this month</dt>
    <dd>Touch and hold it and choose Skip Cycle. That moves the bill forward without recording money, and the skip is listed in History so the gap is explained.</dd>

    <dt>How do I back up my bills?</dt>
    <dd>Settings → Backup → Export writes everything — bills, payments and tags — to a single CSV file you can email to yourself or keep in Files. Restore merges that file back by record, updating what it recognises and adding what is missing, without deleting anything.</dd>

    <dt>I stopped a service but want to keep its history</dt>
    <dd>Archive the bill rather than deleting it. It leaves the Overview, the Calendar and reminders, keeps every payment recorded against it, and can be restored later from the Archived screen.</dd>

    <dt>Can I change how it looks?</dt>
    <dd>Settings offers five accent themes, light or dark, and a background of a colour or one of your own photos. On iPad and Mac you can also choose how bills are arranged — a list, a grid, or a board of paper notes. Appearance is set per device on purpose, so your Mac and your phone can differ.</dd>

    <dt>Why are my reminders not arriving?</dt>
    <dd>Reminders need to be switched on in the app <em>and</em> permitted in your device's Settings under Notifications. Archived bills never remind, and a bill can have reminders turned off individually on its own edit screen.</dd>
  </dl>

  <p style="margin-top:34px"><a href="privacy.html">Privacy policy</a></p>
</div></section>
'''

PAGES = [
    ("index.html",   "Bill Compass — never miss a bill again",
     "Bill Compass tracks every bill you owe on iPhone, iPad and Mac. No account, no analytics, and it syncs through your own iCloud.", "", INDEX),
    ("privacy.html", "Privacy Policy — Bill Compass",
     "Bill Compass collects nothing. No account, no analytics, no third-party code; your bills stay on your devices and in your own iCloud.", "Privacy", PRIVACY),
    ("support.html", "Support — Bill Compass",
     "Help with Bill Compass: recording payments, iCloud syncing, backups, reminders and how to get in touch.", "Support", SUPPORT),
]

if __name__ == "__main__":
    os.makedirs(os.path.join(DOCS, "assets"), exist_ok=True)
    open(os.path.join(DOCS, "style.css"), "w").write(CSS)
    # Tells Pages to serve the files as they are rather than running Jekyll.
    open(os.path.join(DOCS, ".nojekyll"), "w").write("")

    # The icon ships with this repo rather than being re-cut from the app's
    # asset catalog, so the site can be rebuilt without the app source
    # checked out. Replace assets/icon.png when the app icon changes.

    for filename, title, desc, current, body in PAGES:
        html = HEAD.format(title=title, desc=desc) + topbar(current) + body + FOOTER + "\n</body>\n</html>\n"
        open(os.path.join(DOCS, filename), "w").write(html)
        print("wrote docs/" + filename)

    # A single-page preview of all three, for reviewing from a phone before
    # Pages is switched on. Artifact pages supply their own document
    # skeleton, so this one carries only the style block and the content.
    preview = ("<title>Bill Compass Site Preview</title>\n<style>" + CSS
               + "\n.previewbar{background:var(--card);border-bottom:1px solid var(--hair);"
                 "padding:14px 24px;font-family:var(--mono);font-size:11px;letter-spacing:.12em;"
                 "text-transform:uppercase;color:var(--muted)}"
                 ".pagebreak{height:1px;background:var(--hair);margin:0}</style>\n"
               + '<link rel="preconnect" href="https://fonts.googleapis.com">'
                 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
                 'family=Bricolage+Grotesque:opsz,wght@12..96,700&family=IBM+Plex+Mono:wght@400&'
                 'family=IBM+Plex+Sans:wght@400;500&display=swap">\n')
    import base64
    with open(os.path.join(DOCS, "assets/icon.png"), "rb") as fh:
        uri = "data:image/png;base64," + base64.b64encode(fh.read()).decode()
    for filename, title, desc, current, body in PAGES:
        preview += (f'<div class="previewbar">{filename}</div>'
                    + body.replace('src="assets/icon.png"', f'src="{uri}"')
                    + '<div class="pagebreak"></div>')
    print("(preview page skipped — build.py writes the site only)")
