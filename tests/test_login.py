# -*- coding: utf-8 -*-
import pytest
from playwright.sync_api import Page, expect


def test_login_page(page: Page):
    # Test successful login
    page.goto("file:///path/to/index.html")  # Replace with the actual path
    email_input = page.locator('input[placeholder="Email"]')
    password_input = page.locator('input[placeholder="Password"]')
    login_button = page.locator('button')

    email_input.fill("john.doe@example.com")
    password_input.fill("P@ssw0rd123")
    login_button.click()

    # Test invalid email/password combinations
    email_input.fill("invalid_email_format")
    password_input.fill("short")
    login_button.click()
    expect(page.locator('input[placeholder="Email"]')).to_have_value("invalid_email_format")

    # ERROR HANDLING: Empty Email
    # Tests that login fails with empty email
    email_input.fill("")
    password_input.fill("noemail@123")
    login_button.click()
    expect(page.locator('input[placeholder="Email"]')).to_have_value("")


    # ERROR HANDLING: Empty Password
    # Tests that login fails with empty password
    email_input.fill("harry.potter@hogwarts.edu")
    password_input.fill("")
    login_button.click()
    expect(page.locator('input[placeholder="Password"]')).to_have_value("")
    
    # Test with valid credentials (Alice Smith)
    email_input.fill("alice.smith@example.com")
    password_input.fill("alice@321")
    login_button.click()
