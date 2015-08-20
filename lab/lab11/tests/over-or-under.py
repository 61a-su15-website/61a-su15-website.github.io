test = {
  'name': 'over-or-under',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (over-or-under 5 5)
          4b569bf0e21d6369c5343767f1146f64
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (over-or-under 5 4)
          94ce22b5936436a75abf185df37ba826
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (over-or-under 3 5)
          3b428da370693317dabdabf6003b84c6
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