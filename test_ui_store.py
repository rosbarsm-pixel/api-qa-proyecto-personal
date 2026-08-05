from playwright.sync_api import Page, expect

def test_flujo_de_compra_exitoso(page: Page):
    
    # 1. Navegar a la tienda demo para las pruebas
    page.goto("https://www.saucedemo.com/")

    # 2. INICIO DE SESIÓN
    # Se localizan los cuadros de texto por su ID (usando el símbolo #)
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    
    # Clic en el botón de login
    page.locator("#login-button").click()

    # 3. VALIDACIÓN 1
    # Se  verifica que que el título "Products" aparezca en la pantalla.
    expect(page.locator(".title")).to_have_text("Products")

    # 4. AGREGAR AL CARRITO
    # Clic en el botón para agregar la mochila (Backpack)
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    # 5. IR AL CARRITO Y VALIDAR
    # Clic en el ícono del carrito en la esquina superior derecha
    page.locator(".shopping_cart_link").click()
    
    # VALIDACIÓN 2: Se verifica que la mochila realmente esté dentro del carrito
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")