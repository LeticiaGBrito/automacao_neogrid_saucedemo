Feature: Chekout para Finalizar compra 

Background: 
  Given que estou no carrinho de compras para realizar o checkout

  Scenario: Realizar compra
    When clico em checkout
    And preencho os dados com nome "Marina" sobrenome "Silva" e cep "06354158"
    And clico no em continuar
    And finalizo compra     
    Then compra realizada com sucesso