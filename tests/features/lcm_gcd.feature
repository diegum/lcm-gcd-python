Feature: Least common multiple (LCM) and Greatest common divisor (GCD)
  Every pair of numbers have an LCM and a GCD.


  Scenario Outline: LCM and GCD
    Given <a> and <b> integers
    When LCM & GCD are calculated
    Then they are respectively equivalent to <lcm> and <gcd>

    Examples:
    |    a    |    b    |        lcm       |        gcd       |
    |  12345  |  54321  |     223530915    |         3        |
    |987654321|123456789| 13548070123626141|         9        |
    |    1    |    1    |         1        |         1        |
    |   15    |   15    |        15        |        15        |
    |   15    |   30    |        30        |        15        |
    |   15    |   31    |        465       |         1        |