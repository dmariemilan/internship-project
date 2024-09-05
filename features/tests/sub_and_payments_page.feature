# Created by Owner at 9/3/2024
Feature: Tests for Subscription and payments page
  # Enter feature description here

  Scenario: User can open Subscription and payments page
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on settings option
      And Click on subscription & payments
      Then Verify that url has subscription
      And Verify title Subscription & payments is visible
      And Verify back and upgrade plan buttons are available


