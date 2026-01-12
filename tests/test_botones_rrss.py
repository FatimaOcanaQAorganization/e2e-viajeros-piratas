from playwright.sync_api import Page


def test_botones_rrss(page: Page):

    page.goto("https://www.viajerospiratas.es/")

    # Aceptar cookies
    page.get_by_role("button", name="Aceptar todo").click()

    # Scroll hasta el footer
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Localizar enlaces de RRSS
    facebook = page.locator("a[href*='facebook']")
    instagram = page.locator("a[href*='instagram']")
    twitter = page.locator("a[href*='twitter'], a[href*='x.com']")

    # Comprobar que existe al menos un enlace de cada red social
    assert facebook.count() > 0
    assert instagram.count() > 0
    assert twitter.count() > 0
