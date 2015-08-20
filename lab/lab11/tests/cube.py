test = {
  'name': 'cube',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cube 2)
          403f02fd254a4c6524542453898124b4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cube 3)
          572e0aedd0161bb92a0a12d572d6130e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cube 1)
          94ce22b5936436a75abf185df37ba826
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