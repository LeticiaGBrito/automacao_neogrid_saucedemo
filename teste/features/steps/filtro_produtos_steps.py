# from behave import given, when, then  # pylint: disable=no-name-in-module
from behave import given, when, then
from features.pages.filtro_produtos_page import FiltroProdutosPage

@given('que estou na tela de lista de produtos')
def step_given_products_page(context):
    context.filtro_produtos_page = FiltroProdutosPage(context.driver)

@when('seleciono no filtro a opcao "{opcao}"')
def opcao_filtro(context, opcao):
    context.filtro_produtos_page.selecionando_tipo_do_filtro(opcao)

@then('lista atualizada e acordo com filtro')
def validar_ordenacao_precos(context):
    context.filtro_produtos_page.verificar_ordenacao_precos_na_lista()

    
    
 