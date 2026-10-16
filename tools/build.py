#!/usr/bin/env python3
"""Static site generator (standard library only).

    python3 tools/build.py

Reads tools/content.py and writes index.html, research.html, 404.html, projects/*.html,
sitemap.xml and robots.txt into the repository root, which is what GitHub Pages serves.
"""
import hashlib
import html
import json
import os
import re
import sys
from datetime import date
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
import content as C  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
esc = lambda s: html.escape(s, quote=True)
YEAR = date.today().year


def q(path):
    """URL-encode a repo-relative path (folders contain spaces and '&')."""
    return quote(path, safe="/")


def image_size(rel, default=(1200, 800)):
    """Read pixel size from a WebP header (VP8 / VP8L / VP8X) without third-party libraries."""
    try:
        if rel.endswith(".svg"):
            with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
                head = f.read(400)
            w, h = re.search(r'width="(\d+)"', head), re.search(r'height="(\d+)"', head)
            return (int(w.group(1)), int(h.group(1))) if w and h else default
        with open(os.path.join(ROOT, rel), "rb") as f:
            d = f.read(40)
        kind = d[12:16]
        if kind == b"VP8X":
            return 1 + int.from_bytes(d[24:27], "little"), 1 + int.from_bytes(d[27:30], "little")
        if kind == b"VP8 ":
            return int.from_bytes(d[26:28], "little") & 0x3FFF, int.from_bytes(d[28:30], "little") & 0x3FFF
        if kind == b"VP8L":
            b = int.from_bytes(d[21:25], "little")
            return (b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1
    except OSError:
        pass
    return default


def asset_version(name):
    with open(os.path.join(ROOT, name), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


CSS_V, JS_V = asset_version("style.css"), asset_version("script.js")
PROJECTS = {p["slug"]: p for p in C.PROJECTS}
CATEGORY_LABEL = dict(C.CATEGORIES)


# ---------------------------------------------------------------------------
# Shared pieces
# ---------------------------------------------------------------------------
def page(*, title, desc, path, depth, body, nav_active="", extra_head="", body_class="", prefix=None):
    """Wrap `body` in the shared document shell. `depth` is how many folders deep the page lives."""
    p = prefix if prefix is not None else "../" * depth
    url = C.SITE_URL + path
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-4WB2LLQP50"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {{ dataLayer.push(arguments); }}
        gtag('js', new Date());
        gtag('config', 'G-4WB2LLQP50');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="canonical" href="{url}">
    <meta name="theme-color" content="#1c1917">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{C.SITE_URL}images/selfie.jpg">
    <meta name="twitter:card" content="summary">
    <link rel="icon" href="{p}images/icons/icon-48.png" type="image/png">
    <link rel="apple-touch-icon" href="{p}images/icons/icon-180.png">
    <link rel="preload" href="{p}fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin>
    <script>document.documentElement.classList.add('js')</script>
    <link rel="stylesheet" href="{p}style.css?v={CSS_V}">{extra_head}
</head>

<body class="{body_class}">
    <a class="skip-link" href="#main">Skip to content</a>
{nav(p, nav_active)}
{body}
{footer(p)}
    <button id="backToTop" class="back-to-top" aria-label="Back to top">
        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M18 15l-6-6-6 6" />
        </svg>
    </button>
    <script src="{p}script.js?v={JS_V}"></script>
</body>

</html>
"""


def nav(p, active):
    home = "" if active == "home" else p + "index.html"
    items = [
        ("about", "About", f"{home}#about"),
        ("education", "Education", f"{home}#education"),
        ("experience", "Experience", f"{home}#experience"),
        ("research", "Research", "#research" if active == "home" else f"{p}research.html"),
        ("publications", "Publications", f"{p}research.html#publications"),
        ("awards", "Awards", f"{home}#awards"),
        ("contact", "Contact", f"{home}#contact"),
    ]
    links = []
    for key, label, href in items:
        cur = ' aria-current="page"' if key == active else ""
        links.append(f'                <li><a href="{href}"{cur}>{label}</a></li>')
    links.append(f'                <li><a href="{C.BLOG}" target="_blank" rel="noopener">Blog ↗</a></li>')
    links.append(f'                <li><a class="btn btn-outline" href="{C.CV_URL}" target="_blank" rel="noopener">CV</a></li>')
    return f"""    <header class="site-nav">
        <div class="container">
            <div class="logo"><a href="{p}index.html">{C.NAME}</a></div>
            <button class="nav-toggle" aria-expanded="false" aria-controls="site-menu" aria-label="Menu"><span></span></button>
            <nav aria-label="Primary">
                <ul class="nav-links" id="site-menu">
{chr(10).join(links)}
                </ul>
            </nav>
        </div>
    </header>"""


def footer(p):
    socials = [
        ("mailto:" + C.EMAIL, "Email", "email_white_44dp.png", ""),
        (C.GITHUB, "GitHub", "github_white_44dp.png", ' target="_blank" rel="noopener"'),
        (C.LINKEDIN, "LinkedIn", "linkedin_white_44dp.png", ' target="_blank" rel="noopener"'),
        (C.BLOG, "Blog", "blog_white.svg", ' target="_blank" rel="noopener"'),
        (C.MEDIUM, "Medium", "medium_white_44dp.png", ' target="_blank" rel="noopener"'),
        (C.SCHOLAR, "Google Scholar", "google_scholar_icon.png", ' target="_blank" rel="noopener"'),
    ]
    icons = "\n".join(
        f'                <a href="{u}"{t} title="{n}"><img src="{p}images/icons/{i}" alt="{n}" class="social-icon" '
        f'width="18" height="18" loading="lazy"></a>'
        for u, n, i, t in socials)
    return f"""    <footer class="site-footer">
        <div class="container">
            <div class="social-links">
{icons}
            </div>
            <p class="footer-text">&copy; {YEAR} {C.NAME}. All rights reserved.</p>
        </div>
    </footer>"""


def authors_html(authors):
    return esc(authors).replace(C.NAME, f"<strong>{C.NAME}</strong>")


def pub_html(pub, depth, *, show_type=True, show_project=True, attrs=""):
    p = "../" * depth
    tags = []
    if show_type:
        tags.append(f'<span class="chip is-neutral">{C.PUB_TYPES[pub["type"]]}</span>')
    if pub.get("award"):
        tags.append(f'<span class="badge">{esc(pub["award"])}</span>')
    tag_row = f'\n                <div class="pub-tags">{"".join(tags)}</div>' if tags else ""
    links = "".join(
        f'<a class="pub-link" href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a>' for n, u in pub["links"])
    proj = ""
    if show_project and pub.get("project"):
        pr = PROJECTS[pub["project"]]
        href = f"{p}projects/{pr['slug']}.html" if depth == 0 else f"{pr['slug']}.html"
        proj = f'<a class="pub-project" href="{href}">Project: {pr["short"]} →</a>'
    return f"""            <article class="pub"{attrs}>{tag_row}
                <h3 class="pub-title">{esc(pub["title"])}</h3>
                <p class="pub-authors">{authors_html(pub["authors"])}</p>
                <p class="pub-venue">{esc(pub["venue"])} · {esc(pub["date"])}</p>
                <div class="pub-foot">{links}{proj}</div>
            </article>"""


def card_html(pr, depth, *, fade=True, attrs=""):
    base = "" if depth == 0 else "../"
    href = f"{base}projects/{pr['slug']}.html"
    # card thumbnails are one-up from the page; project pages link with ../ already
    thumb = f"{base}{q(pr['thumb'])}"
    w, h = image_size(pr["thumb"])
    badge = f'<span class="badge">{esc(pr["award"])}</span>' if pr.get("award") else ""
    cover = " is-cover" if pr["fit"] == "cover" else ""
    cls = "project-card fade-in" if fade else "project-card"
    return f"""            <article class="{cls}"{attrs}>
                <a class="card-thumb{cover}" href="{href}" tabindex="-1" aria-hidden="true">
                    <img src="{thumb}" alt="" width="{w}" height="{h}" loading="lazy" decoding="async">{badge}
                </a>
                <div class="card-body">
                    <p class="card-meta">{pr["year"]} · {CATEGORY_LABEL[pr["category"]]}</p>
                    <h3><a href="{href}">{pr["title"]}</a></h3>
                    <p>{pr["summary"]}</p>
                    <span class="card-more">View project →</span>
                </div>
            </article>"""


def tl_item(date_txt, inner):
    return f"""            <div class="timeline-item fade-in">
                <div class="timeline-date">{esc(date_txt)}</div>
                <div class="timeline-body">
{inner}
                </div>
            </div>"""


# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------
def build_home():
    edu = []
    for e in C.EDUCATION:
        lines = [f"<p>{esc(l)}</p>" for l in e["lines"]]
        if e.get("gpa"):
            lines.append(f"<p><strong>GPA:</strong> {esc(e['gpa'])}</p>")
        if e.get("extra"):
            lines.append(f"<p><em>{esc(e['extra'])}</em></p>")
        courses = ""
        if e["courses"]:
            lis = "".join(f"<li><strong>{esc(g)}</strong> — {esc(t)}</li>" for g, t in e["courses"])
            courses = f'\n                    <details class="coursework"><summary>Relevant coursework</summary><ul>{lis}</ul></details>'
        inner = (f'                    <h3>{esc(e["org"])}</h3>\n                    <span class="timeline-sub">{esc(e["role"])}</span>\n'
                 f'                    {"".join(lines)}{courses}')
        edu.append(tl_item(e["date"], inner))

    exp = []
    for e in C.EXPERIENCE:
        parts = [f'                    <h3>{esc(e["title"])}</h3>',
                 f'                    <span class="timeline-sub">{esc(e["org"])}</span>']
        if e.get("advisor"):
            parts.append(f'                    <p class="aside">{esc(e["advisor"])}</p>')
        parts += [f"                    <p>{esc(t)}</p>" for t in e["paras"]]
        if e["bullets"]:
            parts.append("                    <ul>" + "".join(f"<li>{esc(b)}</li>" for b in e["bullets"]) + "</ul>")
        exp.append(tl_item(e["date"], "\n".join(parts)))

    awards = []
    for d, title, sub, extra in C.AWARDS:
        parts = [f"                    <h3>{esc(title)}</h3>", f'                    <span class="timeline-sub">{esc(sub)}</span>']
        if extra:
            parts.append(f'                    <p lang="{"zh-TW" if "書卷獎" in extra else "en"}">{esc(extra)}</p>')
        awards.append(tl_item(d, "\n".join(parts)))

    focus = "\n".join(
        f"                <li><span>{n}</span><strong>{t}</strong><p>{d}</p></li>" for n, t, d in C.FOCUS)
    n_featured = sum(1 for pr in C.PROJECTS if pr["featured"])
    featured = "\n".join(card_html(pr, 0) for pr in C.PROJECTS if pr["featured"])
    selected = "\n".join(pub_html(pb, 0, show_type=False) .replace('class="pub"', 'class="pub fade-in"', 1)
                         for pb in C.PUBLICATIONS if pb["selected"])
    contacts = [
        ("mailto:" + C.EMAIL, "email_white_44dp.png", "Email", C.EMAIL, ""),
        (C.LINKEDIN, "linkedin_white_44dp.png", "LinkedIn", "Shyandram", ' target="_blank" rel="noopener"'),
        (C.GITHUB, "github_white_44dp.png", "GitHub", "Shyandram", ' target="_blank" rel="noopener"'),
        (C.BLOG, "blog_white.svg", "Blog", "blog.shyandram.dev", ' target="_blank" rel="noopener"'),
        (C.MEDIUM, "medium_white_44dp.png", "Medium", "@shyangen104", ' target="_blank" rel="noopener"'),
        (C.SCHOLAR, "google_scholar_icon.png", "Scholar", "Google Scholar Profile", ' target="_blank" rel="noopener"'),
    ]
    contact_html = "\n".join(
        f'            <a href="{u}"{t} class="contact-card fade-in"><img src="images/icons/{i}" alt="" class="contact-icon" '
        f'width="24" height="24" loading="lazy"><h3>{n}</h3><p>{v}</p></a>' for u, i, n, v, t in contacts)

    jsonld = json.dumps({
        "@context": "https://schema.org", "@type": "Person", "name": C.NAME, "alternateName": C.NAME_ZH,
        "url": C.SITE_URL, "image": C.SITE_URL + "images/selfie.jpg",
        "jobTitle": "PhD candidate, Computer Vision",
        "affiliation": {"@type": "CollegeOrUniversity", "name": "National Yang Ming Chiao Tung University"},
        "sameAs": [C.GITHUB, C.LINKEDIN, C.BLOG, C.MEDIUM, C.SCHOLAR],
    }, ensure_ascii=False)

    body = f"""    <main id="main">
        <header class="hero">
            <div class="container hero-content">
                <div class="hero-text fade-in">
                    <p class="eyebrow">PhD candidate · Computer vision · Taiwan</p>
                    <h1>{C.NAME}</h1>
                    <p class="hero-lead"><span lang="zh-TW">{C.NAME_ZH}</span> (Shyang) — I build practical vision systems for images that are difficult to see, understand, or use.</p>
                    <div class="btn-row">
                        <a href="#research" class="btn btn-outline">Explore the work</a>
                        <a href="#contact" class="btn">Get in touch</a>
                    </div>
                    <p class="hero-note">Image restoration · Low-light enhancement · Object detection</p>
                </div>
                <div class="hero-photo fade-in">
                    <img src="images/selfie-560.webp" srcset="images/selfie-280.webp 280w, images/selfie-560.webp 560w" sizes="(max-width: 860px) 112px, 280px" alt="Portrait of {C.NAME}" class="profile-pic" width="560" height="560" fetchpriority="high" decoding="async">
                </div>
            </div>
        </header>

        <section id="about" class="section">
            <div class="container">
                <h2 class="section-title fade-in">About</h2>
                <div class="about-grid">
                    <p class="about-copy fade-in">{esc(C.ABOUT)}</p>
                    <ul class="focus-list fade-in">
{focus}
                    </ul>
                </div>
            </div>
        </section>

        <section id="education" class="section">
            <div class="container">
                <h2 class="section-title fade-in">Education</h2>
                <div class="timeline">
{chr(10).join(edu)}
                </div>
            </div>
        </section>

        <section id="experience" class="section">
            <div class="container">
                <h2 class="section-title fade-in">Experience</h2>
                <div class="timeline">
{chr(10).join(exp)}
                </div>
            </div>
        </section>

        <section id="research" class="section">
            <div class="container">
                <div class="section-head fade-in">
                    <h2 class="section-title">Research highlights</h2>
                    <div class="section-actions">
                        <a href="research.html" class="btn btn-outline">Full portfolio</a>
                        <a href="{C.SCHOLAR}" class="text-link" target="_blank" rel="noopener">Google Scholar</a>
                    </div>
                </div>
                <div class="card-grid is-compact{' is-3' if n_featured == 3 else ''}">
{featured}
                </div>

                <div class="subsection-head is-tight fade-in" id="publications"><p class="eyebrow">Selected writing</p><h3>Publications</h3></div>
                <div class="pub-grid is-compact">
{selected}
                </div>
                <div class="btn-row" style="justify-content:center;margin-top:2.5rem"><a href="research.html#publications" class="btn fade-in">All publications</a></div>
            </div>
        </section>

        <section id="awards" class="section">
            <div class="container">
                <h2 class="section-title fade-in">Honors &amp; Awards</h2>
                <div class="timeline">
{chr(10).join(awards)}
                </div>
            </div>
        </section>

        <section id="contact" class="section">
            <div class="container">
                <h2 class="section-title fade-in">Get in touch</h2>
                <div class="contact-grid">
{contact_html}
                </div>
                <div class="contact-actions">
                    <a href="{C.CV_URL}" class="btn btn-outline fade-in" target="_blank" rel="noopener">Download CV</a>
                    <a href="{C.SLIDES_URL}" class="btn btn-outline fade-in" target="_blank" rel="noopener">Research slides</a>
                </div>
            </div>
        </section>
    </main>"""
    return page(
        title=f"{C.NAME} | Computer Vision Researcher", desc="Personal website of Shyang-En Weng, Computer Vision and Deep Learning Researcher.",
        path="", depth=0, body=body, nav_active="home",
        extra_head=f'\n    <link rel="preload" as="image" href="images/IMG_4067-800.webp" media="(max-width: 899px)" fetchpriority="high">\n    <link rel="preload" as="image" href="images/IMG_4067.webp" media="(min-width: 900px)" fetchpriority="high">\n    <script type="application/ld+json">{jsonld}</script>')


# ---------------------------------------------------------------------------
# Research page
# ---------------------------------------------------------------------------
def build_research():
    n_proj, n_pub = len(C.PROJECTS), len(C.PUBLICATIONS)
    n_awards = sum(1 for pr in C.PROJECTS if pr.get("award"))
    cards = "\n".join(
        card_html(pr, 0, attrs=f' data-category="{pr["category"]}"') for pr in C.PROJECTS)
    cat_buttons = "".join(
        f'<button type="button" class="filter" data-filter="{k}" aria-pressed="{str(k == "all").lower()}">{v}</button>'
        for k, v in C.CATEGORIES)

    years = sorted({pb["year"] for pb in C.PUBLICATIONS}, reverse=True)
    groups = []
    for y in years:
        items = "\n".join(
            pub_html(pb, 0, attrs=f' data-type="{pb["type"]}"') for pb in C.PUBLICATIONS if pb["year"] == y)
        groups.append(f"""        <div class="year-group" data-group>
            <h3>{y}</h3>
            <div>
{items}
            </div>
        </div>""")
    type_buttons = '<button type="button" class="filter" data-filter="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" class="filter" data-filter="{k}" aria-pressed="false">{v}</button>'
        for k, v in C.PUB_TYPES.items())

    body = f"""    <main id="main">
        <header class="page-head">
            <div class="container">
                <p class="eyebrow">Research</p>
                <h1>Research &amp; publications</h1>
                <p class="page-lead">Image restoration, low-light enhancement, super-resolution and object detection — from lightweight models for edge devices to diffusion-based restoration.</p>
                <div class="btn-row">
                    <a href="{C.SCHOLAR}" class="btn" target="_blank" rel="noopener">Google Scholar</a>
                    <a href="{C.GITHUB}" class="btn btn-outline" target="_blank" rel="noopener">GitHub</a>
                </div>
                <div class="stat-row">
                    <div class="stat"><strong>{n_proj}</strong><span>Projects</span></div>
                    <div class="stat"><strong>{n_pub}</strong><span>Publications &amp; preprints</span></div>
                    <div class="stat"><strong>{n_awards}</strong><span>Award-winning projects</span></div>
                </div>
                <div class="callout">
                    <div>
                        <p class="eyebrow">Currently</p>
                        <p>Diffusion models for real-world super-resolution at NYCU's ACM Lab.</p>
                    </div>
                    <div class="btn-row">
                        <a class="pub-link" href="https://arxiv.org/abs/2604.24136" target="_blank" rel="noopener">arXiv:2604.24136</a>
                        <a class="pub-link" href="https://arxiv.org/abs/2512.10340" target="_blank" rel="noopener">arXiv:2512.10340</a>
                    </div>
                </div>
            </div>
        </header>

        <div class="toolbar">
            <div class="container">
                <nav class="tabs" aria-label="Sections" data-spy>
                    <a href="#projects">Projects</a>
                    <a href="#publications">Publications</a>
                </nav>
            </div>
        </div>

        <section id="projects" class="section">
            <div class="container">
                <div class="section-head">
                    <h2 class="section-title">Projects</h2>
                    <span class="muted" data-count role="status" aria-live="polite"></span>
                </div>
                <div class="filters" role="group" aria-label="Filter projects" data-filter-group="category" data-target="project-list">{cat_buttons}</div>
                <div class="card-grid is-3" id="project-list">
{cards}
                </div>
            </div>
        </section>

        <section id="publications" class="section">
            <div class="container">
                <div class="section-head">
                    <h2 class="section-title">Publications</h2>
                    <span class="muted" data-count role="status" aria-live="polite"></span>
                </div>
                <div class="filters" role="group" aria-label="Filter publications" data-filter-group="type" data-target="pub-list">{type_buttons}</div>
                <div id="pub-list">
{chr(10).join(groups)}
                </div>
            </div>
        </section>
    </main>"""
    return page(
        title=f"Research & Publications | {C.NAME}".replace("&", "&amp;"),
        desc="Research portfolio and publications of Shyang-En Weng: image restoration, low-light enhancement, super-resolution and object detection.",
        path="research.html", depth=0, body=body, nav_active="research")


# ---------------------------------------------------------------------------
# Project pages
# ---------------------------------------------------------------------------
def figure_html(src, alt):
    w, h = image_size(src)
    return f"""                <figure class="figure">
                    <button type="button" class="figure-frame" data-zoom aria-label="Enlarge figure: {esc(alt)}">
                        <img src="../{q(src)}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async">
                    </button>
                    <figcaption>{esc(alt)}</figcaption>
                </figure>"""


def build_project(i, pr):
    prev_pr = C.PROJECTS[i - 1] if i > 0 else None
    next_pr = C.PROJECTS[i + 1] if i < len(C.PROJECTS) - 1 else None

    sections = []
    for s in pr["sections"]:
        figs = "\n".join(figure_html(src, alt) for src, alt in s.get("figures", []))
        figs = figs + "\n" if figs else ""
        # figures first inside overview; elsewhere text then figure reads naturally, so put figure first too
        sections.append(f"""                <section id="{s["id"]}">
                    <h2>{s["title"]}</h2>
{figs}{s["html"].strip()}
                </section>""")
    pubs = [pb for pb in C.PUBLICATIONS if pb.get("project") == pr["slug"]]
    if pubs:
        pub_items = "\n".join(pub_html(pb, 1, show_project=False) for pb in pubs)
        sections.append(f"""                <section id="publications">
                    <h2>Related publications</h2>
{pub_items}
                </section>""")

    toc_items = [(s["id"], s["title"]) for s in pr["sections"]] + ([("publications", "Related publications")] if pubs else [])
    toc = "\n".join(f'                        <a href="#{i}">{t}</a>' for i, t in toc_items)

    facts = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in pr["facts"])
    kws = "".join(f'<span class="chip is-neutral">{esc(k)}</span>' for k in pr["keywords"])
    chips = "".join(f'<span class="chip">{esc(c)}</span>' for c in pr["chips"])
    btns = "".join(
        f'<a href="{esc(u)}" class="btn{" btn-outline" if n else ""}" target="_blank" rel="noopener">{esc(l)}</a>'
        for n, (l, u) in enumerate(pr["links"]))
    btn_row = f'\n                <div class="btn-row">{btns}</div>' if btns else ""
    award = f' <span class="badge" style="margin-left:.6rem">{esc(pr["award"])}</span>' if pr.get("award") else ""

    pager = []
    if prev_pr:
        pager.append(f'<a class="prev" href="{prev_pr["slug"]}.html"><small>← Previous</small><span>{prev_pr["title"]}</span></a>')
    if next_pr:
        pager.append(f'<a class="next" href="{next_pr["slug"]}.html"><small>Next →</small><span>{next_pr["title"]}</span></a>')

    body = f"""    <main id="main">
        <header class="page-head">
            <div class="container">
                <nav class="breadcrumb" aria-label="Breadcrumb"><a href="../research.html">Research</a><span aria-hidden="true">/</span><span aria-current="page">{pr["short"]}</span></nav>
                <p class="eyebrow">{pr["year"]} · {CATEGORY_LABEL[pr["category"]]}{award}</p>
                <h1>{pr["title"]}</h1>
                <p class="subtitle" lang="zh-TW">{pr["title_zh"]}</p>
                <div class="chips">{chips}</div>{btn_row}
            </div>
        </header>

        <div class="container project-layout">
            <article class="prose">
{chr(10).join(sections)}
                <nav class="pager" aria-label="More projects">{"".join(pager)}</nav>
            </article>

            <aside class="project-aside">
                <div class="aside-block">
                    <h2>At a glance</h2>
                    <dl class="facts">{facts}</dl>
                </div>
                <div class="aside-block toc-block">
                    <h2>On this page</h2>
                    <nav class="toc" aria-label="On this page" data-spy>
{toc}
                    </nav>
                </div>
                <div class="aside-block">
                    <h2>Keywords</h2>
                    <div class="chips">{kws}</div>
                </div>
            </aside>
        </div>
    </main>

    <dialog id="lightbox" class="lightbox" aria-label="Enlarged figure">
        <div class="lightbox-inner"><img src="" alt=""></div>
    </dialog>"""
    plain_title = pr["title"].replace("&amp;", "&")
    return page(
        title=f"{pr['title']} | {C.NAME}",
        desc=f"{plain_title} — {pr['summary']}",
        path=f"projects/{pr['slug']}.html", depth=1, body=body, nav_active="research")


# ---------------------------------------------------------------------------
# 404, sitemap, robots
# ---------------------------------------------------------------------------
def build_404():
    body = """    <main id="main">
        <div class="container" style="padding: 12rem var(--gutter) 6rem;">
            <p class="eyebrow">404</p>
            <h1 style="font-size: clamp(2.4rem, 6vw, 4rem); margin: 1rem 0;">Page not found</h1>
            <p class="muted" style="margin-bottom: 2rem;">The page you're looking for doesn't exist or has moved.</p>
            <a href="/" class="btn">Back to home</a>
        </div>
    </main>"""
    out = page(title=f"Page not found | {C.NAME}", desc="Page not found.", path="404.html", depth=0, body=body,
               prefix="/")   # may be served from any URL, so assets are root-relative
    return out.replace('<meta name="theme-color"', '<meta name="robots" content="noindex">\n    <meta name="theme-color"')


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote", rel)


def main():
    write("index.html", build_home())
    write("research.html", build_research())
    write("404.html", build_404())
    for i, pr in enumerate(C.PROJECTS):
        write(f"projects/{pr['slug']}.html", build_project(i, pr))
    urls = [""] + ["research.html"] + [f"projects/{p['slug']}.html" for p in C.PROJECTS]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{C.SITE_URL}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {C.SITE_URL}sitemap.xml\n")


if __name__ == "__main__":
    main()
