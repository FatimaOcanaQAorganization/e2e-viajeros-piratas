import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("device_name", ["desktop", "mobile"])
def test_menu_header(page: Page, device_name):

    print(f"\nGIVEN el usuario accede a Viajeros Piratas en {device_name}")

    page.goto("https://www.viajerospiratas.es/")

    print("AND acepta las cookies")
    page.get_by_role("button", name="Aceptar todo").click()

    enlaces_menu = [
        ("Vacaciones", "/viajes/vacaciones"),
        ("Chollos", "/viajes"),
        ("Fin de semana", "/viajes/fin-de-semana"),
    ]

    for enlace, expected_path in enlaces_menu:
        print(f"WHEN localiza el enlace '{enlace}'")

        link = page.get_by_role("link", name=enlace).first

        print("THEN el enlace existe")
        expect(link).to_be_visible()

        print("AND el enlace apunta a la URL correcta")
        href = link.get_attribute("href")
        assert expected_path in href
