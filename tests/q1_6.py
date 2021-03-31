test = {
  'name': 'Question r_cr_r_nra',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'r_cr_r_nra'
          >>> 'r_cr_r_nra' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'r_cr_r_nra'
          >>> # from its initial state (of ...)
          >>> r_cr_r_nra is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> -1 <= r_cr_r_nra <= 0
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
