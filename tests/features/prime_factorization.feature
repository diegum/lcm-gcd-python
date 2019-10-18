Feature: Prime factorization
  For every number there's a series possibly empty of prime factors whose product is such number.


  Scenario Outline: Prime factorization
    Given a <number>
    When submitted to prime factorization
    Then it generates its <prime_factors>

    Examples:
    |    number | prime_factors                                 |
    |         0 | []                                            |
    |         1 | []                                            |
    |         2 | [2]                                           |
    |         3 | [3]                                           |
    |         4 | [2, 2]                                        |
    |         5 | [5]                                           |
    |         6 | [2, 3]                                        |
    |         7 | [7]                                           |
    |         8 | [2, 2, 2]                                     |
    |         9 | [3, 3]                                        |
    |        10 | [2, 5]                                        |
    |        11 | [11]                                          |
    |        12 | [2, 2, 3]                                     |
    |        13 | [13]                                          |
    |        14 | [2, 7]                                        |
    |        15 | [3, 5]                                        |
    |        16 | [2, 2, 2, 2]                                  |
    |        17 | [17]                                          |
    |        18 | [2, 3, 3]                                     |
    |        19 | [19]                                          |
    |        20 | [2, 2, 5]                                     |
    |      1000 | [2, 2, 2, 5, 5, 5]                            |
    |     32767 | [7, 31, 151]                                  |
    |     32768 | [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] |
    |     32771 | [32771]                                       |
    | 123456789 | [3, 3, 3607, 3803]                            |
    | 987654321 | [3, 3, 17, 17, 379721]                        |
