from playwright.sync_api import Page


def test_botones_rrss(page: Page):

    page.goto("https://www.viajerospiratas.es/")

    # Aceptar cookies
    page.get_by_role("button", name="Aceptar todo").click()

    # Scroll hasta el footer
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Localizar enlaces de RRSS, en vez de ver que aparecen, haz clic en ellos y comprueba la url
    facebook = page.locator("a[href*='facebook']")
    instagram = page.locator("a[href*='instagram']")
    twitter = page.locator("a[href*='twitter'], a[href*='x.com']")

    # Haz clic en el enlace de la red social y comprueba que se abre la url correcta
    facebook.first.click()
    page.wait_for_url("https://www.facebook.com/viajerospiratas/")
  # luego vuelve a la pagina principal y haz click en el siguiente enlace para comprobar lo mismo
    page.goto("https://www.viajerospiratas.es/")
    instagram.first.click()
    page.wait_for_url("https://www.instagram.com/viajerospiratas/")
    # luego vuelve a la pagina principal y haz click en el siguiente enlace para comprobar lo mismo
    page.goto("https://www.viajerospiratas.es/")
    twitter.first.click()
    page.wait_for_url("https://www.twitter.com/viajerospiratas/")
