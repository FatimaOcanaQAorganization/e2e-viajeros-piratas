from playwright.sync_api import Page, expect


def abrir_login(page: Page):
    page.goto("https://www.viajerospiratas.es/")

    # Cookies
    page.get_by_role("button", name="Aceptar todo").click()

    # Icono login (hay dos, usamos el primero visible)
    login_icon = page.locator("#hp-login-button").first
    expect(login_icon).to_be_visible()
    login_icon.click()

    # Desktop vs Mobile
    if page.get_by_role("button", name="Ya tengo una cuenta").is_visible():
        page.get_by_role("button", name="Ya tengo una cuenta").click()
    else:
        page.get_by_role("button", name="Iniciar sesión").click()

    # Esperar a que el formulario esté realmente cargado
    expect(page.get_by_placeholder("Email")).to_be_visible(timeout=10000)


def test_login_email_vacio(page: Page):
    abrir_login(page)

    page.get_by_placeholder("Email").fill("")
    page.get_by_placeholder("Contraseña").fill("12345678")
    page.get_by_role("button", name="Continuar").click()

    expect(page.get_by_placeholder("Email")).to_be_visible()


def test_login_email_invalido(page: Page):
    abrir_login(page)

    page.get_by_placeholder("Email").fill("correo-invalido")
    page.get_by_placeholder("Contraseña").fill("12345678")
    page.get_by_role("button", name="Continuar").click()

    expect(page.get_by_placeholder("Email")).to_be_visible()
