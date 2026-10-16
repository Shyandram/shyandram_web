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
            const href = this.getAttribute('href');
            if (href.length < 2) return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // "Back" on project pages: go back only when the visitor came from this site,
    // otherwise follow the link's own href (direct visits, search results).
    document.querySelectorAll('a[data-back]').forEach(link => {
        link.addEventListener('click', (e) => {
            let cameFromSite = false;
            try {
                cameFromSite = document.referrer !== '' && new URL(document.referrer).origin === location.origin;
            } catch (err) { /* malformed referrer: fall through to href */ }
            if (cameFromSite && history.length > 1) {
                e.preventDefault();
                history.back();
            }
        });
    });

    // Set current year in footer (if element exists)
    const footerText = document.querySelector('.footer-text');
    if (footerText) {
        footerText.innerHTML = footerText.innerHTML.replace(/(©|&copy;)(\s*)\d{4}/, `$1$2${new Date().getFullYear()}`);
    }

    const nav = document.querySelector('nav');
    const backToTopBtn = document.getElementById('backToTop');

    // Research page: floating switcher and the in-page sub-nav share the same scroll spy
    const floatingSwitcher = document.querySelector('.floating-switcher');
    const fabProjects = document.getElementById('fab-projects');
    const fabPubs = document.getElementById('fab-publications');
    const publicationsSection = document.getElementById('publications');
    const subNavLinks = [...document.querySelectorAll('.sub-nav-link')];

    // One passive, rAF-throttled scroll handler instead of several unthrottled ones
    let ticking = false;
    const onScroll = () => {
        const y = window.scrollY;

        if (nav) nav.classList.toggle('scrolled', y > 50);
        if (backToTopBtn) backToTopBtn.classList.toggle('visible', y > 300);

        if (floatingSwitcher && publicationsSection) {
            floatingSwitcher.classList.toggle('visible', y > 300);

            const inPubs = y >= publicationsSection.offsetTop - 100;
            if (fabPubs) fabPubs.classList.toggle('active', inPubs);
            if (fabProjects) fabProjects.classList.toggle('active', !inPubs);
            subNavLinks.forEach(link => {
                link.classList.toggle('active', (link.getAttribute('href') === '#publications') === inPubs);
            });
        }
        ticking = false;
    };

    window.addEventListener('scroll', () => {
        if (!ticking) {
            ticking = true;
            requestAnimationFrame(onScroll);
        }
    }, { passive: true });
    onScroll();

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
            const targetSection = document.querySelector(this.getAttribute('href'));

            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop - 100, // Offset for fixed header/nav
                    behavior: 'smooth'
                });
            }
        });
    });
});
