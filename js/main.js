/**
 * Abhishek Wood Works - Main Interactive JavaScript
 * Zero runtime dependencies, high performance, full keyboard and touch accessibility.
 */

document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initHeroSlider();
  initGallery();
  initLightbox();
  initEnquiryForm();
});

/* ==========================================================================
   1. Header Sticky & Solid Transition (Zero Backdrop Blur)
   ========================================================================== */
function initHeader() {
  const header = document.getElementById('site-header');
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  const mobileDrawer = document.getElementById('mobile-drawer');
  const menuIconBars = document.getElementById('menu-icon-bars');
  const menuIconClose = document.getElementById('menu-icon-close');

  if (!header) return;

  function handleScroll() {
    if (window.scrollY > 40) {
      // Solid dark walnut background with hairline border (NO backdrop blur)
      header.classList.add('bg-walnut-950', 'text-cream-100', 'hairline-dark-b', 'shadow-md');
      header.classList.remove('bg-transparent');
    } else {
      header.classList.remove('bg-walnut-950', 'hairline-dark-b', 'shadow-md');
      header.classList.add('bg-transparent', 'text-cream-100');
    }
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // Mobile drawer toggle
  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.setAttribute('aria-expanded', !isExpanded);
      
      if (isExpanded) {
        mobileDrawer.classList.add('hidden');
        menuIconBars.classList.remove('hidden');
        menuIconClose.classList.add('hidden');
        document.body.classList.remove('overflow-hidden');
      } else {
        mobileDrawer.classList.remove('hidden');
        menuIconBars.classList.add('hidden');
        menuIconClose.classList.remove('hidden');
        document.body.classList.add('overflow-hidden');
      }
    });

    // Close mobile drawer on link click
    mobileDrawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileDrawer.classList.add('hidden');
        mobileToggle.setAttribute('aria-expanded', 'false');
        menuIconBars.classList.remove('hidden');
        menuIconClose.classList.add('hidden');
        document.body.classList.remove('overflow-hidden');
      });
    });
  }
}

/* ==========================================================================
   Hero Slider (Warm Natural Full-Bleed Crossfade, Subtle Zoom & Accessible Controls)
   ========================================================================== */
