from behave import given, when, then  # pylint: disable=no-name-in-module
from features.pages.login_page import LoginPage

@given('que estou na pagina de login')
def step_given_que_estou_na_pagina_de_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.acessando_tela_de_login()

@when('inserir as credenciais "{usuario}" e senha "{senha}"')
def step_when_inserir_as_credenciais(context, usuario, senha):
    context.login_page.informando_credenciais_login(usuario, senha)

@when('clicar no botao login')
def step_when_clicar_no_botao_login(context):
    context.login_page.clicando_no_botao_login()

@then('valido que o login foi realizado com sucesso')
def step_then_valido_login(context):
    assert context.login_page.validar_tela_inicial(), "Não foi localizado o elemento"
