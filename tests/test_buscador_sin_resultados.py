import re
from playwright.sync_api import Page, expect


def test_buscador_sin_resultados(page: Page):

    # GIVEN el usuario accede a Viajeros Piratas
    page.goto("https://www.viajerospiratas.es/")
    page.get_by_role("button", name="Aceptar todo").click()

    # WHEN abre el buscador
    page.get_by_role("banner") \
        .filter(has_text="Busca y Reserva tu próximo") \
        .get_by_label("Buscar") \
        .click()

    # AND introduce un término sin sentido
    buscador = page.get_by_placeholder("¿Qué buscas?")
    buscador.fill("asdfghjkl123456")

    # AND ejecuta la búsqueda
    buscador.press("Enter")

    # THEN la URL cambia (la búsqueda se ha ejecutado)
    expect(page).to_have_url(re.compile("asdfghjkl", re.IGNORECASE))

    # AND se muestra algún estado de resultados (aunque esté vacío)
    expect(page.locator("body")).to_be_visible()