function initHeroSlider() {
  const hero = document.getElementById('hero');
  const slides = Array.from(document.querySelectorAll('#hero-slider-container .hero-slide'));
  const dots = Array.from(document.querySelectorAll('#hero-dots .hero-dot'));
  const captionBtn = document.getElementById('hero-caption-btn');
  const captionText = document.getElementById('hero-caption-text');
  const counterText = document.getElementById('hero-counter-text');

  if (!hero || slides.length === 0) return;

  let currentIndex = 0;
  let timer = null;
  let isPaused = false;
  let touchResumeTimeout = null;
  const ROTATE_INTERVAL = 6000;

  function updateSlide(index) {
    currentIndex = (index + slides.length) % slides.length;

    // Update slides
    slides.forEach((slide, i) => {
      const isActive = i === currentIndex;
      if (isActive) {
        slide.classList.add('active');
        slide.setAttribute('aria-hidden', 'false');
      } else {
        slide.classList.remove('active');
        slide.setAttribute('aria-hidden', 'true');
      }
    });

    // Update desktop indicator dots
    dots.forEach((dot, i) => {
      const isActive = i === currentIndex;
      if (isActive) {
        dot.className = 'hero-dot w-2 h-7 bg-amber-accent rounded-full transition-all duration-300';
        dot.setAttribute('aria-current', 'true');
      } else {
        dot.className = 'hero-dot w-2 h-2 bg-cream-100/40 hover:bg-cream-100/80 rounded-full transition-all duration-300';
        dot.removeAttribute('aria-current');
      }
    });

    // Update caption and counter
    const activeSlide = slides[currentIndex];
    const caption = activeSlide ? activeSlide.getAttribute('data-caption') : '';
    if (captionText && caption) {
      captionText.textContent = caption;
    }
    if (counterText) {
      counterText.textContent = `${currentIndex + 1} / ${slides.length}`;
    }
  }

  function startRotation() {
    stopRotation();
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      return; // Respect prefers-reduced-motion: static single photo
    }
    timer = setInterval(() => {
      if (!isPaused) {
        updateSlide(currentIndex + 1);
      }
    }, ROTATE_INTERVAL);
  }

  function stopRotation() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  function resetRotation() {
    stopRotation();
    if (!isPaused) {
      startRotation();
    }
  }

  // Pause on hover
  hero.addEventListener('mouseenter', () => {
    isPaused = true;
  });
  hero.addEventListener('mouseleave', () => {
    isPaused = false;
    resetRotation();
  });

  // Pause on tap/touch
  hero.addEventListener('touchstart', () => {
    isPaused = true;
    if (touchResumeTimeout) {
      clearTimeout(touchResumeTimeout);
      touchResumeTimeout = null;
    }
  }, { passive: true });

  hero.addEventListener('touchend', () => {
    touchResumeTimeout = setTimeout(() => {
      isPaused = false;
      resetRotation();
    }, 4000);
  }, { passive: true });

  // Listen for reduced motion changes
  if (window.matchMedia) {
    const reducedMotionMedia = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (reducedMotionMedia.addEventListener) {
      reducedMotionMedia.addEventListener('change', (e) => {
        if (e.matches) {
          stopRotation();
        } else {
          startRotation();
        }
      });
    }
  }

  // Indicator dots click
  dots.forEach((dot, i) => {
    dot.addEventListener('click', (e) => {
      e.preventDefault();
      updateSlide(i);
      resetRotation();
    });
  });

  // Bottom right caption button: tapping scrolls to that category in the gallery
  if (captionBtn) {
    captionBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const activeSlide = slides[currentIndex];
      const category = activeSlide ? activeSlide.getAttribute('data-category') : null;

      if (category) {
        if (typeof window.setGalleryCategory === 'function') {
          window.setGalleryCategory(category, true);
        } else {
          const tabBtn = document.querySelector(`.category-tab-btn[data-cat="${category}"]`);
          if (tabBtn) tabBtn.click();
        }
      }

      const workSection = document.getElementById('work');
      if (workSection) {
        workSection.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  // Initialize
  updateSlide(0);
  startRotation();
}

/* ==========================================================================
   2. Gallery & Filter System (Refined Catalogue Grid & Dynamic Sidebar)
   ========================================================================== */
let activeCategory = 'Wardrobes';
let activeDensity = 'comfortable';
let currentFilteredItems = [];

function getCatSlug(id) {
  const catObj = (window.SITE_CONFIG?.categories || []).find(c => c.id === id);
  if (catObj && catObj.slug) return catObj.slug;
  if (!id) return 'wardrobes';
  return id.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

function findCatBySlug(slug, categories) {
  if (!slug) return 'Wardrobes';
  const clean = slug.toLowerCase().replace('#', '').trim();
  if (!clean || clean === 'all' || clean === 'work') return 'Wardrobes';
  const match = categories.find(c => 
    c.slug === clean || 
    c.shortLabel.toLowerCase() === clean || 
    c.id.toLowerCase() === clean || 
    getCatSlug(c.id) === clean
  );
  return match ? match.id : null;
}

function initGallery() {
  const desktopCatList = document.getElementById('desktop-category-list');
  const densityComfortableBtn = document.getElementById('density-comfortable-btn');
  const densityCompactBtn = document.getElementById('density-compact-btn');
  const categoryTabsContainer = document.getElementById('gallery-category-tabs');
  const galleryGrid = document.getElementById('gallery-grid');
  const galleryCountText = document.getElementById('gallery-count-text');
  const galleryActiveTitle = document.getElementById('gallery-active-title');
  const galleryEmptyState = document.getElementById('gallery-empty-state');
  const resetFilterBtn = document.getElementById('reset-filter-btn');

  if (!galleryGrid || !window.GALLERY_ITEMS) return;

  const categories = window.SITE_CONFIG ? window.SITE_CONFIG.categories : [
    { id: "Sofas & Seating", label: "Sofas & Seating", shortLabel: "Sofas", slug: "sofas" },
    { id: "Dining", label: "Dining", shortLabel: "Dining", slug: "dining" },
    { id: "Wardrobes", label: "Wardrobes", shortLabel: "Wardrobes", slug: "wardrobes" },
    { id: "Kitchens", label: "Kitchens", shortLabel: "Kitchens", slug: "kitchens" },
    { id: "Doors & Windows", label: "Doors & Windows", shortLabel: "Doors", slug: "doors" },
    { id: "TV Units & Partitions", label: "TV Units & Partitions", shortLabel: "TV Units", slug: "tv-units" },
    { id: "Beds & Bedroom", label: "Beds & Bedroom", shortLabel: "Beds", slug: "beds" }
  ];

  // Render Centered Wrapping Tabs (Mobile 2 rows, Tablet/Desktop 1 row)
  function renderCategoryTabs() {
    if (!categoryTabsContainer) return;
    categoryTabsContainer.innerHTML = categories.map(cat => {
      const isActive = cat.id === activeCategory;
      return `
        <button
          type="button"
          data-cat="${cat.id}"
          class="category-tab-btn min-h-[44px] px-1.5 sm:px-2.5 flex items-center justify-center font-serif text-sm sm:text-base tracking-wide border-b-2 transition-colors ${
            isActive
              ? 'border-amber-accent text-walnut-950 font-semibold'
              : 'border-transparent text-walnut-800/70 hover:text-walnut-950 font-normal'
          }"
          aria-current="${isActive ? 'true' : 'false'}"
        >
          ${cat.shortLabel || cat.label}
        </button>
      `;
    }).join('');

    categoryTabsContainer.querySelectorAll('.category-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const catId = btn.getAttribute('data-cat');
        setCategory(catId, true);
      });
    });
  }

  // Render Desktop Sidebar Categories (Serif type, quiet count, thin amber line on active)
  function renderDesktopCategories() {
    if (!desktopCatList) return;
    desktopCatList.innerHTML = categories.map(cat => {
      const count = window.GALLERY_ITEMS.filter(i => i.category === cat.id).length;
      const isActive = cat.id === activeCategory;
      return `
        <li>
          <button
            type="button"
            data-cat="${cat.id}"
            class="desktop-cat-btn w-full text-left py-2 px-3 flex items-center justify-between font-serif text-base transition-colors ${
              isActive 
                ? 'border-l-2 border-amber-accent font-semibold text-walnut-950 bg-amber-accent/5' 
                : 'border-l-2 border-transparent text-walnut-800/80 hover:text-amber-accent font-normal'
            }"
            aria-current="${isActive ? 'true' : 'false'}"
          >
            <span>${cat.label}</span>
            <span class="text-xs font-mono text-walnut-600/70 ml-2">${count}</span>
          </button>
        </li>
      `;
    }).join('');

    desktopCatList.querySelectorAll('.desktop-cat-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const catId = btn.getAttribute('data-cat');
        setCategory(catId, true);
      });
    });
  }

  // Density Toggle (Comfortable vs Compact)
  function setDensity(density) {
    activeDensity = density;
    if (density === 'comfortable') {
      galleryGrid.classList.remove('density-compact');
      galleryGrid.classList.add('density-comfortable');
      if (densityComfortableBtn) {
        densityComfortableBtn.className = 'font-medium text-walnut-950 underline underline-offset-4 decoration-amber-accent';
      }
      if (densityCompactBtn) {
        densityCompactBtn.className = 'text-walnut-700/60 hover:text-walnut-950 transition-colors no-underline font-normal';
      }
    } else {
      galleryGrid.classList.remove('density-comfortable');
      galleryGrid.classList.add('density-compact');
      if (densityCompactBtn) {
        densityCompactBtn.className = 'font-medium text-walnut-950 underline underline-offset-4 decoration-amber-accent';
      }
      if (densityComfortableBtn) {
        densityComfortableBtn.className = 'text-walnut-700/60 hover:text-walnut-950 transition-colors no-underline font-normal';
      }
    }
  }

  if (densityComfortableBtn) densityComfortableBtn.addEventListener('click', () => setDensity('comfortable'));
  if (densityCompactBtn) densityCompactBtn.addEventListener('click', () => setDensity('compact'));

  // Set Category
  function setCategory(catId, updateUrl = true) {
    activeCategory = catId;
    const activeCatObj = categories.find(c => c.id === catId) || categories[0];

    renderCategoryTabs();
    renderDesktopCategories();

    if (galleryActiveTitle) {
      galleryActiveTitle.textContent = activeCatObj.label;
    }

    if (updateUrl) {
      const slug = getCatSlug(catId);
      history.replaceState(null, '', '#' + slug);
    }

    renderItems();
  }

  // Expose category switching for hero caption button and external deep links
  window.setGalleryCategory = setCategory;

  // Render Masonry Grid Items (Strictly current category items)
  function renderItems() {
    currentFilteredItems = window.GALLERY_ITEMS.filter(item => item.category === activeCategory);
    const count = currentFilteredItems.length;

    if (galleryCountText) {
      galleryCountText.textContent = `${count} piece${count === 1 ? '' : 's'}`;
    }

    if (count === 0) {
      galleryGrid.classList.add('hidden');
      if (galleryEmptyState) galleryEmptyState.classList.remove('hidden');
      return;
    } else {
      galleryGrid.classList.remove('hidden');
      if (galleryEmptyState) galleryEmptyState.classList.add('hidden');
    }

    // Smooth subtle fade reflow
    galleryGrid.style.opacity = '0';
    setTimeout(() => {
      galleryGrid.innerHTML = currentFilteredItems.map((item, index) => {
        return `
          <article class="masonry-item group relative bg-white border border-walnut-950/15 overflow-hidden transition-all duration-300 hover:border-walnut-950/40 hover:shadow-md cursor-pointer"
                   data-item-id="${item.id}"
                   data-index="${index}"
                   tabindex="0"
                   role="button"
                   aria-label="View details for ${item.title}">
            <div class="relative overflow-hidden bg-[#FAF5EC]" style="aspect-ratio: ${item.width} / ${item.height};">
              <img 
                src="${item.src}"
                srcset="${item.srcset}"
                sizes="${item.sizes}"
                alt="${item.title} - Custom woodwork by Abhishek Wood Works"
                width="${item.width}"
                height="${item.height}"
                loading="lazy"
                decoding="async"
                class="w-full h-full object-cover blur-up transition-transform duration-500 ease-out md:group-hover:scale-[1.02]"
                onload="this.classList.add('loaded')"
              />
              <!-- Desktop Hover Label Strip (Slides up from bottom, zero text on mobile) -->
              <div class="hidden md:flex absolute inset-x-0 bottom-0 bg-[#FAF5EC]/95 hairline-t px-3.5 py-2.5 items-center justify-between translate-y-full group-hover:translate-y-0 transition-transform duration-300 ease-out z-10 pointer-events-none">
                <span class="font-serif text-sm text-walnut-950 font-normal truncate mr-2">${item.title}</span>
                <span class="text-[10px] font-mono uppercase tracking-wider text-amber-accent font-semibold shrink-0">View</span>
              </div>
            </div>
          </article>
        `;
      }).join('');

      // Attach click and keyboard events
      galleryGrid.querySelectorAll('.masonry-item').forEach(card => {
        const idx = parseInt(card.getAttribute('data-index'), 10);
        card.addEventListener('click', () => openLightbox(idx, card));
        card.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            openLightbox(idx, card);
          }
        });
      });

      galleryGrid.style.opacity = '1';
    }, 100);
  }

  if (resetFilterBtn) {
    resetFilterBtn.addEventListener('click', () => setCategory('Wardrobes', true));
  }

  // Handle URL hash on initial page load
  const initialHash = window.location.hash.replace('#', '').trim();
  if (initialHash) {
    const pieceMatch = window.GALLERY_ITEMS.find(i => i.id === initialHash);
    if (pieceMatch) {
      activeCategory = pieceMatch.category;
    } else {
      const matchedCat = findCatBySlug(initialHash, categories);
      activeCategory = matchedCat || 'Wardrobes';
    }
  } else {
    activeCategory = 'Wardrobes';
  }

  // Initial renders
  renderCategoryTabs();
  renderDesktopCategories();
  renderItems();

  // If initial hash was a piece ID, open it in lightbox
  if (initialHash && initialHash.startsWith('item-')) {
    setTimeout(() => {
      const itemIdx = currentFilteredItems.findIndex(i => i.id === initialHash);
      if (itemIdx !== -1) openLightbox(itemIdx);
    }, 250);
  }

  // Listen to hash changes for deep links
  window.addEventListener('hashchange', () => {
    const newHash = window.location.hash.replace('#', '').trim();
    if (!newHash) return;
    if (newHash.startsWith('item-')) {
      const itemIdx = currentFilteredItems.findIndex(i => i.id === newHash);
      if (itemIdx !== -1) openLightbox(itemIdx);
      return;
    }
    const cat = findCatBySlug(newHash, categories);
    if (cat && cat !== activeCategory) {
      setCategory(cat, false);
    }
  });
}

