# Created by Velluri at 12/5/2024
Feature: Verify cart is empty

  Scenario: “Your cart is empty”
    Given Open target.com
    When Click on Cart icon
    Then Your cart is empty

  Scenario: "Sign in form opened"
    Given Open target.com
    When Click on Sign in
    Then On navigation menu, click on signin
    Then Verify Sign In form opened


