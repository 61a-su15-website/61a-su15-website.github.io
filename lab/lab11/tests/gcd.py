test = {
  'name': 'gcd',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (gcd 0 4)
          3cfd97a152be55d1a3486dbacb2bf637
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 8 0)
          403f02fd254a4c6524542453898124b4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 34 19)
          94ce22b5936436a75abf185df37ba826
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 39 91)
          1e6d9050d0895ed14d21c5460caf6739
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 20 30)
          994cc386b9ac20ceafc06b188d1ee65b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 40 40)
          4e7f353f68fcaf1f15859df0f207faab
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