/* ==========================================================================
   3. Interaction Panel (Refined Two-Part Lightbox & Mobile Peeking Sheet)
   ========================================================================== */
let activeLightboxIndex = 0;
let lastFocusedTile = null;
let currentZoom = 1;

function initLightbox() {
  const modal = document.getElementById('lightbox-modal');
  const desktopCloseBtn = document.getElementById('lightbox-close');
  const mobileCloseBtn = document.getElementById('lightbox-mobile-close');
  const prevBtn = document.getElementById('lightbox-prev');
  const nextBtn = document.getElementById('lightbox-next');
  const desktopEnquireBtn = document.getElementById('lightbox-enquire-btn');
  const mobileEnquireBtn = document.getElementById('lightbox-mobile-enquire-btn');
  const peekHandle = document.getElementById('mobile-sheet-peek-handle');
  const mobileDetails = document.getElementById('lightbox-mobile-details');

  if (!modal) return;

  // Close handlers
  if (desktopCloseBtn) desktopCloseBtn.addEventListener('click', closeLightbox);
  if (mobileCloseBtn) mobileCloseBtn.addEventListener('click', closeLightbox);
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.id === 'lightbox-backdrop') {
      closeLightbox();
    }
  });

  // Prev / Next button handlers
  if (prevBtn) prevBtn.addEventListener('click', showPrevItem);
  if (nextBtn) nextBtn.addEventListener('click', showNextItem);

  // Keyboard navigation & Focus trap
  modal.addEventListener('keydown', (e) => {
    if (modal.classList.contains('hidden')) return;

    if (e.key === 'Escape') {
      closeLightbox();
      return;
    } else if (e.key === 'ArrowLeft') {
      showPrevItem();
      return;
    } else if (e.key === 'ArrowRight') {
      showNextItem();
      return;
    }

    if (e.key === 'Tab') {
      const focusable = modal.querySelectorAll('button:not([disabled]), [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (!focusable.length) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];

      if (e.shiftKey) {
        if (document.activeElement === first) {
          last.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === last) {
          first.focus();
          e.preventDefault();
        }
      }
    }
  });

  // Mobile Touch Gestures (Swipe down to close, Swipe left/right, Double-tap zoom, Pinch zoom)
  let touchStartX = 0;
  let touchStartY = 0;
  let touchEndX = 0;
  let touchEndY = 0;
  let lastTapTime = 0;
  let initialPinchDistance = null;

  const stage = document.getElementById('lightbox-stage');
  const imgEl = document.getElementById('lightbox-image');

  if (stage) {
    stage.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
      } else if (e.touches.length === 2) {
        const dx = e.touches[0].clientX - e.touches[1].clientX;
        const dy = e.touches[0].clientY - e.touches[1].clientY;
        initialPinchDistance = Math.hypot(dx, dy);
      }
    }, { passive: true });

    stage.addEventListener('touchmove', (e) => {
      if (e.touches.length === 2 && initialPinchDistance && imgEl) {
        const dx = e.touches[0].clientX - e.touches[1].clientX;
        const dy = e.touches[0].clientY - e.touches[1].clientY;
        const dist = Math.hypot(dx, dy);
        const scale = Math.min(Math.max(1, (dist / initialPinchDistance)), 3);
        currentZoom = scale;
        imgEl.style.transform = `scale(${currentZoom})`;
      }
    }, { passive: true });

    stage.addEventListener('touchend', (e) => {
      if (e.changedTouches.length === 1) {
        touchEndX = e.changedTouches[0].clientX;
        touchEndY = e.changedTouches[0].clientY;

        const diffX = touchEndX - touchStartX;
        const diffY = touchEndY - touchStartY;
        const absX = Math.abs(diffX);
        const absY = Math.abs(diffY);

        // Double tap zoom toggle
        const now = Date.now();
        if (absX < 15 && absY < 15) {
          if (now - lastTapTime < 300) {
            currentZoom = currentZoom === 1 ? 2 : 1;
            if (imgEl) imgEl.style.transform = `scale(${currentZoom})`;
          }
          lastTapTime = now;
          return;
        }

        // If zoomed in, skip swipe gestures to allow panning
        if (currentZoom > 1) return;

        // Swipe down to close
        if (diffY > 80 && absY > absX) {
          closeLightbox();
          return;
        }

        // Horizontal navigation swipe
        if (absX > 50 && absX > absY) {
          if (diffX > 0) {
            showPrevItem();
          } else {
            showNextItem();
          }
        }
      }
      initialPinchDistance = null;
    }, { passive: true });
  }

  // Mobile Bottom Sheet Peek Handle
  if (peekHandle && mobileDetails) {
    peekHandle.addEventListener('click', (e) => {
      if (e.target.closest('#lightbox-mobile-enquire-btn')) return;
      mobileDetails.classList.toggle('hidden');
    });
  }

  // Enquiry Buttons (Prefill form & scroll)
  if (desktopEnquireBtn) desktopEnquireBtn.addEventListener('click', handleEnquiryPrefill);
  if (mobileEnquireBtn) mobileEnquireBtn.addEventListener('click', handleEnquiryPrefill);

  // Check URL hash for direct piece deep-linking
  const hash = window.location.hash.replace('#', '').trim();
  if (hash && hash.startsWith('item-') && window.GALLERY_ITEMS) {
    const targetIdx = window.GALLERY_ITEMS.findIndex(item => item.id === hash);
    if (targetIdx !== -1) {
      setTimeout(() => openLightbox(targetIdx), 200);
    }
  }
}

