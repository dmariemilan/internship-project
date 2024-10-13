# Created by Owner at 9/28/2024
Feature: Test Scenarios for Support (Whatsapp) and News (Telegram) pages


  Scenario: Uer can access Whatsapp and Telegram Communities
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on settings option
      And Click on support
      And Switch to new window
      Then Verify that url has api.whatsapp.com
      And Switch back to Settings page
      And Click on news
      And Verify that url has t.me
