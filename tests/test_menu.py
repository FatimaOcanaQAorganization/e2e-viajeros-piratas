from playwright.sync_api import Page


def test_menu(page: Page):

    page.goto("https://www.viajerospiratas.es/")

    # Aceptar cookies
    page.get_by_role("button", name="Aceptar todo").click()

    # Enlaces que queremos comprobar
    enlaces_menu = [
        "Vacaciones",
        "Chollos",
        "Fin de semana"
    ]

    for enlace in enlaces_menu:
        page.get_by_role("link", name=enlace).click()

        # Comprobamos que la navegación se realiza
        assert page.url != "https://www.viajerospiratas.es/"

        # Volvemos a la home para probar el siguiente enlace
        page.goto("https://www.viajerospiratas.es/")
from playwright.sync_api import Page


from playwright.sync_api import Page


def test_menu(page: Page):

    print("GIVEN el usuario entra en Viajeros Piratas")
    page.goto("https://www.viajerospiratas.es/")

    print("AND acepta las cookies")
    page.get_by_role("button", name="Aceptar todo").click()

    enlaces_menu = [
        "Vacaciones",
        "Chollos",
        "Fin de semana"
    ]

    for enlace in enlaces_menu:
        print(f"WHEN el usuario hace click en {enlace}")
        page.get_by_role("link", name=enlace).first.click()

        print("THEN la navegación es correcta")
        assert page.url != "https://www.viajerospiratas.es/"

        print("AND vuelve a la página principal")
        page.goto("https://www.viajerospiratas.es/")
