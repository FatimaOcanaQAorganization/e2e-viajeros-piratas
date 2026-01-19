import pytest
from playwright.sync_api import Page


@pytest.mark.parametrize("device_name", ["desktop", "mobile"])
def test_menu_header(page: Page, device_name):

    print(f"\nGIVEN el usuario accede a Viajeros Piratas en {device_name}")

    page.goto("https://www.viajerospiratas.es/")

    print("AND acepta las cookies")
    page.get_by_role("button", name="Aceptar todo").click()
    #bien los enlaces
    enlaces_menu = [
    ("Vacaciones", "https://www.viajerospiratas.es/viajes/vacaciones"),
    ("Chollos", "https://www.viajerospiratas.es/viajes"),
    ("Fin de semana", "https://www.viajerospiratas.es/viajes/fin-de-semana"),
]

    for enlace, url in enlaces_menu:
        #aqui si es movil, hace clic en el menu hamburguesa, si es escritorio simplemente no hace nada porque no tiene que hacer clic en menu hamburguesa
        if device_name == "mobile":
            print("WHEN el usuario abre el menú hamburguesa")
            page.locator("header button").first.click()
        #aqui tanto en movil como en escritorio hacen lo mismo asi que lo dejas fuera del if, simplemente hace click en el enlace y ya.
        print(f"AND hace click en '{enlace}'")
        page.get_by_role("link", name=enlace).first.click(force=True)
        #aqui estas comprobando solo que aparece el boton, pero en realidad debes comprobar que la url cambia entonces quita esto:
        print("THEN el enlace responde correctamente")
        assert page.get_by_role("link", name=enlace).first.is_visible()
        #en su lugar pon esto otro, esperas que carge la url nueva al hacer clic en el menu y luego compruebas que es la esperada
        print("THEN el enlace es el correcto")
        page.wait_for_url(url)
        assert page.url == url
        #esto lo puedes quitar porque no te hace falta volver a la principal ya que los botones del menu siguen visibles en todas las paginas asi que puedes cambiar de uno a otro sin tener que volver a la principal
        print("AND vuelve a la página principal")
        page.goto("https://www.viajerospiratas.es/")
