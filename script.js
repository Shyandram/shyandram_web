document.addEventListener('DOMContentLoaded', () => {

    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Once it's visible, we don't need to observe it anymore
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Track all elements with .fade-in class
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach(el => observer.observe(el));

    // OpenAlex provides a public, CORS-friendly citation index for static sites.
    // Google Scholar itself does not expose a stable public API for browser sync.
    const citationItems = [...document.querySelectorAll('.pub-item')];
    const citationCache = new Map();
    const citationEndpoint = (item) => {
        const title = item.querySelector('.pub-title')?.textContent.trim();
        const link = item.querySelector('.pub-doi[href]');
        if (!title) return null;
        if (link) {
            try {
                const url = new URL(link.href);
                if (url.hostname.includes('doi.org')) {
                    return `https://api.openalex.org/works/https://doi.org/${encodeURIComponent(url.pathname.slice(1))}`;
                }
                if (url.hostname.includes('arxiv.org')) {
                    return `https://api.openalex.org/works/https://arxiv.org/abs/${url.pathname.split('/').pop()}`;
                }
            } catch (error) {
                return null;
            }
        }
        return `https://api.openalex.org/works?search=${encodeURIComponent(title)}&per-page=1`;
    };

    const syncCitationCount = async (item) => {
        const endpoint = citationEndpoint(item);
        if (!endpoint) return;
        const citation = document.createElement('span');
        citation.className = 'citation-count';
        citation.textContent = 'Citations syncing…';
        citation.setAttribute('aria-live', 'polite');
        item.append(citation);

        try {
            let work = citationCache.get(endpoint);
            if (!work) {
                const response = await fetch(endpoint, { headers: { Accept: 'application/json' } });
                if (!response.ok) throw new Error('Citation request failed');
                const payload = await response.json();
                work = payload.results?.[0] || payload;
                citationCache.set(endpoint, work);
            }
            const count = Number(work.cited_by_count);
            citation.textContent = Number.isFinite(count) ? `Cited by ${count}` : 'Citation data unavailable';
            citation.classList.add('is-ready');
        } catch (error) {
            citation.textContent = 'Citation data unavailable';
        }
    };

    citationItems.forEach(syncCitationCount);

    // Keep the section navigation honest as the reader moves through the page.
    const pageSections = [...document.querySelectorAll('main section, body > section[id]')];
    const sectionLinks = [...document.querySelectorAll('.nav-links a[href^="#"]')];
    if (pageSections.length && sectionLinks.length) {
        const sectionObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (!entry.isIntersecting) return;
                sectionLinks.forEach(link => {
                    link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`);
                });
            });
        }, { rootMargin: '-30% 0px -55% 0px', threshold: 0 });

        pageSections.forEach(section => sectionObserver.observe(section));
    }

    // Smooth scroll for nav links (handled by CSS, but good to have)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Header scroll effect
    const nav = document.querySelector('nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.style.padding = '1rem 0';
        } else {
            nav.style.padding = '1.5rem 0';
        }
    });

    // Set current year in footer (if element exists)
    const footerText = document.querySelector('.footer-text');
    if (footerText) {
        const year = new Date().getFullYear();
        footerText.innerHTML = footerText.innerHTML.replace('2024', year);
    }

    // Back to Top Button Logic
    const backToTopBtn = document.getElementById('backToTop');

    // Floating Switcher Logic
    const floatingSwitcher = document.querySelector('.floating-switcher');
    const fabProjects = document.getElementById('fab-projects');
    const fabPubs = document.getElementById('fab-publications');
    const publicationsSection = document.getElementById('publications');

    window.addEventListener('scroll', () => {
        if (backToTopBtn) {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        }

        if (floatingSwitcher && publicationsSection) {
            // Show switcher after scrolling past header
            if (window.scrollY > 300) {
                floatingSwitcher.classList.add('visible');
            } else {
                floatingSwitcher.classList.remove('visible');
            }

            // Scroll Spy for Active State
            const pubOffset = publicationsSection.offsetTop - 100; // Offset for better triggering

            if (window.scrollY >= pubOffset) {
                fabPubs.classList.add('active');
                fabProjects.classList.remove('active');
            } else {
                fabProjects.classList.add('active');
                fabPubs.classList.remove('active');
            }
        }
    });

    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Smooth scroll for switcher links
    document.querySelectorAll('.switcher-btn').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop - 100, // Offset for fixed header/nav
                    behavior: 'smooth'
                });

                // Manual active state update update
                document.querySelectorAll('.switcher-btn').forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');
            }
        });
    });
});
