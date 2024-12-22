# Created by Velluri at 12/11/2024
Feature: Tests for search

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search results shown for tea

  Scenario: Open target circle page
    Given Open target circle page
    Then Verify there are 14 benefit cells

  Scenario: Add Target’s product into the cart
    Given Open target main page
    When Search for Joker
    And Add the toy to cart
    And Decline protection
    Then I should see the product in my cart
    Then Can see the total price
