# Created by Owner at 5/29/2024
Feature: Test scenarios for main page functionality
  # Enter feature description here

  Scenario: Verify that user can click on 'Connect the company' on the left side of the main page
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on Connect the company
      And Switch to new window
      Then Verify that url has book-presentation

    # Enter steps here