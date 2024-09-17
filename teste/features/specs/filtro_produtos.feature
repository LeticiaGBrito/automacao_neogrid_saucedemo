Feature: Consulta de preco pelo filtro

Background: 
  Given que estou na tela de lista de produtos

  Scenario: Realizar uma consulta da ordem dos produtos pelo filtro
    When seleciono no filtro a opcao "Price (low to high)"    
    Then lista atualizada e acordo com filtro
