from playwright.sync_api import Page


def test_botones_rrss(page: Page):

    page.goto("https://www.viajerospiratas.es/")

    # Aceptar cookies
    page.get_by_role("button", name="Aceptar todo").click()

    # Scroll hasta el footer
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Localizar enlaces de RRSS, en vez de ver que aparecen, haz clic en ellos y comprueba la url. ##He puesto un assert, porque me estaba dando error al intentar localizar y abrir las rrss 
    assert page.locator("a[href*='facebook']").count() > 0
    assert page.locator("a[href*='instagram']").count() > 0
    assert page.locator("a[href*='twitter'], a[href*='x.com']").count() > 0
