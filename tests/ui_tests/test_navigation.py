import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
class TestNavigation:
    """Test suite for page navigation and routing"""

    def test_home_page_loads(self, page: Page, base_url):
        """Test that the home page loads successfully"""
        page.goto(base_url)
        expect(page).to_have_title("Testing Demo - Home")
        expect(page.locator("h2")).to_contain_text("Welcome to the Testing Demo")

    def test_navigation_links_present(self, page: Page, base_url):
        """Test that all navigation links are present"""
        page.goto(base_url)

        # Check navigation links
        home_link = page.locator('a[href="/"]')
        form_link = page.locator('a[href="/form.html"]')
        about_link = page.locator('a[href="/about.html"]')

        expect(home_link).to_be_visible()
        expect(form_link).to_be_visible()
        expect(about_link).to_be_visible()

    def test_navigate_to_form_page(self, page: Page, base_url):
        """Test navigation from home to form page"""
        page.goto(base_url)
        page.click('a[href="/form.html"]')

        expect(page).to_have_url(f"{base_url}/form.html")
        expect(page).to_have_title("Testing Demo - Contact Form")
        expect(page.locator("h2")).to_contain_text("Contact Form")

    def test_navigate_to_about_page(self, page: Page, base_url):
        """Test navigation from home to about page"""
        page.goto(base_url)
        page.click('a[href="/about.html"]')

        expect(page).to_have_url(f"{base_url}/about.html")
        expect(page).to_have_title("Testing Demo - About")
        expect(page.locator("h2")).to_contain_text("About This Demo")

    def test_navigate_back_to_home(self, page: Page, base_url):
        """Test navigation from about page back to home"""
        page.goto(f"{base_url}/about.html")
        page.click('a[href="/"]')

        expect(page).to_have_url(base_url + "/")
        expect(page).to_have_title("Testing Demo - Home")

    def test_active_navigation_link(self, page: Page, base_url):
        """Test that the active navigation link has the correct class"""
        page.goto(base_url)

        # On home page, home link should have active class
        home_link = page.locator('.nav-links a[href="/"]')
        expect(home_link).to_have_class("active")

    def test_navigation_between_all_pages(self, page: Page, base_url):
        """Test complete navigation flow through all pages"""
        # Start at home
        page.goto(base_url)
        expect(page).to_have_title("Testing Demo - Home")

        # Go to form
        page.click('a[href="/form.html"]')
        expect(page).to_have_title("Testing Demo - Contact Form")

        # Go to about
        page.click('a[href="/about.html"]')
        expect(page).to_have_title("Testing Demo - About")

        # Back to home
        page.click('a[href="/"]')
        expect(page).to_have_title("Testing Demo - Home")

    def test_logo_is_visible(self, page: Page, base_url):
        """Test that the site logo is visible on all pages"""
        pages_to_test = ["/", "/form.html", "/about.html"]

        for path in pages_to_test:
            page.goto(f"{base_url}{path}")
            logo = page.locator(".logo")
            expect(logo).to_be_visible()
            expect(logo).to_contain_text("Testing Demo")
