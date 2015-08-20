test = {
  'name': 'Time check',
  'points': 0,
  'suites': [
    {
      'type': 'doctest',
      'setup': """
      >>> from hog import *
      """,
      'cases': [
        {
          'code': """
          >>> for i in range(100):
          ...    for j in range(100):
          ...        assert -1 <= final_strategy(i, j) <= 10
          """,
          'locked': False,
        },
      ]
    }
  ]
}
