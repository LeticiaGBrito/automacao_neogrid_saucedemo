#login.feature

Feature: Realizar Login    
  Como usuario necessito acessar o site
  Quero realiazar o login
  Para realizar compra de produtos disponiveis
 

Scenario: Login com credenciais validas
  Given que estou na pagina de login
  When inserir as credenciais "standard_user" e senha "secret_sauce"
  And clicar no botao login
  Then valido que o login foi realizado com sucesso

 
# @login.invalido
# Cenario:Login com credenciais invalidas
#   Dado que estou na pagina de login
#   Quando inserir as credenciais "standard_user123" e senha  "secret_sauce123"
#   E clicar no botao login
#   Entao valido a mensagem de erro na tela de login