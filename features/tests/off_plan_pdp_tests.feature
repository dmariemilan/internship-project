# Created by Owner at 12/29/2024
Feature: Test Scenarios for off plan (Main Page) PDP


  Scenario: User can open product detail and see three options of visualization
      Given Open Reelly main page
      When Input user email and password and sign in
      And Click on off plan side option
      And Click on the first product
      Then Verify the three options of visualization are 'architecture', 'interior', 'lobby'
      And Verify the visualization options are clickable

