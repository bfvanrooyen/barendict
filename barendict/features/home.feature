Feature: Home page
  As a user
  I want to be able to visit the home page
  So that I can view information

  Scenario: Visit barendict home page

    Given A user

    When The user visits http://www.barendict.com

    Then The home page will load