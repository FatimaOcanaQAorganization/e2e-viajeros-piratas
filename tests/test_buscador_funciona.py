from playwright.sync_api import Page, expect


def test_buscador_funciona(page: Page):

    page.goto("https://www.viajerospiratas.es/")

    # Aceptar cookies
    page.get_by_role("button", name="Aceptar todo").click()

    # Abrir buscador
    page.get_by_role("banner") \
        .filter(has_text="Busca y Reserva tu próximo") \
        .get_by_label("Buscar") \
        .click()

    # Escribir búsqueda
    buscador = page.get_by_placeholder("¿Qué buscas?")
    buscador.fill("Roma")

    # Ejecutar búsqueda con ENTER (NO CLICK)
    buscador.press("Enter")

    # Comprobación: no compruebes que no esta en la home, sino que cuando buscas roma te aparece la url de resultados de roma, si estas haciendo busqueda valida, la url debe ser valida
    expect(page).to_have_url("https://www.viajerospiratas.es/busqueda/roma")


# todo esto esta doble lo puedes borrar
from playwright.sync_api import Page, expect

from playwright.sync_api import Page, expect


def test_buscador_funciona(page: Page):

    print("GIVEN el usuario accede a Viajeros Piratas")
    page.goto("https://www.viajerospiratas.es/")

    print("AND acepta las cookies")
    page.get_by_role("button", name="Aceptar todo").click()

    print("WHEN el usuario abre el buscador")
    page.get_by_role("banner") \
        .filter(has_text="Busca y Reserva tu próximo") \
        .get_by_label("Buscar") \
        .click()

    print("AND introduce un término de búsqueda")
    buscador = page.get_by_placeholder("¿Qué buscas?")
    buscador.fill("Roma")

    print("AND ejecuta la búsqueda pulsando Enter")
    buscador.press("Enter")

    print("THEN la página cambia y se muestran resultados")
    expect(page).not_to_have_url("https://www.viajerospiratas.es/")
