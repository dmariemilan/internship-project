# Created by Owner at 10/18/2024
Feature: Test Scenarios for Secondary Page


  Scenario: User can open the Secondary deals page and go through the pagination
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on Secondary option
      Then Verify that URL has secondary-listings
      And Go to the final page using the pagination button
      And Go back to the first page using the pagination button

  Scenario: User can filter the Secondary deals by 'want to sell' option
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on Secondary option
      Then Verify that URL has secondary-listings
      And Click on Filters
      And Filter the products by want to sell
      And Click on Apply Filter
      And Verify all cards have for sale tag

