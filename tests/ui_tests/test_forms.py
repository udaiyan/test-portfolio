import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
class TestForms:
    """Test suite for form validation and submission"""

    def test_form_elements_present(self, page: Page, base_url):
        """Test that all form elements are present"""
        page.goto(f"{base_url}/form.html")

        expect(page.locator("#name")).to_be_visible()
        expect(page.locator("#email")).to_be_visible()
        expect(page.locator("#message")).to_be_visible()
        expect(page.locator("#submit-btn")).to_be_visible()
        expect(page.locator("#reset-btn")).to_be_visible()

    def test_form_labels_present(self, page: Page, base_url):
        """Test that form labels are present and correct"""
        page.goto(f"{base_url}/form.html")

        expect(page.locator('label[for="name"]')).to_contain_text("Name")
        expect(page.locator('label[for="email"]')).to_contain_text("Email")
        expect(page.locator('label[for="message"]')).to_contain_text("Message")

    def test_empty_form_submission_shows_errors(self, page: Page, base_url):
        """Test that submitting an empty form shows validation errors"""
        page.goto(f"{base_url}/form.html")

        page.click("#submit-btn")

        # Wait a moment for validation to run
        page.wait_for_timeout(100)

        # Check that error messages are displayed
        expect(page.locator("#name-error")).to_contain_text("required")
        expect(page.locator("#email-error")).to_contain_text("required")
        expect(page.locator("#message-error")).to_contain_text("required")

    def test_invalid_email_shows_error(self, page: Page, base_url):
        """Test that invalid email format shows error"""
        page.goto(f"{base_url}/form.html")

        page.fill("#name", "John Doe")
        page.fill("#email", "invalid-email")
        page.fill("#message", "This is a test message with enough characters")

        page.click("#submit-btn")

        # Wait for validation
        page.wait_for_timeout(100)

        expect(page.locator("#email-error")).to_contain_text("valid email")

    def test_short_name_shows_error(self, page: Page, base_url):
        """Test that a name that's too short shows error"""
        page.goto(f"{base_url}/form.html")

        page.fill("#name", "J")
        page.fill("#email", "john@example.com")
        page.fill("#message", "This is a test message")

        page.click("#submit-btn")

        expect(page.locator("#name-error")).to_contain_text("at least 2 characters")

    def test_short_message_shows_error(self, page: Page, base_url):
        """Test that a message that's too short shows error"""
        page.goto(f"{base_url}/form.html")

        page.fill("#name", "John Doe")
        page.fill("#email", "john@example.com")
        page.fill("#message", "Short")

        page.click("#submit-btn")

        expect(page.locator("#message-error")).to_contain_text("at least 10 characters")

    def test_valid_form_submission_shows_success(self, page: Page, base_url):
        """Test that valid form submission shows success message"""
        page.goto(f"{base_url}/form.html")

        page.fill("#name", "John Doe")
        page.fill("#email", "john@example.com")
        page.fill("#message", "This is a valid test message with enough characters")

        page.click("#submit-btn")

        # Check success message is displayed
        success_message = page.locator("#form-success")
        expect(success_message).to_be_visible()
        expect(success_message).to_contain_text("successfully")

    def test_reset_button_clears_form(self, page: Page, base_url):
        """Test that reset button clears all form fields"""
        page.goto(f"{base_url}/form.html")

        # Fill form
        page.fill("#name", "John Doe")
        page.fill("#email", "john@example.com")
        page.fill("#message", "Test message")

        # Click reset
        page.click("#reset-btn")

        # Check fields are empty
        expect(page.locator("#name")).to_have_value("")
        expect(page.locator("#email")).to_have_value("")
        expect(page.locator("#message")).to_have_value("")

    def test_reset_clears_error_messages(self, page: Page, base_url):
        """Test that reset button clears error messages"""
        page.goto(f"{base_url}/form.html")

        # Submit empty form to trigger errors
        page.click("#submit-btn")

        # Wait for validation
        page.wait_for_timeout(100)

        # Verify errors are shown
        expect(page.locator("#name-error")).not_to_be_empty()

        # Fill and reset
        page.fill("#name", "John")
        page.click("#reset-btn")

        # Check error messages are cleared
        expect(page.locator("#name-error")).to_be_empty()
        expect(page.locator("#email-error")).to_be_empty()
        expect(page.locator("#message-error")).to_be_empty()

    def test_form_submission_clears_form_fields(self, page: Page, base_url):
        """Test that successful submission clears form fields"""
        page.goto(f"{base_url}/form.html")

        page.fill("#name", "John Doe")
        page.fill("#email", "john@example.com")
        page.fill("#message", "This is a valid test message")

        page.click("#submit-btn")

        # Wait for success message
        expect(page.locator("#form-success")).to_be_visible()

        # Check fields are cleared
        expect(page.locator("#name")).to_have_value("")
        expect(page.locator("#email")).to_have_value("")
        expect(page.locator("#message")).to_have_value("")

    def test_form_placeholder_text(self, page: Page, base_url):
        """Test that form fields have appropriate placeholder text"""
        page.goto(f"{base_url}/form.html")

        expect(page.locator("#name")).to_have_attribute("placeholder", "Enter your name")
        expect(page.locator("#email")).to_have_attribute("placeholder", "Enter your email")
        expect(page.locator("#message")).to_have_attribute("placeholder", "Enter your message")
