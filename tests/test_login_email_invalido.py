from playwright.sync_api import Page, expect


def test_login_email_invalido(page: Page):

    # GIVEN: el usuario entra en Viajeros Piratas
    page.goto("https://www.viajerospiratas.es")

    # Aceptamos cookies si aparece el banner
    if page.locator("button:has-text('Aceptar')").is_visible():
        page.click("button:has-text('Aceptar')")

    # WHEN: el usuario abre el login
    page.click("a[href*='login'], button:has-text('Iniciar sesión')")

    # Ponemos email invalido y escribimos password
    page.fill("input[type='email']", "")
    page.fill("input[type='password']", "password123")

    # Intentamos enviar el formulario
    page.click("button[type='submit']")

    # THEN: comprobamos que el email es incorrecto (validación HTML)
    email_input = page.locator("input[type='email']")
    expect(email_input).to_be_visible()

    from playwright.sync_api import Page

def test_login_email_invalido(page: Page):

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

    print("AND introduce un email con formato inválido")
    email = page.get_by_role("textbox", name="Correo electrónico *")
    email.fill("fatima5t6gmail")

    print("AND introduce una contraseña válida")
    page.get_by_role("textbox", name="Contraseña *").fill("12345")

    print("AND pulsa el botón Continuar")
    page.get_by_role("button", name="Continuar").click()

    print("THEN el navegador bloquea el envío por email inválido")
    validation_message = email.evaluate("el => el.validationMessage")
    assert validation_message != ""
