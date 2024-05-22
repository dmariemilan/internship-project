# Created by Owner at 4/6/2024
Feature: Test Scenarios for SignIn Functionality
  # Enter feature description here

  Scenario: Logged out user is able to signin
      Given Open Target main page
      When Click sign in from top navigation
      When Click sign in from side navigation menu
      Then Verify Sign into your Target account is displayed

  Scenario: User is able to open and close Terms and Conditions
     Given Open Target main page
      When Click sign in from top navigation
      When Click sign in from side navigation menu
      And Store original window
      When Click Terms and Conditions Link
      And Switch to new window
      Then Verify Terms and Conditions page opened
      And Close current page
      And Return to original window