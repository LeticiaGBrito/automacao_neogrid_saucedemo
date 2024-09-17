from behave import given, when, then  # pylint: disable=no-name-in-module
from features.pages.adicionar_ao_carrinho_page import CarrinhoComprasPage



@given('que estou na tela inicial') 
def step_given_products_page(context):
      context.adicionar_ao_carrinho_page = CarrinhoComprasPage(context.driver)

@when('adiciono o produto ao carrinho')
def adiciono_produto(context):
    context.adicionar_ao_carrinho_page.adicionando_produto()

@when('verifico se o produto foi adiciono ao carrinho')
def verifico_produto(context):
    context.adicionar_ao_carrinho_page.acessando_carrinho()        


@when('valido o número de itens no carrinho  atualizado')
def validando_carrinho(context):
    assert context.adicionar_ao_carrinho_page.validando_produto_adicionado(), \
        "Nao foi localizado o elemento"
        
@when('clico em Continue Shopping')
def btn_continue_shopping(context):
    context.adicionar_ao_carrinho_page.clicando_em_Continue_Shopping()
   
@when('removo o produto desejado')
def remover_produto_selecionado(context):
    context.adicionar_ao_carrinho_page.removendo_produto_da_lista() 
    
@then('valido que o produto foi removido do carrinho')
def verificando_carrinho(context):
    context.adicionar_ao_carrinho_page.verficando_exclusao_produtos_no_carrinho() 
        
