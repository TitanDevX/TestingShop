from playwright.sync_api import sync_playwright

def test_shop_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://127.0.0.1:5000/")

        # Check UI exists
        assert page.locator("h1").inner_text() == "Shop"

        # Click buy button
        page.click("text=Buy")

        # Accept alert
        page.on("dialog", lambda d: d.accept())

        page.wait_for_timeout(1000)

        browser.close()