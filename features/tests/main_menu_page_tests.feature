# Created by Owner at 8/7/2024
Feature: Test scenarios for main menu page functionality
  # Enter feature description here

  Scenario: User can change the language from the page to Russian
    Given Open Reelly main page
    When Input user email and password and sign in
    And Click on Main menu option
    And Change the language of the page to Russian
    Then Verify the language has changed