function openLightbox(index, triggerEl = null) {
  const modal = document.getElementById('lightbox-modal');
  if (!modal || !currentFilteredItems.length) return;

  activeLightboxIndex = index;
  lastFocusedTile = triggerEl || document.activeElement;
  currentZoom = 1;

  modal.classList.remove('hidden');
  document.body.classList.add('overflow-hidden');

  renderFilmstrip();
  updateLightboxContent();

  const closeBtn = document.getElementById('lightbox-close');
  if (closeBtn && window.innerWidth >= 768) {
    closeBtn.focus();
  } else {
    const mobileClose = document.getElementById('lightbox-mobile-close');
    if (mobileClose) mobileClose.focus();
  }
}

function closeLightbox() {
  const modal = document.getElementById('lightbox-modal');
  if (!modal || modal.classList.contains('hidden')) return;

  modal.classList.add('hidden');
  document.body.classList.remove('overflow-hidden');
  currentZoom = 1;

  const imgEl = document.getElementById('lightbox-image');
  if (imgEl) imgEl.style.transform = 'scale(1)';

  const mobileDetails = document.getElementById('lightbox-mobile-details');
  if (mobileDetails) mobileDetails.classList.add('hidden');

  // Reset URL hash to category
  const slug = getCatSlug(activeCategory);
  history.replaceState(null, '', '#' + slug);

  if (lastFocusedTile && typeof lastFocusedTile.focus === 'function') {
    lastFocusedTile.focus();
  }
}

