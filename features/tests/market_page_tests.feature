# Created by Owner at 12/29/2024
Feature: Test Scenarios for Market Page
  # Enter feature description here

  Scenario: User can open market tab and filter by developers option
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on market side option
      Then Verify that URL has market-companies
      And Click on Developers filter at the top of the page
      And Verify all cards have license tag
