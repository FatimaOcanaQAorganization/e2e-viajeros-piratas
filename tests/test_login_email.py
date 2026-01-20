from playwright.sync_api import Page, expect


def abrir_login(page: Page):
    page.goto("https://www.viajerospiratas.es/")
    page.get_by_role("button", name="Aceptar todo").click()
    page.get_by_role("banner") \
        .filter(has_text="Busca y Reserva tu próximo") \
        .locator("#hp-login-button") \
        .click()
    page.get_by_role("button", name="Ya tengo una cuenta").click()


def test_login_email_vacio(page: Page):
    abrir_login(page)

    # Dejar email vacío, solo contraseña
    page.get_by_role("textbox", name="Contraseña *").fill("123456")
    page.get_by_role("button", name="Continuar").click()

    # El formulario no avanza → el email sigue visible
    email_input = page.get_by_role("textbox", name="Correo electrónico *")
    expect(email_input).to_be_visible()


def test_login_email_invalido(page: Page):
    abrir_login(page)

    # Email inválido
    page.get_by_role("textbox", name="Correo electrónico *").fill("fatima123gmail")
    page.get_by_role("textbox", name="Contraseña *").fill("123456")
    page.get_by_role("button", name="Continuar").click()

    # El navegador bloquea el envío
    email_input = page.get_by_role("textbox", name="Correo electrónico *")
    validation_message = email_input.evaluate("el => el.validationMessage")
    assert validation_message != ""