function showPrevItem() {
  if (!currentFilteredItems.length) return;
  activeLightboxIndex = (activeLightboxIndex - 1 + currentFilteredItems.length) % currentFilteredItems.length;
  updateLightboxContent();
}

function showNextItem() {
  if (!currentFilteredItems.length) return;
  activeLightboxIndex = (activeLightboxIndex + 1) % currentFilteredItems.length;
  updateLightboxContent();
}

function updateLightboxContent() {
  const item = currentFilteredItems[activeLightboxIndex];
  if (!item) return;

  currentZoom = 1;
  const imgEl = document.getElementById('lightbox-image');
  if (imgEl) {
    imgEl.style.transform = 'scale(1)';
    imgEl.style.opacity = '0';
    const newImg = new Image();
    newImg.src = item.full || item.src;
    newImg.onload = () => {
      imgEl.src = item.full || item.src;
      imgEl.alt = `${item.title} - Custom Woodwork`;
      imgEl.style.opacity = '1';
    };
    if (newImg.complete) {
      imgEl.src = item.full || item.src;
      imgEl.alt = `${item.title} - Custom Woodwork`;
      imgEl.style.opacity = '1';
    }
  }

  // Preload adjacent images
  const nextIdx = (activeLightboxIndex + 1) % currentFilteredItems.length;
  const prevIdx = (activeLightboxIndex - 1 + currentFilteredItems.length) % currentFilteredItems.length;
  if (currentFilteredItems[nextIdx]) {
    const pNext = new Image();
    pNext.src = currentFilteredItems[nextIdx].full || currentFilteredItems[nextIdx].src;
  }
  if (currentFilteredItems[prevIdx]) {
    const pPrev = new Image();
    pPrev.src = currentFilteredItems[prevIdx].full || currentFilteredItems[prevIdx].src;
  }

  // Counter
  const counterText = `${activeLightboxIndex + 1} / ${currentFilteredItems.length}`;
  const counterEl = document.getElementById('lightbox-counter');
  const mobileCounterEl = document.getElementById('lightbox-mobile-counter');
  if (counterEl) counterEl.textContent = counterText;
  if (mobileCounterEl) mobileCounterEl.textContent = counterText;

  // Title & Category
  const titleEl = document.getElementById('lightbox-title');
  const categoryEl = document.getElementById('lightbox-category');
  const mobileTitle = document.getElementById('lightbox-mobile-title');
  const mobileCategory = document.getElementById('lightbox-mobile-category');
  if (titleEl) titleEl.textContent = item.title;
  if (categoryEl) categoryEl.textContent = item.category;
  if (mobileTitle) mobileTitle.textContent = item.title;
  if (mobileCategory) mobileCategory.textContent = item.category;

  // Material: Only display if defined in config
  const matWrapper = document.getElementById('lightbox-material-wrapper');
  const matEl = document.getElementById('lightbox-material');
  const mobMatWrapper = document.getElementById('lightbox-mobile-material-wrapper');
  const mobMat = document.getElementById('lightbox-mobile-material');
  if (item.material && item.material.trim()) {
    if (matWrapper) matWrapper.classList.remove('hidden');
    if (matEl) matEl.textContent = item.material;
    if (mobMatWrapper) mobMatWrapper.classList.remove('hidden');
    if (mobMat) mobMat.textContent = item.material;
  } else {
    if (matWrapper) matWrapper.classList.add('hidden');
    if (mobMatWrapper) mobMatWrapper.classList.add('hidden');
  }

  // Description: Only display if defined in config
  const descWrapper = document.getElementById('lightbox-desc-wrapper');
  const descEl = document.getElementById('lightbox-description');
  const mobDescWrapper = document.getElementById('lightbox-mobile-desc-wrapper');
  const mobDesc = document.getElementById('lightbox-mobile-description');
  if (item.description && item.description.trim()) {
    if (descWrapper) descWrapper.classList.remove('hidden');
    if (descEl) descEl.textContent = item.description;
    if (mobDescWrapper) mobDescWrapper.classList.remove('hidden');
    if (mobDesc) mobDesc.textContent = item.description;
  } else {
    if (descWrapper) descWrapper.classList.add('hidden');
    if (mobDescWrapper) mobDescWrapper.classList.add('hidden');
  }

  // WhatsApp Share Link
  const businessPhone = window.SITE_CONFIG?.business?.whatsappClean || "919876543210";
  const shareUrl = `${window.location.origin}${window.location.pathname}#${item.id}`;
  const shareMsg = `Hello Abhishek Wood Works, I am looking at "${item.title}" (${item.category}) in your portfolio:\n${shareUrl}`;
  const shareHref = `https://wa.me/${businessPhone}?text=${encodeURIComponent(shareMsg)}`;

  const desktopShare = document.getElementById('lightbox-share-whatsapp');
  const mobileShare = document.getElementById('lightbox-mobile-share-whatsapp');
  if (desktopShare) desktopShare.href = shareHref;
  if (mobileShare) mobileShare.href = shareHref;

  // URL hash sync
  history.replaceState(null, '', '#' + item.id);

  // Update filmstrip active state
  updateFilmstripActive();
}

