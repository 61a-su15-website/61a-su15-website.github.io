test = {
  'name': 'filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter even? '(1 2 3 4))
          0a183800d4fe74ae89831116eeb77142
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter odd? '(1 3 5))
          f1ae8fe0f0648e509095cd872251ddd7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter odd? '(2 4 6 1))
          0ef86a453a3a12bb52a4391170792be2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter even? '(3))
          c02484be4076814f723f27f111ca2044
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter odd? nil)
          c02484be4076814f723f27f111ca2044
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab11)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}