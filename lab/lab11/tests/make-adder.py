test = {
  'name': 'make-adder',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add-two 2)
          3cfd97a152be55d1a3486dbacb2bf637
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add-two 3)
          9934e055a74f1f7f5fb94c0f9fd6402d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add-three 3)
          71dc1c0558e41b2d6d30fd9795b4fb1f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add-three 9)
          9eff0ca700216024c3e3ce67d10b784a
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab11)
      scm> (define add-two (make-adder 2))
      scm> (define add-three (make-adder 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}