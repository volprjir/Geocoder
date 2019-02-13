Feature: Temporary files handling
  Scenario: Negative scenarios

    Given no temporary folders provided
    When clean method is called
    Then the result is False

  Scenario: Positive scenario - counting

    Given not empty directories
    When count method is called
    Then the result is "1"