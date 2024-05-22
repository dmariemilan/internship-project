# Created by Owner at 4/11/2024
Feature: Search tests

  Scenario: User can search for coffee
    Given Open Target main page
    When Search for coffee
    Then Verify search results are shown for coffee
    Then Verify that url has coffee

  Scenario: User can search for tea
    Given Open Target main page
    When Search for tea
    Then Verify search results are shown for tea
    Then Verify that url has tea

  Scenario: Verify that user can see product names and images
    Given Open Target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image