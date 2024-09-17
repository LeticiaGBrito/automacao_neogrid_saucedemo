class Elements:
    
    # Login 
    USERNAME =  "user-name"
    PASSWORD = "password"
    LOGIN_BUTTON = "login-button"
    SELECT_TEXT_01= "//span[@data-test='title']"  
    
    
    
    #Produto  carrinho
    ADD_PRODUTO_01 = "add-to-cart-sauce-labs-backpack"
    ADD_PRODUTO_02  = "add-to-cart-sauce-labs-onesie"
    CARRINHO = "//a[@data-test='shopping-cart-link']"
    SELECT_TEXT_02 = "//span[@data-test='title' and text()='Your Cart']"
    BUTTON_CONTINUE = "continue-shopping"
    REMOVE_PRODUTO_01 = "//button[@data-test='remove-sauce-labs-backpack']"
    REMOVE_PRODUTO_02  = "//button[@data-test='remove-sauce-labs-onesie']"
    
    

    #Checkout page elements
    CHECKOUT_BUTTON = "checkout"
    FIRST_NAME_INPUT = "first-name"
    LAST_NAME_INPUT = "last-name"
    POSTAL_CODE_INPUT = "postal-code"
    CONTINUE_BUTTON = "continue"
    FINISH_BUTTON = "finish"
    SELECT_TEXT_03 = "//h2[@class='complete-header' and @data-test='complete-header' and text()='Thank you for your order!']"


    #filtro page elements      
    SELECT_FILTRO = "select[data-test='product-sort-container']"
    LISTA_ITENS =  ".inventory_item_price"
    SELEC_PRECO_MENOR = "//*[contains(text(), '7.99')]"
    SELEC_PRECO_MAIOR = "//*[contains(text(), '49.99')]"
    
    