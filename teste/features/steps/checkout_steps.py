from behave import given, when, then  # pylint: disable=no-name-in-module
from features.pages.adicionar_ao_carrinho_page import CarrinhoComprasPage
from features.pages.checkout_page import CheckoutPage

@given('que estou no carrinho de compras para realizar o checkout')
def step_given_products_page(context):
      context.adicionar_ao_carrinho_page = CarrinhoComprasPage(context.driver)
      context.adicionar_ao_carrinho_page.adicionando_produto()
      context.adicionar_ao_carrinho_page.acessando_carrinho() 
      context.checkout_page = CheckoutPage(context.driver)
      
@when('clico em checkout')
def button_checkout(context):
    context.checkout_page.clicando_em_checkout()  
    
@when('preencho os dados com nome "{nome}" sobrenome "{sobrenome}" e cep "{cep}"')
def preencho_dados(context, nome, sobrenome, cep):
    context.checkout_page.realizando_cadastro(nome, sobrenome, cep)  
    
    
@when('clico no em continuar')
def button_continuar(context):
    context.checkout_page.clicando_em_continue()  

@when('finalizo compra')
def finalizar_compra(context):
    context.checkout_page.finalizando_compra()    
    
@then('compra realizada com sucesso')
def valido_compra(context): 
   assert context.checkout_page.validando_compra_finalizada(), \
       "Nao foi localizado o elemento"

    