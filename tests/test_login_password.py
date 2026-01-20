from playwright.sync_api import Page, expect


def abrir_login(page: Page):
    page.goto("https://www.viajerospiratas.es/")

    # Aceptar cookies
    page.get_by_role("button", name="Aceptar todo").click()

    # Abrir login (hay varios, usamos el primero)
    page.locator("#hp-login-button").first.click()

    # Ir a formulario de login
    page.get_by_role("button", name="Ya tengo una cuenta").click()


def test_login_password_vacia(page: Page):
    abrir_login(page)

    page.get_by_role("textbox", name="Correo electrónico *").fill(
        "test@email.com"
    )

    page.get_by_role("button", name="Continuar").click()

    # El formulario NO avanza
    password_input = page.get_by_role("textbox", name="Contraseña *")
    expect(password_input).to_be_visible()


def test_login_password_corta(page: Page):
    abrir_login(page)

    page.get_by_role("textbox", name="Correo electrónico *").fill(
        "test@email.com"
    )
    page.get_by_role("textbox", name="Contraseña *").fill("123")

    page.get_by_role("button", name="Continuar").click()

    # El formulario NO avanza
    password_input = page.get_by_role("textbox", name="Contraseña *")
    expect(password_input).to_be_visible()
