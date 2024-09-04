# Created by Owner at 9/3/2024
Feature: Test scenarios for change password page
  # Enter feature description here

  Scenario: User can open change password page
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on settings option
      And Click on change password
      Then Verify that url has set-new-password
      And Add some test password to the input fields
      And Verify the change password button is available

