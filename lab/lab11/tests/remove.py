test = {
  'name': 'remove',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (remove 3 nil)
          c02484be4076814f723f27f111ca2044
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 2 '(1 3 2))
          1747242d7745a0e0e94092d738ddb8ee
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 1 '(1 3 2))
          2d8fb84a568ddcee05a856e3f5f3f23b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 42 '(1 3 2))
          eb29d0c193582d7dcee57743694af59c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 3 '(1 3 3 7))
          2e7e0a84905453be8250ab5da4b567ce
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