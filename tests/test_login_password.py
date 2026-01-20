from playwright.sync_api import Page, expect


def abrir_login(page: Page):
    page.goto("https://www.viajerospiratas.es/")

    page.get_by_role("button", name="Aceptar todo").click()

    login_icon = page.locator("#hp-login-button").first
    expect(login_icon).to_be_visible()
    login_icon.click()

    if page.get_by_role("button", name="Ya tengo una cuenta").is_visible():
        page.get_by_role("button", name="Ya tengo una cuenta").click()
    else:
        page.get_by_role("button", name="Iniciar sesión").click()

    expect(page.get_by_placeholder("Email")).to_be_visible(timeout=10000)


def test_login_password_vacia(page: Page):
    abrir_login(page)

    page.get_by_placeholder("Email").fill("test@test.com")
    page.get_by_placeholder("Contraseña").fill("")
    page.get_by_role("button", name="Continuar").click()

    expect(page.get_by_placeholder("Contraseña")).to_be_visible()


def test_login_password_corta(page: Page):
    abrir_login(page)

    page.get_by_placeholder("Email").fill("test@test.com")
    page.get_by_placeholder("Contraseña").fill("123")
    page.get_by_role("button", name="Continuar").click()

    expect(page.get_by_placeholder("Contraseña")).to_be_visible()
