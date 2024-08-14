# Created by Owner at 8/9/2024
Feature: Test scenarios for Add a Project page
  # Enter feature description here

  Scenario: User can add a project through the settings
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on settings option
      And Click on Add a project
      Then Verify that url has add-a-project
      And Add some test information to the input fields
      And Verify the right information is present in the input fields
      And Verify Send an application button is available and clickable