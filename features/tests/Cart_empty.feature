# Created by Velluri at 12/22/2024
Feature: “Your cart is empty” message is shown for empty cart

  Scenario: “Your cart is empty”
  Given Open the home page for Cart
  When Click on Cart icon button
  Then Verify “Your cart is empty” message
