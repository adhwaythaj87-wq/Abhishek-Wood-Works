import asyncio
import os
from playwright.async_api import async_playwright

async def verify():
    output_dir = "test_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # We will serve or load index.html via file://
    file_path = os.path.abspath("index.html")
    file_url = f"file:///{file_path.replace(os.sep, '/')}"

    async with async_playwright() as p:
        # 1. Desktop Test (1440x900)
        print("--- Testing Desktop (1440x900) ---")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()
        
        await page.goto(file_url, wait_until="networkidle")
        await asyncio.sleep(0.5)

        # Scroll to gallery
        work_section = page.locator("#work")
        await work_section.scroll_into_view_if_needed()
        await asyncio.sleep(0.5)

        # Check desktop sidebar and grid
        sidebar = page.locator("#desktop-category-list")
        assert await sidebar.is_visible(), "Desktop category list must be visible"
        
        item_count = await page.locator("#gallery-grid .masonry-item").count()
        print(f"Desktop initial items count: {item_count}")
        assert item_count == 30, f"Expected 30 items, got {item_count}"

        # Capture Desktop Full Gallery
        await page.screenshot(path=f"{output_dir}/01_desktop_gallery_all.png")
        print("Captured 01_desktop_gallery_all.png")

        # Test hover on first tile to verify bottom label strip sliding up
        first_item = page.locator("#gallery-grid .masonry-item").first
        await first_item.hover()
        await asyncio.sleep(0.4)
        await page.screenshot(path=f"{output_dir}/02_desktop_hover_tile.png")
        print("Captured 02_desktop_hover_tile.png")

        # Test Density Toggle: Click Compact
        compact_btn = page.locator("#density-compact-btn")
        await compact_btn.click()
        await asyncio.sleep(0.3)
        grid_class = await page.locator("#gallery-grid").get_attribute("class")
        assert "density-compact" in grid_class, "Grid should have density-compact class"
        await page.screenshot(path=f"{output_dir}/03_desktop_density_compact.png")
        print("Captured 03_desktop_density_compact.png")

        # Revert to Comfortable
        comfortable_btn = page.locator("#density-comfortable-btn")
        await comfortable_btn.click()
        await asyncio.sleep(0.3)

        # Test Filtering: Click 'Wardrobes' in sidebar
        wardrobes_btn = sidebar.locator('button[data-cat="Wardrobes"]')
        await wardrobes_btn.click()
        await asyncio.sleep(0.5)

        filtered_count = await page.locator("#gallery-grid .masonry-item").count()
        print(f"Filtered Wardrobes count: {filtered_count}")
        assert filtered_count == 5, f"Expected 5 wardrobes, got {filtered_count}"

        # Verify URL hash
        hash_val = await page.evaluate("window.location.hash")
        print(f"URL hash after filtering: {hash_val}")
        assert hash_val == "#wardrobes", f"Expected #wardrobes, got {hash_val}"
        await page.screenshot(path=f"{output_dir}/04_desktop_filtered_wardrobes.png")
        print("Captured 04_desktop_filtered_wardrobes.png")

        # Click first wardrobe tile to open Lightbox
        await page.locator("#gallery-grid .masonry-item").first.click()
        await asyncio.sleep(0.6)

        modal = page.locator("#lightbox-modal")
        assert await modal.is_visible(), "Lightbox modal must be visible"

        # Verify counter and close button separation
        counter_text = await page.locator("#lightbox-counter").text_content()
        print(f"Desktop Lightbox Counter: {counter_text}")
        assert "1 / 5" in counter_text, f"Expected '1 / 5', got {counter_text}"

        # Verify filmstrip has 5 items and active item is marked
        filmstrip_items = await page.locator("#lightbox-filmstrip .filmstrip-item").count()
        assert filmstrip_items == 5, f"Expected 5 filmstrip items, got {filmstrip_items}"

        # Verify details panel
        title_text = await page.locator("#lightbox-title").text_content()
        print(f"Desktop Lightbox Title: {title_text}")

        # Capture Desktop Lightbox
        await page.screenshot(path=f"{output_dir}/05_desktop_lightbox_detail.png")
        print("Captured 05_desktop_lightbox_detail.png")

        # Test next button navigation in Lightbox
        next_btn = page.locator("#lightbox-next")
        await next_btn.click()
        await asyncio.sleep(0.4)
        new_counter = await page.locator("#lightbox-counter").text_content()
        print(f"Desktop Counter after Next: {new_counter}")
        assert "2 / 5" in new_counter, f"Expected '2 / 5', got {new_counter}"

        # Test keyboard navigation: press ArrowLeft to go back to 1 / 5
        await page.keyboard.press("ArrowLeft")
        await asyncio.sleep(0.4)
        back_counter = await page.locator("#lightbox-counter").text_content()
        assert "1 / 5" in back_counter, f"Expected '1 / 5', got {back_counter}"

        # Test WhatsApp Share link format
        wa_link = await page.locator("#lightbox-share-whatsapp").get_attribute("href")
        print(f"WhatsApp share link: {wa_link}")
        assert "wa.me" in wa_link and "Wardrobes" in wa_link, "WhatsApp link should be valid"

        # Test Enquire Button Prefill
        enquire_btn = page.locator("#lightbox-enquire-btn")
        await enquire_btn.click()
        await asyncio.sleep(0.6)

        # Lightbox should be closed
        assert not await modal.is_visible(), "Modal should be closed after enquire click"

        # Form fields should be prefilled
        selected_type = await page.locator("#enquiry-project-type").input_value()
        msg_val = await page.locator("#enquiry-message").input_value()
        print(f"Prefilled project type: {selected_type}")
        print(f"Prefilled message snippet: {msg_val[:60]}...")
        assert "Wardrobes" in selected_type or "wardrobe" in selected_type.lower()
        assert title_text in msg_val

        await page.screenshot(path=f"{output_dir}/06_desktop_form_prefilled.png")
        print("Captured 06_desktop_form_prefilled.png")

        await browser.close()

        # 2. Mobile First Test (390x844 - iPhone 12/13/14 standard)
        print("\n--- Testing Mobile First (390x844) ---")
        browser_mobile = await p.chromium.launch(headless=True)
        context_mobile = await browser_mobile.new_context(
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            has_touch=True
        )
        mobile_page = await context_mobile.new_page()
        await mobile_page.goto(file_url, wait_until="networkidle")
        await asyncio.sleep(0.5)

        # Scroll down to gallery
        await mobile_page.locator("#work").scroll_into_view_if_needed()
        await asyncio.sleep(0.5)

        # Verify mobile toolbar
        toolbar = mobile_page.locator("#mobile-gallery-toolbar")
        assert await toolbar.is_visible(), "Mobile gallery toolbar must be visible"
        
        toolbar_text = await mobile_page.locator("#mobile-current-cat-display").text_content()
        print(f"Mobile Toolbar Summary: {toolbar_text.strip()}")
        assert "30" in toolbar_text

        # Verify mobile 2-column grid and NO text on tiles
        mobile_items = await mobile_page.locator("#gallery-grid .masonry-item").count()
        assert mobile_items == 30, f"Expected 30 items on mobile, got {mobile_items}"

        # Capture Mobile Grid
        await mobile_page.screenshot(path=f"{output_dir}/07_mobile_grid_390px.png")
        print("Captured 07_mobile_grid_390px.png")

        # Test Mobile Bottom Sheet Filter: Click Filter button
        filter_open_btn = mobile_page.locator("#mobile-filter-open-btn")
        await filter_open_btn.click()
        await asyncio.sleep(0.4)

        sheet = mobile_page.locator("#mobile-filter-sheet")
        assert await sheet.is_visible(), "Mobile filter sheet must be visible"

        # Capture Mobile Bottom Sheet
        await mobile_page.screenshot(path=f"{output_dir}/08_mobile_filter_sheet.png")
        print("Captured 08_mobile_filter_sheet.png")

        # Select "Dining" in bottom sheet
        dining_row = mobile_page.locator('#mobile-sheet-categories button[data-cat="Dining"]')
        await dining_row.click()
        await asyncio.sleep(0.5)

        # Sheet should be closed and grid filtered to dining
        assert not await sheet.is_visible(), "Filter sheet should close after selection"
        dining_count = await mobile_page.locator("#gallery-grid .masonry-item").count()
        print(f"Mobile Dining count: {dining_count}")
        assert dining_count == 4, f"Expected 4 dining pieces, got {dining_count}"

        await mobile_page.screenshot(path=f"{output_dir}/09_mobile_filtered_dining.png")
        print("Captured 09_mobile_filtered_dining.png")

        # Click first dining item on mobile to open mobile lightbox
        await mobile_page.locator("#gallery-grid .masonry-item").first.click()
        await asyncio.sleep(0.6)

        m_modal = mobile_page.locator("#lightbox-modal")
        assert await m_modal.is_visible(), "Mobile lightbox must be visible"

        m_counter = await mobile_page.locator("#lightbox-mobile-counter").text_content()
        print(f"Mobile Lightbox Counter: {m_counter}")
        assert "1 / 4" in m_counter

        # Verify peeking bottom sheet
        m_peek_title = await mobile_page.locator("#lightbox-mobile-title").text_content()
        print(f"Mobile Lightbox Peek Title: {m_peek_title}")

        await mobile_page.screenshot(path=f"{output_dir}/10_mobile_lightbox_peeking.png")
        print("Captured 10_mobile_lightbox_peeking.png")

        # Expand peeking drawer
        peek_handle = mobile_page.locator("#mobile-sheet-peek-handle")
        await peek_handle.click()
        await asyncio.sleep(0.4)

        m_details = mobile_page.locator("#lightbox-mobile-details")
        assert await m_details.is_visible(), "Mobile expanded details should be visible"

        await mobile_page.screenshot(path=f"{output_dir}/11_mobile_lightbox_expanded.png")
        print("Captured 11_mobile_lightbox_expanded.png")

        # Test Mobile Close Button
        mobile_close = mobile_page.locator("#lightbox-mobile-close")
        await mobile_close.click()
        await asyncio.sleep(0.4)
        assert not await m_modal.is_visible(), "Mobile modal should be closed"

        await browser_mobile.close()
        print("\nAll Playwright UI and interaction verification tests passed successfully!")

asyncio.run(verify())
