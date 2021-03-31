test = {
  'name': 'Question min_result',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'min_result'
          >>> 'min_result' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'min_result'
          >>> # from its initial state (of ...)
          >>> min_result is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # min_result does not have a 'fun' attribute.
          >>> # Have you stored the parameter array instead of the
          >>> # full return value from minimize?
          >>> hasattr(min_result, 'fun')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # min_result.x contains the parameters that minimize
          >>> # the function.  There should be three parameters
          >>> # (intercept, slope_room, slope_stat)
          >>> len(min_result.x)
          3
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