function renderFilmstrip() {
  const filmstripEl = document.getElementById('lightbox-filmstrip');
  if (!filmstripEl) return;

  filmstripEl.innerHTML = currentFilteredItems.map((item, idx) => {
    const isActive = idx === activeLightboxIndex;
    return `
      <button
        type="button"
        data-filmstrip-index="${idx}"
        class="filmstrip-item relative shrink-0 w-14 h-14 bg-wood-dark overflow-hidden transition-all duration-200 border-2 ${
          isActive ? 'border-amber-accent opacity-100 scale-105' : 'border-transparent opacity-50 hover:opacity-85'
        }"
        aria-label="View piece ${idx + 1}: ${item.title}"
      >
        <img src="${item.thumb || item.src}" alt="${item.title}" class="w-full h-full object-cover" loading="lazy" />
      </button>
    `;
  }).join('');

  filmstripEl.querySelectorAll('.filmstrip-item').forEach(btn => {
    btn.addEventListener('click', () => {
      const idx = parseInt(btn.getAttribute('data-filmstrip-index'), 10);
      activeLightboxIndex = idx;
      updateLightboxContent();
    });
  });

  updateFilmstripActive();
}

function updateFilmstripActive() {
  const filmstripEl = document.getElementById('lightbox-filmstrip');
  if (!filmstripEl) return;

  filmstripEl.querySelectorAll('.filmstrip-item').forEach(btn => {
    const idx = parseInt(btn.getAttribute('data-filmstrip-index'), 10);
    const isActive = idx === activeLightboxIndex;
    if (isActive) {
      btn.className = 'filmstrip-item relative shrink-0 w-14 h-14 bg-wood-dark overflow-hidden transition-all duration-200 border-2 border-amber-accent opacity-100 scale-105';
      btn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    } else {
      btn.className = 'filmstrip-item relative shrink-0 w-14 h-14 bg-wood-dark overflow-hidden transition-all duration-200 border-2 border-transparent opacity-50 hover:opacity-85';
    }
  });
}

