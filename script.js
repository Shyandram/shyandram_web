/* Progressive enhancement only: every page is fully readable and navigable without this file. */
document.addEventListener('DOMContentLoaded', () => {
    const $ = (sel, root = document) => root.querySelector(sel);
    const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

    // ---- Scroll reveal ----
    const reveal = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('visible');
            reveal.unobserve(entry.target);
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    $$('.fade-in').forEach(el => reveal.observe(el));

    // ---- Scroll spy: marks the link whose in-page target is currently in view ----
    // Used by the main nav (home), the research tabs and the project table of contents.
    const spy = (links) => {
        const pairs = links
            .map(link => [link, document.getElementById((link.getAttribute('href').split('#')[1] || ''))])
            .filter(([, target]) => target);
        if (!pairs.length) return;
        const visible = new Set();
        const io = new IntersectionObserver((entries) => {
            entries.forEach(e => (e.isIntersecting ? visible.add(e.target) : visible.delete(e.target)));
            // the first target (document order) that is in the reading band wins
            const current = pairs.find(([, target]) => visible.has(target));
            pairs.forEach(([link, target]) => {
                if (current && current[1] === target) link.setAttribute('aria-current', 'true');
                else link.removeAttribute('aria-current');
            });
        }, { rootMargin: '-25% 0px -60% 0px', threshold: 0 });
        pairs.forEach(([, target]) => io.observe(target));
    };
    spy($$('.nav-links a[href^="#"]'));
    spy($$('[data-spy] a[href^="#"]'));

    // ---- Header: scrolled state, mobile menu, back-to-top (single passive, rAF-throttled handler) ----
    const nav = $('.site-nav');
    const toggle = $('.nav-toggle');
    const menu = $('.nav-links');
    const topBtn = $('#backToTop');

    let ticking = false;
    const onScroll = () => {
        const y = window.scrollY;
        if (nav) nav.classList.toggle('scrolled', y > 24);
        if (topBtn) topBtn.classList.toggle('visible', y > 400);
        ticking = false;
    };
    window.addEventListener('scroll', () => {
        if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
    }, { passive: true });
    onScroll();

    if (topBtn) topBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

    if (toggle && menu) {
        const setOpen = (open) => {
            menu.classList.toggle('is-open', open);
            toggle.setAttribute('aria-expanded', String(open));
        };
        toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
        menu.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setOpen(false); });
    }

    // ---- Filters (research page): buttons with data-filter control items with data-<attr> ----
    $$('[data-filter-group]').forEach(group => {
        const attr = group.dataset.filterGroup;               // e.g. "category" or "type"
        const scope = document.getElementById(group.dataset.target);
        if (!scope) return;
        const items = $$(`[data-${attr}]`, scope);
        const buttons = $$('.filter', group);
        const counter = $('[data-count]', scope.parentElement || document);

        const apply = (value) => {
            buttons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.filter === value)));
            let shown = 0;
            items.forEach(item => {
                const match = value === 'all' || item.dataset[attr] === value;
                item.hidden = !match;
                if (match) shown++;
            });
            // hide year groups / sections that have nothing left to show
            $$('[data-group]', scope).forEach(g => { g.hidden = !$$(`[data-${attr}]`, g).some(i => !i.hidden); });
            if (counter) counter.textContent = `${shown} shown`;
        };
        buttons.forEach(b => b.addEventListener('click', () => apply(b.dataset.filter)));
        apply('all');
    });

    // ---- Figure lightbox ----
    const dialog = $('#lightbox');
    if (dialog && typeof dialog.showModal === 'function') {
        const big = $('img', dialog);
        $$('[data-zoom]').forEach(btn => {
            btn.addEventListener('click', () => {
                const img = $('img', btn);
                big.src = img.currentSrc || img.src;
                big.alt = img.alt;
                dialog.showModal();
            });
        });
        dialog.addEventListener('click', () => dialog.close());
    }
});
