# Created by Owner at 8/14/2024
Feature: Test scenarios for Community Page
  # Enter feature description here

  Scenario: User can open the community page
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on settings option
      And Click on Community
      Then Verify that url has community
      And Verify Contact support button is available and clickable