import re
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

    # Ejecutar búsqueda con ENTER
    buscador.press("Enter")

    # Comprobación correcta: la URL contiene "roma"
    expect(page).to_have_url(re.compile("roma", re.IGNORECASE))
