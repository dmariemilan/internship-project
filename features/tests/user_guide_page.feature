# Created by Owner at 9/2/2024
Feature: Test scenarios for user guide page
  # Enter feature description here

  Scenario: User can open User guide page
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on settings option
      And Click on user guide
      Then Verify that url has user-guide
      And Verify all lesson videos contain titles
