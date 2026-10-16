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

Manrope is self-hosted (`fonts/manrope-latin.woff2`, latin subset, SIL Open Font License). Responsive image
variants (`IMG_4067-800.webp`, `selfie-280/560.webp`, `icons/icon-48/180.png`) are generated assets; originals
(`IMG_4067.JPEG`, `selfie.jpg`, `icons/icon.jpg`) are kept as sources.
