"""Rebuilds the Bill Compass site from the copy held in this file.

The product page, a tour of the features, a How to Use guide, a page on
iCloud sync, an FAQ, and the two pages Apple requires before an app can be
submitted — a privacy policy and a support page.

Everything the privacy page claims was checked against the source rather
than assumed: no third-party packages, no URLSession anywhere, and the
diagnostics report's own wording about what it does and does not include.
The guide was written the same way: every menu item, setting and label it
names is the app's own wording, so a reader can find what it points at.

The screenshots in assets/screens come from the app's debug-only
screenshot mode (`-BCScreenshotMode`), which seeds a made-up household into
a store of its own — no real bills appear in them.
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
.wide{max-width:1080px;margin:0 auto;padding:0 24px}
.topbar .wrap{max-width:1080px;flex-wrap:wrap}
.topbar nav{flex-wrap:wrap;row-gap:6px}
footer .wrap{max-width:1080px}
footer nav{display:flex;flex-wrap:wrap;gap:6px 18px}

/* Screenshots: a device's own rounded corners, and a hairline so a light
   screenshot keeps its edge on a light page. */
.shot{display:block;width:100%;height:auto;border-radius:26px;border:1px solid var(--hair);
      box-shadow:0 1px 3px rgba(40,20,50,.10),0 22px 44px -26px rgba(40,20,50,.45);background:var(--card)}
.shot.tablet{border-radius:18px}
figure{margin:0}
figcaption{font-size:14px;color:var(--muted);margin-top:12px;text-align:center}

.hero .pair{display:flex;justify-content:center;gap:22px;margin:44px auto 0;max-width:560px}
.hero .pair figure{flex:1;min-width:0}
.hero .pair figure:last-child{margin-top:44px}
.ctas{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-top:26px}
.btn{display:inline-block;padding:11px 20px;border-radius:999px;font-weight:500;font-size:15.5px;
     text-decoration:none;border:1px solid var(--hair);color:var(--ink);background:var(--card)}
.btn.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.btn:hover{border-color:var(--accent)}

/* A screenshot beside the words about it; stacked on a phone. */
.split{display:grid;grid-template-columns:minmax(0,1fr) 280px;gap:48px;align-items:center}
.split.flip{grid-template-columns:280px minmax(0,1fr)}
.split.flip > figure{order:-1}
.split.tabletcol{grid-template-columns:minmax(0,1fr) minmax(0,1.35fr)}
.split h2{margin-top:0}
.features a{color:inherit;text-decoration:none}
.features li:hover{border-color:var(--accent)}

.steps{counter-reset:step;list-style:none;padding:0;margin:0 0 20px}
.steps > li{counter-increment:step;position:relative;padding-left:44px;margin-bottom:14px}
.steps > li::before{content:counter(step);position:absolute;left:0;top:1px;width:28px;height:28px;
  border-radius:50%;background:var(--card);border:1px solid var(--hair);color:var(--accent);
  font-family:var(--display);font-weight:700;font-size:14px;display:grid;place-items:center}
.three{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:22px;
       counter-reset:step;list-style:none;padding:0;margin:0}
.three li{counter-increment:step;background:var(--card);border:1px solid var(--hair);border-radius:14px;padding:20px 22px}
.three li::before{content:"0" counter(step);display:block;font-family:var(--mono);font-size:12px;
  letter-spacing:.12em;color:var(--accent);margin-bottom:6px}
.three b{display:block;font-family:var(--display);font-size:17px;margin-bottom:4px}
.three span{color:var(--muted);font-size:15px}

/* A drawing of the touch-and-hold menu, since a screenshot can't catch
   a gesture mid-press. */
.menu{max-width:300px;background:var(--card);border:1px solid var(--hair);border-radius:14px;
      box-shadow:0 18px 40px -24px rgba(40,20,50,.5);margin:6px 0 22px;overflow:hidden;font-size:15.5px}
.menu div{padding:10px 16px;border-top:1px solid var(--hair);display:flex;justify-content:space-between;gap:12px}
.menu div:first-child{border-top:0}
.menu div.gap{border-top:6px solid var(--ground)}
.menu .danger{color:#D93A2B}
.menu small{color:var(--muted);font-family:var(--mono);font-size:11px;letter-spacing:.06em}

.toc{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:22px 0 0}
.toc a{display:inline-block;padding:6px 13px;border:1px solid var(--hair);border-radius:999px;
       background:var(--card);color:var(--ink);text-decoration:none;font-size:14.5px}
.toc a:hover{border-color:var(--accent)}
.guide h2{scroll-margin-top:20px;padding-top:12px}
.guide section{padding:38px 0;border-top:1px solid var(--hair)}
.guide section:first-of-type{border-top:0}
.tip{background:var(--card);border:1px solid var(--hair);border-radius:12px;padding:14px 18px;
     margin:4px 0 18px;font-size:15.5px;color:var(--muted)}
.tip b{color:var(--ink)}
.fields{display:grid;grid-template-columns:max-content 1fr;gap:8px 20px;margin:4px 0 20px;font-size:15.5px}
.fields dt{margin:0;font-size:15.5px}
.fields dd{margin:0}
.path{font-family:var(--mono);font-size:.86em;white-space:nowrap}
.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:26px;margin-top:10px}
.price{font-family:var(--display);font-weight:700;font-size:44px;letter-spacing:-.02em;line-height:1;margin:6px 0 10px}

@media (max-width:760px){
  .split,.split.flip,.split.tabletcol{grid-template-columns:1fr;gap:26px}
  .split > figure{max-width:280px;margin:0 auto}
  .split.tabletcol > figure{max-width:none}
  .split.flip > figure{order:0}
}
@media (max-width:520px){
  .hero{padding-top:44px}
  .topbar nav{gap:6px 14px;font-size:14px}
  .hero .pair{gap:14px}
  .hero .pair figure:last-child{margin-top:28px}
  .fields{grid-template-columns:1fr;gap:2px}
  .fields dd{margin-bottom:10px}
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
  <nav>{link("features.html","Features")}{link("guide.html","How to Use")}{link("sync.html","Sync")}{link("faq.html","FAQ")}{link("support.html","Support")}</nav>
</div></header>'''

FOOTER = f'''<footer><div class="wrap">
  <span>Bill Compass — for iPhone, iPad and Mac</span>
  <nav><a href="features.html">Features</a><a href="guide.html">How to Use</a><a href="sync.html">iCloud Sync</a><a href="faq.html">FAQ</a><a href="support.html">Support</a><a href="privacy.html">Privacy</a></nav>
</div></footer>'''


def shot(name, alt, caption="", tablet=False):
    """One screenshot from assets/screens, with its caption if it has one."""
    cls = "shot tablet" if tablet else "shot"
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return (f'<figure><img class="{cls}" src="assets/screens/{name}.jpg" alt="{alt}" '
            f'loading="lazy" decoding="async">{cap}</figure>')


INDEX = f'''
<div class="hero"><div class="wrap">
  <img class="icon" src="assets/icon.png" alt="The Bill Compass app icon">
  <h1>Never miss a bill again</h1>
  <p class="tagline">Every bill you owe, in one calm list — and a month you can see coming.</p>
  <p class="platforms">iPhone · iPad · Mac</p>
  <div class="ctas">
    <a class="btn primary" href="guide.html">How to use it</a>
    <a class="btn" href="features.html">See every feature</a>
  </div>
  <p class="storenote">Coming to the App Store</p>
  <div class="pair">
    {shot("iphone-overview", "The Overview: bills listed soonest first, each with its amount and how many days are left")}
    {shot("iphone-overview-dark", "The same Overview in dark mode")}
  </div>
</div></div>

<section><div class="wrap">
  <h2>Three habits, and you are done</h2>
  <ol class="three">
    <li><b>Add each bill once</b><span>Name, amount, due date and how often it repeats. Bill Compass works out every date after that.</span></li>
    <li><b>Let it remind you</b><span>A notification before each bill falls due, as early as you like — the day of, or up to two weeks ahead.</span></li>
    <li><b>Touch and hold to pay</b><span>Record the payment and the bill rolls on to its next date. Automatic payments record themselves.</span></li>
  </ol>
  <p style="margin-top:22px"><a href="guide.html">Read the full How to Use guide →</a></p>
</div></section>

<section><div class="wrap">
  <h2>What it does</h2>
  <ul class="features">
    <li><a href="features.html#overview"><b>Overview</b><span>Everything still owed, soonest first, with how many days you have left. As a list, a grid, or a wall of paper notes.</span></a></li>
    <li><a href="features.html#calendar"><b>Calendar</b><span>The month laid out by date, so a heavy week is visible before it arrives.</span></a></li>
    <li><a href="features.html#reports"><b>Reports</b><span>What the next 30, 60 and 90 days cost, what each category takes over a year, and what you have paid so far.</span></a></li>
    <li><a href="features.html#history"><b>History</b><span>Every payment you have recorded, grouped by month, including part payments and skipped cycles.</span></a></li>
    <li><a href="features.html#tags"><b>Tags</b><span>Group bills your own way — Essentials, Household, Family — and see what each group costs.</span></a></li>
    <li><a href="features.html#reminders"><b>Reminders</b><span>A notification before a bill is due, with the lead time set per bill rather than one rule for all.</span></a></li>
  </ul>
</div></section>

<section><div class="wide">
  <div class="split tabletcol">
    <div>
      <h2>Room to spread out on iPad and Mac</h2>
      <p class="lead">A sidebar with your tags in it, a calendar that shows each bill on its day, and a choice of layouts — a list, a grid, or a board of paper notes.</p>
      <p><a href="features.html#layouts">More about layouts →</a></p>
    </div>
    {shot("ipad-stickie", "Bill Compass on iPad, with bills laid out as paper notes and tags in the sidebar", tablet=True)}
  </div>
</div></section>

<section><div class="wrap">
  <h2>It syncs, and it stays yours</h2>
  <div class="pledge">
    <span class="stamp">Privacy</span>
    <p>Bill Compass has no account, no server of ours, and no analytics. Your bills live on your device and sync through <b>your own iCloud</b>, which we cannot read. Nothing is collected, and nothing is sold.</p>
  </div>
  <p class="lead">Add a bill on your phone and it is on your Mac. Appearance stays per device on purpose — a Mac on a desk and a phone in bed are entitled to different answers.</p>

  <div class="pledge" style="border-left-color:var(--accent)">
    <span class="stamp" style="color:var(--accent)">One-time purchase</span>
    <p><b>Lifetime iCloud Sync — $7.99.</b> Bill Compass works fully on a single device. Keeping the same bills on your iPhone, iPad and Mac is the one thing that costs, and it is bought once — not a subscription. It unlocks on every device signed in to the same Apple Account.</p>
  </div>
  <p><a href="sync.html">How iCloud sync works</a> · <a href="privacy.html">Read the full privacy policy</a></p>
</div></section>
'''


FEATURES = f'''
<section><div class="wrap">
  <h1 style="font-size:clamp(30px,5.5vw,44px);margin-top:0">Features</h1>
  <p class="lead">A tour of every screen. For step-by-step instructions, see <a href="guide.html">How to Use</a>.</p>
</div></section>

<section id="overview" style="padding-top:0"><div class="wide">
  <div class="split">
    <div>
      <h2>Overview — what you owe, soonest first</h2>
      <p>Every bill you are tracking, in due-date order, with its amount and a plain countdown: <em>Due today</em>, <em>Due in 3 days</em>, <em>Overdue</em>. The colour of the countdown tells you how close it is, from red for late through amber to teal for comfortably far off.</p>
      <p>Two filters narrow the list: <b>Category</b>, and <b>Due</b> — Overdue, Current Month, or the next 30, 60 or 90 days. A half-filled circle marks a bill you have part paid.</p>
      <p>The dot beside the page title is the one-glance verdict: <b style="color:var(--green)">green</b> when nothing is late, <b style="color:var(--gold)">amber</b> at one or two overdue bills, red beyond that.</p>
    </div>
    {shot("iphone-overview", "The Overview screen")}
  </div>
</div></section>

<section id="calendar"><div class="wide">
  <div class="split flip">
    {shot("iphone-calendar", "The Calendar screen, with dots under the days that have bills due")}
    <div>
      <h2>Calendar — a month you can see coming</h2>
      <p>The month laid out by date, with a mark on every day that has a bill due. Pick a day and the list beneath opens at it, so you can read ahead from any point in the month. <b>Today</b> brings you back.</p>
      <p>On iPad and Mac the calendar is large enough to name each bill on its day.</p>
      <p>The Calendar shows only what is still owed. Once a bill is paid, its record lives in History.</p>
    </div>
  </div>
</div></section>

<section id="history"><div class="wide">
  <div class="split">
    <div>
      <h2>History — every payment, kept</h2>
      <p>Every payment you have recorded, newest first and grouped by month. Each one says whether it was <b>paid in full</b>, a <b>partial payment</b>, or a <b>skipped</b> cycle, with the confirmation number or note you gave it.</p>
      <p>Filter to a single bill to see its whole record. Open a payment to read it, correct it, or delete it.</p>
    </div>
    {shot("iphone-history", "The History screen, listing payments for September")}
  </div>
</div></section>

<section id="reports"><div class="wide">
  <div class="split flip">
    {shot("iphone-reports", "The Reports screen: upcoming totals and the annual projection by category")}
    <div>
      <h2>Reports — the year in figures</h2>
      <p><b>Upcoming</b> adds up what falls due in the next 30, 60 and 90 days.</p>
      <p><b>Annual Projection</b> is what a year of your recurring bills comes to, broken down by category. Bills whose amount varies are averaged from what you have actually paid, so they only count once they have a payment recorded.</p>
      <p><b>Paid This Year</b> is the other half: what has actually gone out since January 1, bill by bill, with how many payments and when the last one was.</p>
    </div>
  </div>
</div></section>

<section id="tags"><div class="wide">
  <div class="split">
    <div>
      <h2>Tags — your own groups</h2>
      <p>Categories say what a bill is for; tags group bills the way you think about them. A bill can carry as many as you like — Essentials, Household, Family, Subscriptions — and each tag shows how many bills it holds and what they cost a year.</p>
      <p>On iPad and Mac every tag sits in the sidebar, one click away.</p>
    </div>
    {shot("iphone-tags", "The Tags screen, with the yearly cost of each tag")}
  </div>
</div></section>

<section id="reminders"><div class="wrap">
  <h2>Reminders, set per bill</h2>
  <p>A notification before each bill is due — on the day, 1 day, 3 days, 1 week or 2 weeks before — at a time of day you choose. Each bill keeps its own lead time, so the rent can warn you a week out while a streaming service warns you on the day. You can also ask for a second reminder on the due date itself.</p>
  <p>The app icon carries a badge counting the bills that are due or overdue.</p>
  <p>Reminders are scheduled on your device. Nothing is sent to a server to make them appear, and they keep working offline.</p>
</div></section>

<section id="automatic"><div class="wrap">
  <h2>Automatic payments that record themselves</h2>
  <p>Mark a direct debit or card-on-file bill <b>Recorded Automatically</b> and, on its due date, Bill Compass records the payment for you and moves the bill to its next date — the same as recording it by hand. Its reminder asks for the one thing that can still go wrong: that enough money is in the account.</p>
  <p>A cycle with no amount yet — an electricity bill whose statement has not arrived — waits for you instead of being recorded as $0.00.</p>
</div></section>

<section id="layouts"><div class="wide">
  <h2>Three layouts on iPad and Mac</h2>
  <p class="lead" style="max-width:62ch">Choose how the Overview arranges your bills in Settings → Appearance → Bill Layout: <b>Tile</b>, a list of rows; <b>Grid</b>, cards side by side; or <b>Stickie</b>, a board of paper notes. The iPhone keeps the list, which suits its width best.</p>
  <div class="gallery" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr))">
    {shot("ipad-grid", "Bills arranged as a grid of cards on iPad", "Grid", tablet=True)}
    {shot("ipad-stickie", "Bills arranged as paper notes on iPad", "Stickie", tablet=True)}
    {shot("ipad-calendar", "The Calendar on iPad, with each bill named on its day", "Calendar on iPad", tablet=True)}
  </div>
</div></section>

<section id="more"><div class="wrap">
  <h2>And the rest</h2>
  <ul class="features">
    <li><b>Partial payments</b><span>Pay part of a bill and it stays due, showing what is still owed, until the rest is paid.</span></li>
    <li><b>Skip a cycle</b><span>A bill that was not due this time moves on without money changing hands, and History notes the gap.</span></li>
    <li><b>Varying amounts</b><span>For utilities: the amount clears after each payment, ready for the next statement.</span></li>
    <li><b>Archive</b><span>Stop tracking a bill without losing its history. Restore it any time.</span></li>
    <li><b>Backup to CSV</b><span>Export everything to one file you keep, and restore from it without deleting anything.</span></li>
    <li><b>Make it yours</b><span>Five accent colours, light or dark, and a background colour or photo — chosen per device.</span></li>
    <li><b>Payment methods</b><span>Name the cards and accounts you pay from, and note which one settled each bill.</span></li>
    <li><b>Any currency</b><span>Follows your device's region, or pick a currency of your own.</span></li>
    <li><b>iCloud sync</b><span>The same bills on iPhone, iPad and Mac, through your own iCloud. <a href="sync.html">A one-time purchase</a>.</span></li>
  </ul>
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
  <p>Bills, payments and tags are stored on your device. If you have unlocked iCloud sync and are signed in to iCloud, they also sync through Apple's CloudKit to your <em>private</em> iCloud database, so the same bills appear on your other devices. That database belongs to your Apple Account. The developer has no access to it and no way to read what is in it.</p>
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


GUIDE = f'''
<section><div class="wrap">
  <h1 style="font-size:clamp(30px,5.5vw,44px);margin-top:0">How to Use Bill Compass</h1>
  <p class="lead">Everything from your first bill to backups, in the order you are likely to need it. Menu and setting names are written exactly as they appear in the app.</p>
  <ul class="toc">
    <li><a href="#start">Getting started</a></li>
    <li><a href="#add">Adding a bill</a></li>
    <li><a href="#act">Acting on a bill</a></li>
    <li><a href="#pay">Recording a payment</a></li>
    <li><a href="#skip">Skipping a cycle</a></li>
    <li><a href="#auto">Automatic payments</a></li>
    <li><a href="#overview">The Overview</a></li>
    <li><a href="#calendar">The Calendar</a></li>
    <li><a href="#history">History</a></li>
    <li><a href="#reports">Reports</a></li>
    <li><a href="#tags">Tags</a></li>
    <li><a href="#archive">Archiving</a></li>
    <li><a href="#reminders">Reminders</a></li>
    <li><a href="#settings">Settings</a></li>
    <li><a href="#backup">Backup and restore</a></li>
    <li><a href="#mac">On the Mac</a></li>
  </ul>
</div></section>

<div class="guide"><div class="wrap">

<section id="start">
  <h2>Getting started</h2>
  <p>The first time Bill Compass opens it asks whether you would like reminders, then points out the two things you need to find: the <b>+</b> button for adding a bill, and the <b>Calendar</b>. After your first bill is added it shows you, once, how to record a payment.</p>
  <p>On iPhone, the five main screens — <b>Overview</b>, <b>Calendar</b>, <b>History</b>, <b>Reports</b> and <b>Tags</b> — are tabs along the bottom. <b>Archived</b> and <b>Settings</b> are in the <b>•••</b> menu at the top left. On iPad and Mac every screen is in the sidebar, with each of your tags listed beneath.</p>
</section>

<section id="add">
  <h2>Adding a bill</h2>
  <ol class="steps">
    <li>Tap the round <b>+</b> button in the bottom corner of the Overview or the Calendar. From the Calendar, the day you have selected is filled in as the due date.</li>
    <li>Fill in the bill, then tap <b>Save</b>.</li>
  </ol>
  <dl class="fields">
    <dt>Name</dt><dd>What you call the bill — Rent, Electricity, Gym.</dd>
    <dt>Category</dt><dd>What the bill is for. It chooses the bill's icon and groups it in Reports.</dd>
    <dt>Amount</dt><dd>What each cycle costs.</dd>
    <dt>Amount Varies Each Bill</dt><dd>For bills like electricity or water. After a full payment the amount clears to zero, ready for the next statement — enter it when you know it.</dd>
    <dt>Recorded Automatically</dt><dd>For direct debits and cards on file. See <a href="#auto">Automatic payments</a>.</dd>
    <dt>Due Date</dt><dd>The next date this bill is due.</dd>
    <dt>Frequency</dt><dd>One-Time, Weekly, Every 2 Weeks, Monthly, Every 2 Months, Every 3 Months, Every 6 Months or Yearly.</dd>
    <dt>Has End Date</dt><dd>For a bill that stops — a loan's last instalment, a fixed-term contract.</dd>
    <dt>Reminder</dt><dd>Whether this bill reminds you, and how far ahead (<b>Remind Me</b>).</dd>
    <dt>Tags</dt><dd>Type a name in <b>New Tag</b> and press Return to make a tag, then tick the ones this bill belongs to.</dd>
    <dt>Website, Notes</dt><dd>Optional. Where you pay it, an account number, anything else worth keeping.</dd>
  </dl>
  <div class="tip"><b>Tip:</b> enter the <em>next</em> due date, not the first one you ever paid. Bill Compass works out every date after it from the frequency.</div>
</section>

<section id="act">
  <h2>Acting on a bill</h2>
  <p><b>Tapping a bill does nothing, on purpose.</b> You scroll past bills far more often than you act on them, and a tap that opened something would turn every interrupted scroll into a payment screen. Instead:</p>
  <ul class="plain">
    <li><b>Touch and hold</b> a bill (right-click on a Mac) to open its menu.</li>
    <li>On iPhone and iPad you can also <b>swipe</b>: swipe right for <b>Pay</b> and <b>Skip</b>, swipe left for <b>Edit</b>, <b>Archive</b> and <b>Delete</b>.</li>
    <li>On a Mac, <b>double-click</b> a bill to record a payment.</li>
  </ul>
  <div class="menu" role="img" aria-label="The menu a bill opens: Record Payment, Skip This Cycle, Payment History, Edit, Archive, Delete">
    <div>Record Payment</div>
    <div>Skip This Cycle</div>
    <div class="gap">Payment History</div>
    <div>Edit</div>
    <div>Archive</div>
    <div class="gap danger">Delete</div>
  </div>
</section>

<section id="pay">
  <h2>Recording a payment</h2>
  <ol class="steps">
    <li>Touch and hold the bill and choose <b>Record Payment</b>.</li>
    <li>Check the amount. Choose <b>Full</b> if this settles the cycle, or <b>Partial</b> if you have paid only part of it.</li>
    <li>Set the <b>Payment Date</b> if it was not today, and optionally a <b>Payment Method</b>, a <b>Confirmation Number</b> and a <b>Note</b>.</li>
    <li>Save.</li>
  </ol>
  <p>A <b>full</b> payment moves the bill to its next due date, and the payment appears in History. A <b>partial</b> payment leaves the bill due, marked with a half-filled circle, until the rest is paid. A one-time bill paid in full is finished.</p>
  <div class="tip"><b>Paid late or early?</b> Record it with the date you actually paid. The bill still moves on by one cycle.</div>
</section>

<section id="skip">
  <h2>Skipping a cycle</h2>
  <p>When a bill was not due this time — a holiday from the gym, a waived fee — touch and hold it and choose <b>Skip This Cycle</b>. It moves on to its next date without money being recorded, and History lists the skip so the gap is explained later.</p>
</section>

<section id="auto">
  <h2>Automatic payments</h2>
  <p>Turn on <b>Recorded Automatically</b> for any bill that leaves your account by itself. On its due date Bill Compass records a full payment for you and moves the bill on, exactly as if you had done it by hand. Its reminder becomes a nudge to <em>ensure enough funds are available in the account</em>. Such bills carry a small <b>A</b> beside their name.</p>
  <p>A bill whose amount is still zero — a varying bill whose statement has not arrived — is left for you to record, rather than logged as a $0.00 payment.</p>
</section>

<section id="overview">
  <h2>The Overview</h2>
  <p>Your bills, soonest first. Each shows its amount and a countdown whose colour says how close it is: red for overdue, then orange and amber as the date approaches, and teal when it is comfortably far off.</p>
  <p>Use <b>Category</b> to show one kind of bill, and <b>Due</b> to show Overdue, Current Month, or the Next 30, 60 or 90 Days. The two combine. <b>Show All Bills</b> clears them.</p>
  <p>The coloured dot beside the page title is your status at a glance — green when nothing is overdue, amber for one or two overdue bills, red for more.</p>
</section>

<section id="calendar">
  <h2>The Calendar</h2>
  <p>Days with a bill due are marked. Select a day and the list beneath opens at it, showing that day's bills and everything after. <b>Today</b> returns to the current date, and the arrows beside the month step between months. Bills in the list respond to touch and hold exactly as they do on the Overview.</p>
  <p>The Calendar lists only what you still owe. Paid bills are in History.</p>
</section>

<section id="history">
  <h2>History</h2>
  <p>Every payment you have recorded, grouped by month and marked <b>Paid in full</b>, <b>Partial payment</b> or skipped. Use the <b>Payments</b> filter to show one bill's record — or choose <b>Payment History</b> from any bill's menu to jump straight there.</p>
  <p>Touch and hold a payment for <b>View Payment</b>, <b>Edit Payment</b> or <b>Delete Payment</b>. Deleting a full payment or a skip also puts the bill back on the date it was due before, so a mistaken payment is undone completely. A skip can be deleted but not edited.</p>
</section>

<section id="reports">
  <h2>Reports</h2>
  <ul class="plain">
    <li><b>Upcoming</b> — the total of everything falling due in the next 30, 60 and 90 days.</li>
    <li><b>Annual Projection</b> — what a year of your recurring bills costs, by category. Tap the <b>ⓘ</b> beside a category to see how its figure is worked out. One-time bills are not counted, and varying bills count once they have a payment to average.</li>
    <li><b>Paid This Year</b> — what you have actually paid since January 1, bill by bill, with a total. Archived bills are included, because that money was still spent this year.</li>
  </ul>
</section>

<section id="tags">
  <h2>Tags</h2>
  <p>Make a tag from a bill's edit screen (type it in <b>New Tag</b> and press Return), or from the Tags screen's <b>+</b> button. Open a tag to see its bills and their yearly cost. Touch and hold a tag to <b>Rename</b> or <b>Delete</b> it — deleting a tag never deletes its bills.</p>
</section>

<section id="archive">
  <h2>Archiving a bill</h2>
  <p>When you stop paying something but want to keep its record, choose <b>Archive</b> from the bill's menu. It leaves the Overview, the Calendar and your reminders, and every payment against it is kept.</p>
  <p>Find archived bills under <b>Archived</b> (in the <b>•••</b> menu on iPhone, in the sidebar on iPad and Mac). From there you can <b>Restore</b> a bill to the Overview, see its <b>Payment History</b>, or delete it for good — which also deletes its payments and cannot be undone.</p>
</section>

<section id="reminders">
  <h2>Reminders</h2>
  <ol class="steps">
    <li>Open <b>Settings</b> and turn on <b>Bill Reminders</b>. Allow notifications when your device asks.</li>
    <li>Choose a <b>Time Of Day</b> for reminders to arrive.</li>
    <li>Choose how far ahead <b>New Bills Remind</b> you — on the due date, 1 day, 3 days, 1 week or 2 weeks before. This is the starting point for bills you add from now on; each bill keeps its own setting, which you can change on its edit screen.</li>
    <li>Turn on <b>Also On The Due Date</b> for a second reminder on the day itself.</li>
  </ol>
  <p>The number on the app icon counts bills that are overdue or coming due within your reminder window.</p>
</section>

<section id="settings">
  <h2>Settings</h2>
  <dl class="fields">
    <dt>Open On</dt><dd>The screen Bill Compass starts on.</dd>
    <dt>Appearance</dt><dd><b>Theme</b> (light, dark or matching your device), an <b>Accent</b> colour, and on iPad and Mac the <b>Bill Layout</b> — Tile, Grid or Stickie.</dd>
    <dt>Background</dt><dd>A colour or one of your own photos behind the app.</dd>
    <dt>Reminders</dt><dd>See <a href="#reminders">Reminders</a>.</dd>
    <dt>Currency</dt><dd>Match your device's region, or choose one.</dd>
    <dt>Payment Methods</dt><dd>The cards and accounts offered when you record a payment. Add your own, or remove the ones you do not use.</dd>
    <dt>iCloud</dt><dd>Sync status, and where to unlock or restore <a href="sync.html">Lifetime iCloud Sync</a>.</dd>
    <dt>Backup</dt><dd>See <a href="#backup">Backup and restore</a>.</dd>
    <dt>Diagnostics</dt><dd>Version, iCloud status and what is stored — with a report you can copy into a support email.</dd>
  </dl>
  <p>Appearance, reminder times and the start screen are set per device, so your Mac and your phone can differ. Your bills, payments, tags and payment methods are your data and sync with the rest.</p>
</section>

<section id="backup">
  <h2>Backup and restore</h2>
  <p><span class="path">Settings → Backup → Export Backup…</span> writes your bills, payments and tags to a single CSV file. Save it to Files, email it to yourself, or keep it anywhere you like.</p>
  <p><span class="path">Restore From Backup…</span> reads that file back. It merges by record — updating what it recognises and adding what is missing — and never deletes anything already in the app.</p>
</section>

<section id="mac">
  <h2>On the Mac</h2>
  <ul class="plain">
    <li><b>Right-click</b> a bill for its menu; <b>double-click</b> to record a payment.</li>
    <li><span class="path">⌘T</span> jumps the Calendar to today; <span class="path">⌘[</span> and <span class="path">⌘]</span> step between months.</li>
    <li><span class="path">⌥⌘K</span> switches the bill list between standard and compact tiles, to fit more on screen.</li>
    <li>With sync on, the <b>Sync Now</b> toolbar button asks iCloud for changes straight away.</li>
  </ul>
</section>

</div></div>

<section><div class="wrap">
  <p class="lead">Still stuck? The <a href="faq.html">FAQ</a> covers the common questions, and <a href="support.html">Support</a> has a real person at the other end.</p>
</div></section>
'''


SYNC = f'''
<section><div class="wrap">
  <h1 style="font-size:clamp(30px,5.5vw,44px);margin-top:0">iCloud Sync</h1>
  <p class="lead">The same bills on your iPhone, iPad and Mac — through your own iCloud, which only you can read.</p>

  <div class="pledge" style="border-left-color:var(--accent)">
    <span class="stamp" style="color:var(--accent)">Lifetime iCloud Sync</span>
    <p class="price">$7.99</p>
    <p>One payment, no subscription. It unlocks sync on every device signed in to the same Apple Account. Everything else in Bill Compass works without it, on a single device.</p>
  </div>

  <h2>Turning it on</h2>
  <ol class="steps">
    <li>Make sure the device is signed in to iCloud with <b>iCloud Drive</b> on.</li>
    <li>Open <span class="path">Settings → iCloud</span> and choose <b>Unlock Sync</b>.</li>
    <li>Quit and reopen Bill Compass. The app chooses its database as it launches, so sync starts on the next launch, and Settings will say so until then.</li>
    <li>On each of your other devices, open <span class="path">Settings → iCloud</span> and choose <b>Restore Purchase</b>, then reopen the app. You are not charged again.</li>
  </ol>
  <div class="tip"><b>Started on one device already?</b> When Bill Compass finds it is already in use on your iCloud account — say, you open the Mac app after a year on your phone — it tells you so, and offers to turn sync on, rather than leaving you with an empty screen and a guess.</div>

  <h2>How it works</h2>
  <p>Your bills are stored on each device and mirrored through Apple's CloudKit into the <em>private</em> database of your own iCloud account. There is no Bill Compass server and no account to make; the developer cannot see your data. See the <a href="privacy.html">privacy policy</a>.</p>
  <p>What syncs: bills, payments, tags and payment methods. What stays on each device: appearance, background, bill layout, reminder settings and the screen the app opens on.</p>
  <p>iCloud delivers changes in the background, usually within a minute or two. To ask for them straight away, pull down on the bill list on iPhone and iPad, or use <b>Sync Now</b> in the Mac toolbar.</p>

  <h2>If something has not synced</h2>
  <ul class="plain">
    <li>Check <span class="path">Settings → iCloud</span> on <em>both</em> devices says sync is on.</li>
    <li>Both must be signed in to the same Apple Account, with iCloud Drive on.</li>
    <li>A device that has been asleep may need the app opened once to catch up.</li>
    <li><span class="path">Settings → Diagnostics</span> shows whether sync is running and when data was last sent and received.</li>
    <li>Still stuck? <a href="support.html">Get in touch</a>, and include the Diagnostics report.</li>
  </ul>
</div></section>
'''


FAQ = f'''
<section><div class="wrap">
  <h1 style="font-size:clamp(30px,5.5vw,44px);margin-top:0">Frequently Asked Questions</h1>
  <p class="lead">Can't find your answer? See the <a href="guide.html">How to Use guide</a> or <a href="support.html">contact support</a>.</p>

  <h2 style="margin-top:40px">Using the app</h2>
  <dl>
    <dt>Tapping a bill does nothing. Is it broken?</dt>
    <dd>No — that is deliberate, so scrolling can never settle a bill by accident. Touch and hold a bill to record a payment, edit it or skip a cycle. On iPhone and iPad you can also swipe it; on a Mac, right-click or double-click.</dd>

    <dt>How do I record a payment?</dt>
    <dd>Touch and hold the bill and choose Record Payment. A full payment moves the bill on to its next cycle; a partial payment leaves it due and shows what is still owed. You can do the same from the bills under the Calendar.</dd>

    <dt>A bill was not due this month</dt>
    <dd>Touch and hold it and choose Skip This Cycle. That moves the bill forward without recording money, and the skip is listed in History so the gap is explained.</dd>

    <dt>My electricity bill is different every month</dt>
    <dd>Turn on Amount Varies Each Bill. After each full payment the amount clears to zero, ready for you to enter the next statement's figure. Reports averages such bills from what you have actually paid.</dd>

    <dt>Can the app record payments that come out automatically?</dt>
    <dd>Yes — turn on Recorded Automatically for that bill. Bill Compass records the payment on the due date and moves the bill on. It never moves money itself; it only keeps the record.</dd>

    <dt>I recorded a payment by mistake</dt>
    <dd>Find it in History, touch and hold it, and choose Edit Payment to correct it or Delete Payment to remove it. Deleting it also puts the bill back on the date it was due before, so it is owed again.</dd>

    <dt>I stopped a service but want to keep its history</dt>
    <dd>Archive the bill rather than deleting it. It leaves the Overview, the Calendar and reminders, keeps every payment recorded against it, and can be restored later from the Archived screen.</dd>

    <dt>What does the coloured dot next to the title mean?</dt>
    <dd>It is your status at a glance: green when nothing is overdue, amber when one or two bills are, red when more are.</dd>

    <dt>Where are Settings and Archived on iPhone?</dt>
    <dd>In the ••• menu at the top left of the screen.</dd>

    <dt>Can I change how it looks?</dt>
    <dd>Settings offers five accent colours, light or dark, and a background of a colour or one of your own photos. On iPad and Mac you can also choose how bills are arranged — a list, a grid, or a board of paper notes. Appearance is set per device on purpose, so your Mac and your phone can differ.</dd>
  </dl>

  <h2 style="margin-top:48px">Reminders</h2>
  <dl>
    <dt>Why are my reminders not arriving?</dt>
    <dd>Reminders need to be switched on in the app <em>and</em> permitted in your device's Settings under Notifications. Archived bills never remind, and a bill can have reminders turned off individually on its own edit screen.</dd>

    <dt>I changed the reminder setting but my bills did not change</dt>
    <dd>New Bills Remind sets the starting point for bills you add from now on. Each existing bill keeps its own lead time — change it on that bill's edit screen.</dd>

    <dt>What does the number on the app icon mean?</dt>
    <dd>How many bills are overdue or coming due within your reminder window.</dd>
  </dl>

  <h2 style="margin-top:48px">Sync and purchases</h2>
  <dl>
    <dt>Do I have to pay to sync?</dt>
    <dd>Syncing between devices is a one-time <b>Lifetime iCloud Sync</b> purchase of $7.99 — not a subscription. Everything else works without it, on one device. Because it is tied to your Apple Account, buying it once covers your iPhone, your iPad and your Mac.</dd>

    <dt>I bought sync but nothing is syncing yet</dt>
    <dd>Reopen the app. Bill Compass decides how to open your database when it launches, so a purchase made while it is running takes effect the next time you start it. Settings will say so after you buy.</dd>

    <dt>I already bought it, but a new device says sync is off</dt>
    <dd>Settings → iCloud → <b>Restore Purchase</b>, with the device signed in to the same Apple Account you bought it on. Nothing is charged twice.</dd>

    <dt>My bills have not appeared on my other device</dt>
    <dd>First, check sync is unlocked on both devices — Settings → iCloud. Then both need to be signed in to the same Apple Account with iCloud Drive on. Syncing is handled by iCloud and is not instant — it can take a few minutes, and a device that has been asleep may need the app opened once. On iPhone and iPad you can pull down on the bill list to prompt a refresh; on a Mac, use Sync Now. Settings → Diagnostics shows whether sync is on and when data was last sent and received. More on the <a href="sync.html">iCloud Sync page</a>.</dd>
  </dl>

  <h2 style="margin-top:48px">Your data</h2>
  <dl>
    <dt>How do I back up my bills?</dt>
    <dd>Settings → Backup → Export Backup… writes everything — bills, payments and tags — to a single CSV file you can email to yourself or keep in Files. Restore From Backup… merges that file back by record, updating what it recognises and adding what is missing, without deleting anything.</dd>

    <dt>Does Bill Compass connect to my bank?</dt>
    <dd>No. It never sees your bank, never moves money, and makes no network requests of its own. It keeps the record you give it.</dd>

    <dt>Who can see my bills?</dt>
    <dd>Only you. They are stored on your devices and, with sync, in your own private iCloud database. There is no account, no analytics and no server of ours. See the <a href="privacy.html">privacy policy</a>.</dd>
  </dl>
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

  <h2>Before you write</h2>
  <ul class="features">
    <li><a href="guide.html"><b>How to Use</b><span>Step-by-step instructions for every screen, from your first bill to backups.</span></a></li>
    <li><a href="faq.html"><b>FAQ</b><span>Answers to the questions that come up most.</span></a></li>
    <li><a href="sync.html"><b>iCloud Sync</b><span>Turning sync on, restoring your purchase, and what to check when it is slow.</span></a></li>
  </ul>

  <h2 style="margin-top:48px">The questions asked most</h2>
  <dl>
    <dt>Tapping a bill does nothing. Is it broken?</dt>
    <dd>No — that is deliberate, so scrolling can never settle a bill by accident. Touch and hold a bill to record a payment, edit it or skip a cycle. On a Mac, right-click or double-click.</dd>

    <dt>I bought sync but nothing is syncing yet</dt>
    <dd>Reopen the app. Bill Compass decides how to open your database when it launches, so a purchase made while it is running takes effect the next time you start it.</dd>

    <dt>I already bought sync, but a new device says it is off</dt>
    <dd>Settings → iCloud → <b>Restore Purchase</b>, with the device signed in to the same Apple Account you bought it on. Nothing is charged twice.</dd>

    <dt>Why are my reminders not arriving?</dt>
    <dd>Reminders need to be switched on in the app <em>and</em> permitted in your device's Settings under Notifications. Archived bills never remind, and a bill can have reminders turned off individually on its own edit screen.</dd>
  </dl>

  <p style="margin-top:34px"><a href="faq.html">All questions</a> · <a href="privacy.html">Privacy policy</a></p>
</div></section>
'''

PAGES = [
    ("index.html",    "Bill Compass — never miss a bill again",
     "Bill Compass tracks every bill you owe on iPhone, iPad and Mac. No account, no analytics, and it syncs through your own iCloud.", "", INDEX),
    ("features.html", "Features — Bill Compass",
     "Every screen in Bill Compass: the Overview, Calendar, History, Reports, Tags, reminders, automatic payments and layouts for iPad and Mac.", "Features", FEATURES),
    ("guide.html",    "How to Use — Bill Compass",
     "Step-by-step help for Bill Compass: adding bills, recording and skipping payments, the Calendar, Reports, tags, reminders, archiving and backups.", "How to Use", GUIDE),
    ("sync.html",     "iCloud Sync — Bill Compass",
     "Lifetime iCloud Sync keeps the same bills on your iPhone, iPad and Mac through your own iCloud — a one-time $7.99 purchase.", "Sync", SYNC),
    ("faq.html",      "FAQ — Bill Compass",
     "Answers to common Bill Compass questions: recording payments, reminders, iCloud sync and purchases, backups and privacy.", "FAQ", FAQ),
    ("privacy.html",  "Privacy Policy — Bill Compass",
     "Bill Compass collects nothing. No account, no analytics, no third-party code; your bills stay on your devices and in your own iCloud.", "Privacy", PRIVACY),
    ("support.html",  "Support — Bill Compass",
     "Help with Bill Compass: how to get in touch, the questions asked most, and where to find the guide and FAQ.", "Support", SUPPORT),
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