function handleEnquiryPrefill() {
  const item = currentFilteredItems[activeLightboxIndex];
  if (!item) return;

  closeLightbox();

  const enquirySection = document.getElementById('enquiry');
  if (enquirySection) {
    enquirySection.scrollIntoView({ behavior: 'smooth' });
  }

  const projectTypeSelect = document.getElementById('enquiry-project-type');
  const messageTextarea = document.getElementById('enquiry-message');

  if (projectTypeSelect) {
    const cat = item.category.toLowerCase();
    for (let i = 0; i < projectTypeSelect.options.length; i++) {
      const opt = projectTypeSelect.options[i];
      const val = opt.value.toLowerCase();
      const text = opt.text.toLowerCase();
      if (
        val && (
          val === cat || 
          text.includes(cat) || 
          cat.includes(val) ||
          (cat.startsWith('wardrobe') && val.startsWith('wardrobe')) ||
          (cat.startsWith('sofa') && val.startsWith('sofa')) ||
          (cat.startsWith('dining') && val.startsWith('dining')) ||
          (cat.startsWith('kitchen') && val.startsWith('kitchen')) ||
          (cat.startsWith('door') && val.startsWith('door')) ||
          (cat.startsWith('tv') && val.startsWith('tv')) ||
          (cat.startsWith('bed') && val.startsWith('bed'))
        )
      ) {
        projectTypeSelect.selectedIndex = i;
        projectTypeSelect.value = opt.value;
        projectTypeSelect.dispatchEvent(new Event('change', { bubbles: true }));
        break;
      }
    }
  }

  if (messageTextarea) {
    messageTextarea.value = `Hello, I saw "${item.title}" in your gallery and would like to enquire about getting a custom piece built with similar specifications.`;
    messageTextarea.focus();
  }
}


