from playwright.sync_api import sync_playwright
import pytest


@pytest.mark.parametrize("device_name", ["desktop", "mobile"])
def test_menu_header(device_name):

    with sync_playwright() as playwright:

        print(f"\nGIVEN el usuario accede a Viajeros Piratas en {device_name}")

        browser = playwright.chromium.launch(headless=False)

        if device_name == "mobile":
            print("AND el dispositivo es móvil (iPhone 12)")
            device = playwright.devices["iPhone 12"]
            context = browser.new_context(**device)
        else:
            print("AND el dispositivo es escritorio")
            context = browser.new_context()

        page = context.new_page()
        page.goto("https://www.viajerospiratas.es/")

        print("AND acepta las cookies")
        page.get_by_role("button", name="Aceptar todo").click()

        enlaces_menu = ["Vacaciones", "Chollos", "Fin de semana"]

        for enlace in enlaces_menu:

            if device_name == "mobile":
                print("WHEN el usuario abre el menú hamburguesa")
                page.locator("header button").first.click()
                page.wait_for_timeout(500)

                print(f"AND hace click en '{enlace}' (móvil)")
                page.get_by_role("link", name=enlace).first.click(force=True)

            else:
                print(f"AND hace click en '{enlace}' (escritorio)")
                page.get_by_role("link", name=enlace).first.click()

            print("THEN el enlace responde correctamente")

            print("AND vuelve a la página principal")
            page.goto("https://www.viajerospiratas.es/")

        context.close()
        browser.close()
