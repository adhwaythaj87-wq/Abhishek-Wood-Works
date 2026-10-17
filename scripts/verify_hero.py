import asyncio
import os
import shutil
from playwright.async_api import async_playwright

ARTIFACT_DIR = r"C:\Users\adhwa\.gemini\antigravity\brain\8bdbcf5d-b3ab-4140-b62b-cd0712352e1f"
TEST_RESULTS_DIR = r"c:\Users\adhwa\OneDrive\Desktop\furniture\test_results"

async def run_verification():
    os.makedirs(TEST_RESULTS_DIR, exist_ok=True)
    os.makedirs(ARTIFACT_DIR, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # ==========================================
        # 1. MOBILE VERIFICATION (390px x 844px)
        # ==========================================
        print("\n--- Running Mobile Verification (390px x 844px) ---")
        context_mobile = await browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2
        )
        page_mobile = await context_mobile.new_page()
        await page_mobile.goto("http://localhost:3000/index.html")
        await page_mobile.wait_for_timeout(1000)

        # Check horizontal overflow
        h_scroll = await page_mobile.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")
        print(f"Mobile Horizontal Scroll Present: {h_scroll} (Expected: False)")
        assert not h_scroll, "Horizontal scroll detected on mobile 390px!"

        # Check Hero visibility and styles
        hero_data = await page_mobile.evaluate('''() => {
            const hero = document.getElementById('hero');
            const rect = hero.getBoundingClientRect();
            const label = hero.querySelector('span.text-xs.uppercase');
            const title = hero.querySelector('h1');
            const italicPart = title.querySelector('em');
            const tagline = hero.querySelector('p');
            const ctaBtn = hero.querySelector('a[href="#work"]');
            const quoteLink = hero.querySelector('a[href="#enquiry"]');
            const captionBtn = document.getElementById('hero-caption-btn');
            const captionText = document.getElementById('hero-caption-text');
            const counterText = document.getElementById('hero-counter-text');
            const whatsappPill = document.getElementById('floating-whatsapp-pill');
            
            const captionRect = captionBtn ? captionBtn.getBoundingClientRect() : null;
            const waRect = whatsappPill ? whatsappPill.getBoundingClientRect() : null;

            // Check overlap between caption button and WhatsApp pill
            let overlaps = false;
            if (captionRect && waRect) {
                overlaps = !(captionRect.right < waRect.left || 
                             captionRect.left > waRect.right || 
                             captionRect.bottom < waRect.top || 
                             captionRect.top > waRect.bottom);
            }

            return {
                heroHeight: rect.height,
                labelText: label ? label.textContent.trim() : null,
                titleText: title ? title.textContent.trim() : null,
                italicText: italicPart ? italicPart.textContent.trim() : null,
                taglineText: tagline ? tagline.textContent.trim() : null,
                ctaText: ctaBtn ? ctaBtn.textContent.trim() : null,
                ctaWidth: ctaBtn ? ctaBtn.getBoundingClientRect().width : null,
                quoteText: quoteLink ? quoteLink.textContent.trim() : null,
                captionText: captionText ? captionText.textContent.trim() : null,
                counterText: counterText ? counterText.textContent.trim() : null,
                captionRect: captionRect ? { top: captionRect.top, bottom: captionRect.bottom, left: captionRect.left, right: captionRect.right } : null,
                waRect: waRect ? { top: waRect.top, bottom: waRect.bottom, left: waRect.left, right: waRect.right } : null,
                overlapsWithWhatsApp: overlaps
            };
        }''')

        print("Mobile Hero Evaluation:")
        for k, v in hero_data.items():
            print(f"  {k}: {v}")

        assert hero_data["labelText"] == "Custom furniture · Interiors", f"Unexpected label: {hero_data['labelText']}"
        assert "Abhishek" in hero_data["titleText"] and "Wood Works" in hero_data["titleText"], f"Unexpected title: {hero_data['titleText']}"
        assert hero_data["italicText"] == "Wood Works", f"Unexpected italic text: {hero_data['italicText']}"
        assert hero_data["taglineText"] == "Made to order.", f"Unexpected tagline: {hero_data['taglineText']}"
        assert hero_data["ctaText"] == "View Our Work", f"Unexpected CTA: {hero_data['ctaText']}"
        assert hero_data["ctaWidth"] < 250, "CTA button should be content-sized, not full-width!"
        assert hero_data["quoteText"] == "Get a Quote", f"Unexpected Quote link: {hero_data['quoteText']}"
        assert not hero_data["overlapsWithWhatsApp"], "Hero caption button MUST NOT overlap floating WhatsApp pill!"

        # Capture Mobile Screenshot (First Screen / Hero)
        mobile_screenshot_path = os.path.join(TEST_RESULTS_DIR, "hero_390px.png")
        await page_mobile.screenshot(path=mobile_screenshot_path, full_page=False)
        shutil.copy(mobile_screenshot_path, os.path.join(ARTIFACT_DIR, "hero_390px.png"))
        print(f"Saved mobile screenshot: {mobile_screenshot_path}")

        # Test tapping hero caption button scrolls to category in gallery
        await page_mobile.locator("#hero-caption-btn").click()
        await page_mobile.wait_for_timeout(800)
        scroll_y = await page_mobile.evaluate("() => window.scrollY")
        active_gallery_cat = await page_mobile.evaluate("() => window.activeCategory || document.querySelector('.category-tab-btn[aria-current=\"true\"]')?.getAttribute('data-cat')")
        print(f"After caption click: scrollY={scroll_y}, activeGalleryCat={active_gallery_cat}")
        assert scroll_y > 300, "Tapping caption button should smooth-scroll down toward the gallery!"
        assert active_gallery_cat == "Wardrobes", f"Expected 'Wardrobes' active, got {active_gallery_cat}"

        # ==========================================
        # 2. DESKTOP VERIFICATION (1440px x 900px)
        # ==========================================
        print("\n--- Running Desktop Verification (1440px x 900px) ---")
        context_desktop = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1
        )
        page_desktop = await context_desktop.new_page()
        await page_desktop.goto("http://localhost:3000/index.html")
        await page_desktop.wait_for_timeout(1000)

        # Check horizontal overflow on desktop
        h_scroll_desktop = await page_desktop.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")
        print(f"Desktop Horizontal Scroll Present: {h_scroll_desktop} (Expected: False)")
        assert not h_scroll_desktop, "Horizontal scroll detected on desktop 1440px!"

        # Check desktop dots navigation
        dots_count = await page_desktop.locator("#hero-dots .hero-dot").count()
        print(f"Desktop Hero Indicator Dots count: {dots_count} (Expected: 4)")
        assert dots_count == 4, f"Expected 4 hero dots, found {dots_count}"

        # Check initial slide (Slide 0: Teak wardrobe)
        initial_slide_info = await page_desktop.evaluate('''() => {
            const activeSlide = document.querySelector('#hero-slider-container .hero-slide.active');
            const caption = document.getElementById('hero-caption-text')?.textContent.trim();
            const counter = document.getElementById('hero-counter-text')?.textContent.trim();
            const activeDot = document.querySelector('#hero-dots .hero-dot[aria-current="true"]');
            return {
                caption,
                counter,
                activeDotIdx: activeDot ? activeDot.getAttribute('data-hero-slide') : null,
                slideCaptionAttr: activeSlide ? activeSlide.getAttribute('data-caption') : null
            };
        }''')
        print(f"Initial Slide 0 Info: {initial_slide_info}")
        assert initial_slide_info["caption"] == "Teak wardrobe", f"Expected Teak wardrobe, got {initial_slide_info['caption']}"
        assert initial_slide_info["counter"] == "1 / 4", f"Expected 1 / 4, got {initial_slide_info['counter']}"

        # Click Dot 1 (Teak entry door)
        print("Clicking Dot 1 (Teak entry door)...")
        await page_desktop.locator('button[data-hero-slide="1"]').click()
        await page_desktop.wait_for_timeout(500)

        slide1_info = await page_desktop.evaluate('''() => {
            const activeSlide = document.querySelector('#hero-slider-container .hero-slide.active');
            const caption = document.getElementById('hero-caption-text')?.textContent.trim();
            const counter = document.getElementById('hero-counter-text')?.textContent.trim();
            const activeDot = document.querySelector('#hero-dots .hero-dot[aria-current="true"]');
            return {
                caption,
                counter,
                activeDotIdx: activeDot ? activeDot.getAttribute('data-hero-slide') : null,
                slideIndex: activeSlide ? activeSlide.getAttribute('data-index') : null
            };
        }''')
        print(f"After Dot 1 Click: {slide1_info}")
        assert slide1_info["caption"] == "Teak entry door", f"Expected Teak entry door, got {slide1_info['caption']}"
        assert slide1_info["counter"] == "2 / 4", f"Expected 2 / 4, got {slide1_info['counter']}"
        assert slide1_info["slideIndex"] == "1", f"Expected slide 1, got {slide1_info['slideIndex']}"

        # Click Dot 2 (Dining chair)
        print("Clicking Dot 2 (Dining chair)...")
        await page_desktop.locator('button[data-hero-slide="2"]').click()
        await page_desktop.wait_for_timeout(500)

        slide2_info = await page_desktop.evaluate('''() => {
            const activeSlide = document.querySelector('#hero-slider-container .hero-slide.active');
            const caption = document.getElementById('hero-caption-text')?.textContent.trim();
            const counter = document.getElementById('hero-counter-text')?.textContent.trim();
            return {
                caption,
                counter,
                slideIndex: activeSlide ? activeSlide.getAttribute('data-index') : null
            };
        }''')
        print(f"After Dot 2 Click: {slide2_info}")
        assert slide2_info["caption"] == "Dining chair", f"Expected Dining chair, got {slide2_info['caption']}"
        assert slide2_info["counter"] == "3 / 4", f"Expected 3 / 4, got {slide2_info['counter']}"

        # Check Desktop Overlap between WhatsApp pill and hero caption button
        desktop_overlap = await page_desktop.evaluate('''() => {
            const captionBtn = document.getElementById('hero-caption-btn');
            const whatsappPill = document.getElementById('floating-whatsapp-pill');
            const cRect = captionBtn.getBoundingClientRect();
            const wRect = whatsappPill.getBoundingClientRect();

            return !(cRect.right < wRect.left || 
                     cRect.left > wRect.right || 
                     cRect.bottom < wRect.top || 
                     cRect.top > wRect.bottom);
        }''')
        print(f"Desktop Caption vs WhatsApp Pill Overlap: {desktop_overlap} (Expected: False)")
        assert not desktop_overlap, "Desktop hero caption button must NOT overlap floating WhatsApp pill!"

        # Reset to slide 0 for clean screenshot
        await page_desktop.locator('button[data-hero-slide="0"]').click()
        await page_desktop.wait_for_timeout(600)

        # Capture Desktop Screenshot (First Screen / Hero)
        desktop_screenshot_path = os.path.join(TEST_RESULTS_DIR, "hero_1440px.png")
        await page_desktop.screenshot(path=desktop_screenshot_path, full_page=False)
        shutil.copy(desktop_screenshot_path, os.path.join(ARTIFACT_DIR, "hero_1440px.png"))
        print(f"Saved desktop screenshot: {desktop_screenshot_path}")

        # Check text contrast ratio
        contrast_data = await page_desktop.evaluate('''() => {
            function getLuminance(r, g, b) {
                const [rs, gs, bs] = [r, g, b].map(c => {
                    c = c / 255;
                    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
                });
                return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
            }
            function getContrast(l1, l2) {
                const lighter = Math.max(l1, l2);
                const darker = Math.min(l1, l2);
                return (lighter + 0.05) / (darker + 0.05);
            }
            // #F1E3C8 is rgb(241, 227, 200)
            const creamLum = getLuminance(241, 227, 200);
            // #0E0A08 is rgb(14, 10, 8)
            const walnutLum = getLuminance(14, 10, 8);
            // Amber accent #D98B2B is rgb(217, 139, 43)
            const amberLum = getLuminance(217, 139, 43);

            return {
                creamOnWalnut: getContrast(creamLum, walnutLum).toFixed(2),
                amberOnWalnut: getContrast(amberLum, walnutLum).toFixed(2)
            };
        }''')
        print(f"Contrast Ratios: Cream on dark-walnut gradient={contrast_data['creamOnWalnut']}:1 (WCAG AA requires 4.5:1, AAA requires 7:1)")
        print(f"Contrast Ratios: Amber on dark-walnut gradient={contrast_data['amberOnWalnut']}:1")

        await browser.close()
        print("\nALL HERO VERIFICATION CHECKS PASSED SUCCESSFULLY!\n")

if __name__ == '__main__':
    asyncio.run(run_verification())
