from playwright.sync_api import Page, expect


def test_login_password_vacia(page: Page):

    # GIVEN el usuario entra en Viajeros Piratas
    page.goto("https://www.viajerospiratas.es/")

    # Aceptamos cookies
    if page.locator("button:has-text('Aceptar todo')").is_visible():
        page.click("button:has-text('Aceptar todo')")

    # WHEN el usuario abre el login
    page.get_by_role("banner") \
        .filter(has_text="Busca y Reserva tu próximo") \
        .locator("#hp-login-button") \
        .click()

    page.get_by_role("button", name="Ya tengo una cuenta").click()

    # Ponemos email válido y password corta
    page.get_by_role("textbox", name="Correo electrónico *") \
        .fill("fatimaocana695@gmail.com")

    password_input = page.get_by_role("textbox", name="Contraseña *")
    password_input.fill("12")

    # Intentamos enviar el formulario
    page.get_by_role("button", name="Continuar").click()

    # THEN comprobamos que el formulario no avanza
    expect(password_input).to_be_visible()

from playwright.sync_api import Page, expect


def test_login_password_corta(page: Page):

    print("GIVEN el usuario accede a Viajeros Piratas")
    page.goto("https://www.viajerospiratas.es/")

    print("AND acepta las cookies")
    page.get_by_role("button", name="Aceptar todo").click()

    print("WHEN el usuario abre el formulario de login")
    page.get_by_role("banner") \
        .filter(has_text="Busca y Reserva tu próximo") \
        .locator("#hp-login-button") \
        .click()

    page.get_by_role("button", name="Ya tengo una cuenta").click()

    print("AND introduce un email válido")
    page.get_by_role("textbox", name="Correo electrónico *") \
        .fill("fatimaocana695@gmail.com")

    print("AND introduce una contraseña demasiado corta")
    password = page.get_by_role("textbox", name="Contraseña *")
    password.fill("12")

    print("AND pulsa el botón Continuar")
    page.get_by_role("button", name="Continuar").click()

    print("THEN el formulario no avanza y el campo contraseña sigue visible")
    expect(password).to_be_visible()

