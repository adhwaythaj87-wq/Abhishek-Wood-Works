import sys
import os
import time
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r"C:\Users\adhwa\.gemini\antigravity\brain\8bdbcf5d-b3ab-4140-b62b-cd0712352e1f"

CATEGORIES = [
    {"slug": "wardrobes", "label": "Wardrobes", "expected_count": 5, "fullName": "Custom Wardrobes & Dressing Units"},
    {"slug": "doors", "label": "Doors", "expected_count": 5, "fullName": "Custom Doors & Architectural Windows"},
    {"slug": "dining", "label": "Dining", "expected_count": 5, "fullName": "Dining Tables, Chairs & Barstools"},
    {"slug": "sofas", "label": "Sofas", "expected_count": 5, "fullName": "Custom Sofas & Living Seating"},
    {"slug": "kitchens", "label": "Kitchens", "expected_count": 4, "fullName": "Modular Kitchens & Cabinetry"},
    {"slug": "living", "label": "Living", "expected_count": 4, "fullName": "TV Units, Partitions & Living Shelving"},
    {"slug": "bedroom", "label": "Bedroom", "expected_count": 2, "fullName": "Daybeds, Diwans & Bedroom Furniture"}
]

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile viewport: 390px width x 844px height, device_scale_factor=2
        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True
        )
        page = context.new_page()

        print("Navigating to http://localhost:3000/ ...")
        page.goto("http://localhost:3000/", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # 1. Check tab bar wrapping and no horizontal scroll at 390px
        tab_nav = page.locator("#gallery-category-nav")
        tab_container = page.locator("#gallery-category-tabs")
        
        tab_box = tab_container.bounding_box()
        print(f"Tabs container bounding box at 390px: width={tab_box['width']:.1f}px, height={tab_box['height']:.1f}px")
        
        # Height for at most 2 rows should be around 88-100px max (each tab row is ~44px min-height)
        assert tab_box['height'] <= 110, f"Tab container height {tab_box['height']}px exceeds 2 rows!"
        print(f"PASS: Tabs container height ({tab_box['height']:.1f}px) wraps in at most 2 rows.")

        has_h_scroll = page.evaluate("""() => {
            const nav = document.getElementById('gallery-category-nav');
            const body = document.body;
            return {
                nav_overflow: nav.scrollWidth > nav.clientWidth,
                body_overflow: body.scrollWidth > body.clientWidth,
                doc_overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
            };
        }""")
        print("Overflow check at 390px:", has_h_scroll)
        assert not has_h_scroll['nav_overflow'], "Navigation has horizontal scroll!"
        assert not has_h_scroll['body_overflow'], "Body has horizontal scroll!"
        assert not has_h_scroll['doc_overflow'], "Document has horizontal scroll!"
        print("PASS: Zero horizontal scroll at 390px.")

        # 2. Iterate through each category, click its tab, verify items and take screenshot
        for cat in CATEGORIES:
            slug = cat["slug"]
            label = cat["label"]
            expected = cat["expected_count"]
            print(f"\n--- Testing Category: {label} ({slug}) ---")

            # Click tab button
            tab_btn = page.locator(f'.category-tab-btn[data-cat="{label}"]')
            tab_btn.scroll_into_view_if_needed()
            tab_btn.click()
            page.wait_for_timeout(600) # Wait for fade reflow

            # Verify active styling
            aria_curr = tab_btn.get_attribute("aria-current")
            assert aria_curr == "true", f"Tab {label} did not become active!"

            # Verify count in grid
            cards = page.locator("#gallery-grid article.masonry-item")
            count = cards.count()
            print(f"Found {count} cards in grid (expected {expected})")
            assert count == expected, f"Category {label} expected {expected} cards, got {count}!"

            # Scroll smoothly so the tab bar is sticky and grid is prominently visible
            # Scroll to #work section
            page.evaluate("document.getElementById('work').scrollIntoView({ behavior: 'instant' })")
            page.wait_for_timeout(500)

            # Take screenshot of viewport
            screenshot_path = os.path.join(ARTIFACT_DIR, f"tab_{slug}_390px.png")
            page.screenshot(path=screenshot_path)
            print(f"Saved screenshot: {screenshot_path}")

        # 3. Test Lightbox full name display
        print("\n--- Testing Lightbox fullName & counter ---")
        # Click on Bedroom category
        bed_tab = page.locator('.category-tab-btn[data-cat="Bedroom"]')
        bed_tab.click()
        page.wait_for_timeout(500)

        # Click first card
        first_card = page.locator("#gallery-grid article.masonry-item").first
        first_card.click()
        page.wait_for_timeout(600)

        # Verify lightbox is visible
        modal = page.locator("#lightbox-modal")
        modal_classes = modal.get_attribute("class") or ""
        assert "hidden" not in modal_classes, "Lightbox modal should be open!"

        # Check full name displayed
        cat_text = page.locator("#lightbox-category").text_content().strip()
        print(f"Lightbox category displayed: '{cat_text}'")
        assert cat_text == "Daybeds, Diwans & Bedroom Furniture", f"Unexpected lightbox category: {cat_text}"

        counter_text = page.locator("#lightbox-counter").text_content().strip()
        print(f"Lightbox counter: '{counter_text}'")
        assert counter_text == "1 / 2", f"Unexpected lightbox counter: {counter_text}"

        # Take screenshot of lightbox on mobile
        lightbox_shot = os.path.join(ARTIFACT_DIR, "lightbox_bedroom_390px.png")
        page.screenshot(path=lightbox_shot)
        print(f"Saved lightbox screenshot: {lightbox_shot}")

        # Close lightbox
        close_btn = page.locator("#lightbox-mobile-close")
        close_btn.click()
        page.wait_for_timeout(400)
        modal_classes_after = modal.get_attribute("class") or ""
        assert "hidden" in modal_classes_after, "Lightbox modal should be closed!"
        print("PASS: Lightbox tested successfully.")

        # 4. Test Hero caption tap-to-scroll
        print("\n--- Testing Hero caption tap-to-scroll ---")
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(400)

        active_slide = page.locator("#hero-slider-container .hero-slide.active")
        expected_cat = active_slide.get_attribute("data-category")
        print(f"Hero active slide category: {expected_cat}")

        caption_btn = page.locator("#hero-caption-btn")
        caption_btn.click()
        page.wait_for_timeout(800)

        active_tab = page.locator(f'.category-tab-btn[data-cat="{expected_cat}"]')
        assert active_tab.get_attribute("aria-current") == "true", f"Hero caption button did not activate {expected_cat}!"
        print(f"PASS: Hero caption button correctly activated {expected_cat} category.")

        browser.close()
        print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run()
