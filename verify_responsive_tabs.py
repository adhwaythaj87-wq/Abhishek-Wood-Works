import asyncio
import os
from playwright.async_api import async_playwright

async def run_checks():
    output_dir = "test_results"
    os.makedirs(output_dir, exist_ok=True)
    base_url = "http://localhost:3000"

    expected_labels = ["Sofas", "Dining", "Wardrobes", "Kitchens", "Doors", "TV Units", "Beds"]

    async with async_playwright() as p:
        # Check 1: 360px Mobile (Android small phone)
        print("--- Testing 360px Viewport ---")
        browser = await p.chromium.launch(headless=True)
        ctx_360 = await browser.new_context(viewport={"width": 360, "height": 740})
        p_360 = await ctx_360.new_page()
        await p_360.goto(base_url, wait_until="networkidle")
        await asyncio.sleep(0.5)

        # Check no horizontal scrolling on window
        scroll_width = await p_360.evaluate("document.documentElement.scrollWidth")
        client_width = await p_360.evaluate("document.documentElement.clientWidth")
        print(f"360px viewport: scrollWidth={scroll_width}, clientWidth={client_width}")
        assert scroll_width <= client_width, f"Horizontal scroll exists at 360px: {scroll_width} > {client_width}"

        # Check tabs container
        tabs_360 = p_360.locator("#gallery-category-tabs .category-tab-btn")
        tab_count_360 = await tabs_360.count()
        assert tab_count_360 == 7, f"Expected 7 tabs, got {tab_count_360}"
        
        # Verify text and visibility
        labels_found = []
        for i in range(tab_count_360):
            t = await tabs_360.nth(i).inner_text()
            labels_found.append(t.strip())
            is_vis = await tabs_360.nth(i).is_visible()
            assert is_vis, f"Tab {t} should be visible at 360px"
        print(f"360px tabs found: {labels_found}")
        assert labels_found == expected_labels, f"Expected {expected_labels}, got {labels_found}"

        # Verify no 'All Work'
        page_content_360 = await p_360.content()
        assert "All Work" not in page_content_360, "Found 'All Work' in page at 360px"
        assert "All Pieces" not in page_content_360, "Found 'All Pieces' in page at 360px"

        # Verify default selected is Wardrobes
        active_tab_360 = p_360.locator('#gallery-category-tabs .category-tab-btn[aria-current="true"]')
        active_text_360 = await active_tab_360.inner_text()
        print(f"360px active tab: {active_text_360}")
        assert "Wardrobes" in active_text_360

        # Verify Wardrobes count in grid
        items_360 = await p_360.locator("#gallery-grid .masonry-item").count()
        print(f"360px Wardrobes items in grid: {items_360}")
        assert items_360 == 5, f"Expected 5 wardrobe items, got {items_360}"

        # Check height of sticky tab nav: takes at most 2 rows of height on mobile
        nav_box_360 = await p_360.locator("#gallery-category-nav").bounding_box()
        print(f"360px nav height: {nav_box_360['height']}px")
        # 2 rows of ~44px + py-1 padding is ~96-105px. Must be <= 120px
        assert nav_box_360['height'] <= 120, f"Nav takes more than 2 rows: {nav_box_360['height']}px"

        await p_360.screenshot(path=f"{output_dir}/tabs_360px.png")
        print("Captured tabs_360px.png")
        await ctx_360.close()

        # Check 2: 390px Mobile (iPhone 12/13/14)
        print("\n--- Testing 390px Viewport ---")
        ctx_390 = await browser.new_context(viewport={"width": 390, "height": 844})
        p_390 = await ctx_390.new_page()
        await p_390.goto(base_url, wait_until="networkidle")
        await asyncio.sleep(0.5)

        # Check horizontal scroll
        scroll_width_390 = await p_390.evaluate("document.documentElement.scrollWidth")
        client_width_390 = await p_390.evaluate("document.documentElement.clientWidth")
        print(f"390px viewport: scrollWidth={scroll_width_390}, clientWidth={client_width_390}")
        assert scroll_width_390 <= client_width_390, "Horizontal scroll exists at 390px"

        # Check tap target heights: 44px
        tabs_390 = p_390.locator("#gallery-category-tabs .category-tab-btn")
        for i in range(7):
            box = await tabs_390.nth(i).bounding_box()
            assert box['height'] >= 43.5, f"Tab {i} height {box['height']} is less than 44px"

        nav_box_390 = await p_390.locator("#gallery-category-nav").bounding_box()
        print(f"390px nav height: {nav_box_390['height']}px")
        assert nav_box_390['height'] <= 120, f"Nav takes more than 2 rows at 390px: {nav_box_390['height']}px"

        # Test clicking 'Dining'
        dining_tab = p_390.locator('#gallery-category-tabs .category-tab-btn[data-cat="Dining"]')
        await dining_tab.click()
        await asyncio.sleep(0.5)

        dining_count_390 = await p_390.locator("#gallery-grid .masonry-item").count()
        print(f"390px Dining items count: {dining_count_390}")
        assert dining_count_390 == 4, f"Expected 4 dining items, got {dining_count_390}"

        # Check URL hash
        hash_390 = await p_390.evaluate("window.location.hash")
        print(f"390px URL hash: {hash_390}")
        assert hash_390 == "#dining"

        await p_390.screenshot(path=f"{output_dir}/tabs_390px.png")
        print("Captured tabs_390px.png")
        await ctx_390.close()

        # Check 3: 768px Tablet (iPad / Medium screen)
        print("\n--- Testing 768px Viewport ---")
        ctx_768 = await browser.new_context(viewport={"width": 768, "height": 1024})
        p_768 = await ctx_768.new_page()
        await p_768.goto(base_url, wait_until="networkidle")
        await asyncio.sleep(0.5)

        # Check horizontal scroll
        scroll_width_768 = await p_768.evaluate("document.documentElement.scrollWidth")
        client_width_768 = await p_768.evaluate("document.documentElement.clientWidth")
        assert scroll_width_768 <= client_width_768, "Horizontal scroll exists at 768px"

        # Check 7 tabs in ONE centered row
        nav_box_768 = await p_768.locator("#gallery-category-nav").bounding_box()
        print(f"768px nav height: {nav_box_768['height']}px")
        # In one single row, height is ~50-60px
        assert nav_box_768['height'] <= 65, f"Nav at 768px should be single row (height <= 65px), got {nav_box_768['height']}px"

        # Heading line check: show current category count only e.g. "5 pieces"
        count_heading_text = await p_768.locator("#gallery-count-text").text_content()
        print(f"768px count text: '{count_heading_text.strip()}'")
        assert count_heading_text.strip() == "5 pieces", f"Expected '5 pieces', got '{count_heading_text}'"

        await p_768.screenshot(path=f"{output_dir}/tabs_768px.png")
        print("Captured tabs_768px.png")
        await ctx_768.close()

        # Check 4: Deep Link Hash load (e.g. #kitchens)
        print("\n--- Testing Direct Deep Link #kitchens ---")
        ctx_hash = await browser.new_context(viewport={"width": 1440, "height": 900})
        p_hash = await ctx_hash.new_page()
        await p_hash.goto(f"{base_url}/#kitchens", wait_until="networkidle")
        await asyncio.sleep(0.5)

        active_tab_hash = p_hash.locator('#gallery-category-tabs .category-tab-btn[aria-current="true"]')
        active_tab_name = await active_tab_hash.inner_text()
        print(f"Active tab when loaded with #kitchens: {active_tab_name}")
        assert "Kitchens" in active_tab_name

        kitchen_count = await p_hash.locator("#gallery-grid .masonry-item").count()
        print(f"Kitchen items count: {kitchen_count}")
        assert kitchen_count == 4

        # Open lightbox in Kitchens to verify counter and filmstrip
        await p_hash.locator("#gallery-grid .masonry-item").first.click()
        await asyncio.sleep(0.5)
        lb_counter = await p_hash.locator("#lightbox-counter").text_content()
        print(f"Lightbox counter: {lb_counter}")
        assert "1 / 4" in lb_counter

        filmstrip_count = await p_hash.locator("#lightbox-filmstrip .filmstrip-item").count()
        print(f"Filmstrip items count: {filmstrip_count}")
        assert filmstrip_count == 4

        await p_hash.screenshot(path=f"{output_dir}/deep_link_kitchens.png")
        print("Captured deep_link_kitchens.png")
        await ctx_hash.close()

        await browser.close()
        print("\nALL RESPONSIVE AND TAB CHECKS PASSED PERFECTLY!")

asyncio.run(run_checks())
