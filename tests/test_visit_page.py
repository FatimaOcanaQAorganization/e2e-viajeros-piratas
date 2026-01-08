from playwright.sync_api import Page, expect

def test_visit(page: Page):
    print("Given user visit homepage")
    page.goto("https://www.viajerospiratas.es/")

    
    

