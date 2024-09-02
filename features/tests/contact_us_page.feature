# Created by Owner at 8/30/2024
Feature: Test scenarios for contact us page
  # Enter feature description here

  Scenario: User can open the contact us page
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on settings option
      And Click on contact us
      Then Verify that url has contact-us
      And Verify there are at least 4 social media icons
      And Verify Connect the company button is available and clickable