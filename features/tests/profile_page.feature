# Created by Owner at 7/24/2024
Feature: Test scenarios for profile edit page
  # Enter feature description here

  Scenario: User can go to settings and edit the personal information
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on settings option
      And Click on Edit profile
      And Enter test data into the name field: Test Tester
      And Enter test data into the phone number field: 555 555 5555
      And Enter test data into the company field: Testing
      And Enter test data into the email field: test@tester.com
      Then Verify the correct information is present in the name input field
      And Verify the correct information is present in the phone number input field
      And Verify the correct information is present in th company input field
      And Verify the correct information is present in the email input field
      And Check "Save Changes" button is available and clickable
      And Check "Close" button is available and clickable
