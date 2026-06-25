import pytest
import re
from playwright.sync_api import Page, expect


@pytest.mark.ui
class TestDynamicContent:
    """Test suite for dynamic content loading and interactions"""

    def test_load_data_button_present(self, page: Page, base_url):
        """Test that Load Data button is present on home page"""
        page.goto(base_url)

        load_btn = page.locator("#load-data-btn")
        expect(load_btn).to_be_visible()
        expect(load_btn).to_contain_text("Load Data")

    def test_toggle_content_button_present(self, page: Page, base_url):
        """Test that Toggle Content button is present"""
        page.goto(base_url)

        toggle_btn = page.locator("#toggle-content-btn")
        expect(toggle_btn).to_be_visible()
        expect(toggle_btn).to_contain_text("Toggle Content")

    def test_data_container_hidden_initially(self, page: Page, base_url):
        """Test that data container is hidden before clicking Load Data"""
        page.goto(base_url)

        data_container = page.locator("#data-container")
        expect(data_container).to_have_css("display", "none")

    def test_toggle_content_hidden_initially(self, page: Page, base_url):
        """Test that toggle content is hidden initially"""
        page.goto(base_url)

        toggle_content = page.locator("#toggle-content")
        expect(toggle_content).to_have_css("display", "none")

    def test_load_data_shows_items(self, page: Page, base_url):
        """Test that clicking Load Data button displays items from API"""
        page.goto(base_url)

        # Click Load Data button
        page.click("#load-data-btn")

        # Wait for data container to be visible
        data_container = page.locator("#data-container")
        expect(data_container).to_be_visible()

        # Check that items are loaded
        items_list = page.locator("#items-list li")
        expect(items_list).not_to_have_count(0)

    def test_loaded_items_have_correct_structure(self, page: Page, base_url):
        """Test that loaded items have the expected structure"""
        page.goto(base_url)

        page.click("#load-data-btn")

        # Wait for items to load
        page.wait_for_selector("#items-list li")

        # Check first item has data-item-id attribute
        first_item = page.locator("#items-list li").first
        # Just check that the attribute exists (value can be any number)
        expect(first_item).to_have_attribute("data-item-id", re.compile(r"\d+"))

        # Check that item contains text
        expect(first_item).not_to_be_empty()

    def test_load_data_button_text_changes(self, page: Page, base_url):
        """Test that Load Data button text changes after loading"""
        page.goto(base_url)

        load_btn = page.locator("#load-data-btn")

        # Initial text
        expect(load_btn).to_contain_text("Load Data")

        # Click and check text changes
        page.click("#load-data-btn")
        page.wait_for_selector("#data-container[style*='block']")

        expect(load_btn).to_contain_text("Refresh Data")

    def test_toggle_content_shows_content(self, page: Page, base_url):
        """Test that clicking Toggle Content button shows hidden content"""
        page.goto(base_url)

        toggle_content = page.locator("#toggle-content")

        # Initially hidden
        expect(toggle_content).to_have_css("display", "none")

        # Click toggle button
        page.click("#toggle-content-btn")

        # Now visible
        expect(toggle_content).to_be_visible()
        expect(toggle_content).to_contain_text("toggled")

    def test_toggle_content_hides_content(self, page: Page, base_url):
        """Test that clicking Toggle Content button again hides content"""
        page.goto(base_url)

        toggle_btn = page.locator("#toggle-content-btn")
        toggle_content = page.locator("#toggle-content")

        # Show content
        page.click("#toggle-content-btn")
        expect(toggle_content).to_be_visible()

        # Hide content
        page.click("#toggle-content-btn")
        expect(toggle_content).to_have_css("display", "none")

    def test_toggle_button_text_changes(self, page: Page, base_url):
        """Test that Toggle Content button text changes based on state"""
        page.goto(base_url)

        toggle_btn = page.locator("#toggle-content-btn")

        # Initial text
        expect(toggle_btn).to_contain_text("Toggle Content")

        # After showing content
        page.click("#toggle-content-btn")
        expect(toggle_btn).to_contain_text("Hide Content")

        # After hiding content
        page.click("#toggle-content-btn")
        expect(toggle_btn).to_contain_text("Toggle Content")

    def test_multiple_data_refreshes(self, page: Page, base_url):
        """Test that data can be refreshed multiple times"""
        page.goto(base_url)

        load_btn = page.locator("#load-data-btn")

        # Load data first time
        page.click("#load-data-btn")
        page.wait_for_selector("#data-container[style*='block']")

        # Load data second time
        page.click("#load-data-btn")

        # Data container should still be visible
        data_container = page.locator("#data-container")
        expect(data_container).to_be_visible()

        # Items should be present
        items = page.locator("#items-list li")
        expect(items).not_to_have_count(0)

    def test_features_section_visible(self, page: Page, base_url):
        """Test that features section is visible on home page"""
        page.goto(base_url)

        features_section = page.locator(".features")
        expect(features_section).to_be_visible()

        # Check feature cards
        feature_cards = page.locator(".feature-card")
        expect(feature_cards).to_have_count(3)

    def test_feature_cards_content(self, page: Page, base_url):
        """Test that feature cards have correct content"""
        page.goto(base_url)

        # Check for specific feature titles
        expect(page.locator("text=UI Testing")).to_be_visible()
        expect(page.locator("text=API Testing")).to_be_visible()
        expect(page.locator("text=CI/CD Ready")).to_be_visible()
