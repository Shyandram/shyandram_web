# Shyang-En Weng — personal site

Live: https://shyandram.dev/

Static site served by GitHub Pages straight from the repository root.
The HTML pages are **generated** from a single content file, so edit the source, not the HTML:

| What | Where |
|---|---|
| Profile, education, experience, awards, projects, publications | `tools/content.py` |
| Page templates and shared nav/footer | `tools/build.py` |
| Styles / behaviour | `style.css`, `script.js` |

```bash
python3 tools/build.py   # regenerates index.html, research.html, 404.html, projects/*.html, sitemap.xml, robots.txt
```

The build uses only the Python standard library. Asset URLs get a content hash (`style.css?v=…`), so there is
no manual cache-busting. Commit the regenerated HTML together with the content change.

Images are WebP (`images/**.webp`); the original PNG/JPG files are kept next to them as source/OG images.

The font is self-hosted: Geist (`fonts/geist-latin.woff2`, latin subset, SIL Open Font License). Responsive image
variants (`IMG_4067-800.webp`, `selfie-280/560.webp`, `icons/icon-48/180.png`) are generated assets; originals
(`IMG_4067.JPEG`, `selfie.jpg`, `icons/icon.jpg`) are kept as sources.

No ads, no third-party fonts or scripts. The only third-party request is Google Analytics (GA4, ID in
`tools/build.py`), loaded after the page has finished loading so it does not slow first paint.

The ORCID iD icon (`images/icons/orcid.svg`) is ORCID's official, unmodified icon (from orcid.org); it is shown only to
link to the owner's own ORCID record, per ORCID's iD display guidelines.
