from playwright.sync_api import Page, expect


from playwright.sync_api import Page, expect


def test_email_vacio_login(page: Page):

    print("GIVEN el usuario entra en Viajeros Piratas")
    page.goto("https://www.viajerospiratas.es")

    print("AND acepta las cookies")
    page.get_by_role("button", name="Aceptar todo").click()

    print("WHEN el usuario abre el login")
    page.get_by_role("banner") \
        .filter(has_text="Busca y Reserva tu próximo") \
        .locator("#hp-login-button") \
        .click()

    page.get_by_role("button", name="Ya tengo una cuenta").click()

    print("AND deja el email vacío y rellena solo la contraseña")
    page.get_by_role("textbox", name="Contraseña *").fill("Superotas")

    print("AND pulsa Continuar")
    page.get_by_role("button", name="Continuar").click()

    print("THEN el formulario no avanza y el email sigue visible")
    email = page.get_by_role("textbox", name="Correo electrónico *")
    expect(email).to_be_visible()

