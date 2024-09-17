Feature: Adicionar e Remover Produto ao Carrinho

Background: 
  Given que estou na tela inicial

  Scenario: Adicionar produto ao carrinho com sucesso e remover o produto selecionado
    When adiciono o produto ao carrinho  
    And verifico se o produto foi adiciono ao carrinho
    And valido o número de itens no carrinho  atualizado
    And clico em Continue Shopping        
    And removo o produto desejado  
    Then valido que o produto foi removido do carrinho
