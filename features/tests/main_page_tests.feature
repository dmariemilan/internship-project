# Created by Owner at 5/29/2024
Feature: Test scenarios for main page functionality
  # Enter feature description here

  Scenario: Verify that user can click on 'Connect the company' on the left side of the main page
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on Connect the company
      And Switch to new window
      Then Verify that url has book-presentation

  @mobile
  Scenario: Verify MOBILE user can click on 'Connect the company' on the left side of the main page
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on Mobile Menu button
      And Click on Mobile Connect the company
      And Switch to new window
      Then Verify that url has book-presentation

  Scenario: User can filter the off plan products by Unit price range
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on off plan side option
      Then Verify that URL has soft.reelly
      And Click on off plan Filter
      And Filter the products by price range from 1200000 to 2000000 AED
      And Click on off plan Apply Filter
      And Verify the price in all cards is in the range (1200000 - 2000000)

  Scenario: User can see titles and pictures on each product inside the off plan page
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on off plan side option
      Then Verify that URL has soft.reelly
      And Verify each product on the page contains a title and a picture

  Scenario: User can filter by sales status Out of Stocks
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on off plan side option
      Then Verify that URL has soft.reelly
      And Click on sales status filter
      And Click on out of stock
      And Verify all cards have Out of stock tag








