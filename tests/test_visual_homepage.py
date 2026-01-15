from playwright.sync_api import Page, expect

def test_visual_homepage(page: Page, assert_snapshot):
    print("Given user visit homepage")
    page.goto("https://www.viajerospiratas.es/")

    #comprueba la captura de pantalla se muestre tal y como este
    assert_snapshot(page.screenshot())