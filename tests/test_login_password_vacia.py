from playwright.sync_api import Page, expect


def test_login_password_vacia(page: Page):

    # GIVEN: el usuario entra en Viajeros Piratas
    page.goto("https://www.viajerospiratas.es")

    # Aceptamos cookies si aparece el banner
    if page.locator("button:has-text('Aceptar')").is_visible():
        page.click("button:has-text('Aceptar')")

    # WHEN: el usuario abre el login
    page.click("a[href*='login'], button:has-text('Iniciar sesión')")

    # Ponemos email valido y no escribimos password
    page.fill("input[type='email']", "fatimaocana695@gmail.com")
    page.fill("input[type='password']", "")

    # Intentamos enviar el formulario
    page.click("button[type='submit']")

    # THEN: comprobamos que el campo password esta vacio(validación HTML)
    password_input = page.locator("input[type='password']")
    expect(password).to_be_visible()



from playwright.sync_api import Page, expect


def test_login_password_vacia(page: Page):

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
    page.get_by_role("textbox", name="Correo electrónico *").fill(
        "fatimaocana695@gmail.com"
    )

    print("AND deja la contraseña vacía")
    password = page.get_by_role("textbox", name="Contraseña *")
    password.fill("")

    print("AND pulsa el botón Continuar")
    page.get_by_role("button", name="Continuar").click()

    print("THEN el formulario no avanza y el campo contraseña sigue visible")
    expect(password).to_be_visible()
