# Created by Owner at 7/9/2024
Feature: Test scenarios for settings page functionality and UI


  Scenario: User can go to setting and see the right number of UI elements
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on settings option
      Then Verify that URL has settings
      And Verify page has 12 options
      Then Verify connect the company button present

