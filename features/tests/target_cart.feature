# Created by Owner at 4/5/2024
Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for coffee
    And Click on Add to Cart button
    And Store product name
    And Click Add to Cart button from side navigation
    And Click on view cart & and check out
    Then Verify cart has 1 item(s)
    And Verify cart has correct product



      # Enter steps here