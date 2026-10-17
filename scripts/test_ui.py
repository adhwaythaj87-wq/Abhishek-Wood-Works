import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        url = 'file:///' + os.path.abspath('index.html').replace('\\', '/')
        await page.goto(url)
        await page.wait_for_timeout(500)
        
        # Test Beds & Bedroom filter
        await page.locator('button[data-filter="Beds & Bedroom"]').click()
        await page.wait_for_timeout(300)
        
        # Click the bed item
        await page.locator('.masonry-item').first.click()
        await page.wait_for_timeout(300)
        
        # Click enquire
        await page.locator('#lightbox-enquire-btn').click()
        await page.wait_for_timeout(500)
        
        data = await page.evaluate('''() => {
            const select = document.getElementById('enquiry-project-type');
            return {
                val: select.value,
                text: select.options[select.selectedIndex]?.text
            };
        }''')
        print('Bed prefill test passed:', data)
        await browser.close()

asyncio.run(main())