/* ==========================================================================
   4. Enquiry Form & Direct WhatsApp Integration
   ========================================================================== */
function initEnquiryForm() {
  const form = document.getElementById('project-enquiry-form');
  const whatsappBtn = document.getElementById('whatsapp-direct-submit-btn');

  if (whatsappBtn) {
    whatsappBtn.addEventListener('click', (e) => {
      e.preventDefault();

      const name = (document.getElementById('enquiry-name')?.value || '').trim();
      const phone = (document.getElementById('enquiry-phone')?.value || '').trim();
      const projectType = document.getElementById('enquiry-project-type')?.value || '';
      const budget = document.getElementById('enquiry-budget')?.value || '';
      const timeline = document.getElementById('enquiry-timeline')?.value || '';
      const message = (document.getElementById('enquiry-message')?.value || '').trim();

      const businessPhone = window.SITE_CONFIG?.business?.whatsappClean || "919876543210";

      let text = `*New Custom Woodwork Enquiry*\n`;
      if (name) text += `• *Name:* ${name}\n`;
      if (phone) text += `• *Phone:* ${phone}\n`;
      if (projectType) text += `• *Requirement:* ${projectType}\n`;
      if (budget) text += `• *Budget:* ${budget}\n`;
      if (timeline) text += `• *Timeline:* ${timeline}\n`;
      if (message) text += `• *Details:* ${message}\n`;
      text += `\n_Sent via Abhishek Wood Works Portfolio_`;

      const encoded = encodeURIComponent(text);
      window.open(`https://wa.me/${businessPhone}?text=${encoded}`, '_blank');
    });
  }

  if (form) {
    form.addEventListener('submit', (e) => {
      // Standard HTML submission or AJAX can proceed
      // If action key is placeholder, give a friendly notice
      const accessKey = form.querySelector('input[name="access_key"]')?.value;
      if (accessKey && accessKey.includes('[TODO')) {
        e.preventDefault();
        alert('Notice: Form submission backend access key is set to [TODO] in site-config.js. Please use the "Send on WhatsApp Instead" button or configure your Web3Forms/Formspree access key.');
      }
    });
  }
}
