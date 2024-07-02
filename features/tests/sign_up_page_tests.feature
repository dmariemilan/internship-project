# Created by Owner at 6/28/2024
Feature: Test scenarios for sign up page functionality
  # Enter feature description here

  Scenario: The user can enter the information into the input fields on the registration page
      Given Open Reelly sign up page
      When Input a name and phone number
      And Input an email and password
      And Input a company name
      Then Verify input name is correct
      And Verify phone number is correct
      And Verify email is correct
      And Verify password is correct
      And Verify company name is correct

