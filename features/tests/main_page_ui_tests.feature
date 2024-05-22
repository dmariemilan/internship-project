# Created by Owner at 4/16/2024
Feature: Tests for main page UI

  Scenario: Verify header in shown
    Given Open Target main page
    Then Verify header in shown


  Scenario: Verify header has correct amount of links
    Given Open Target main page
    Then Verify header has 6 links
  # since our last class, Target has changed their links and now has 7 on the right side