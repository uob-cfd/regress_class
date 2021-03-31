test = {
  'name': 'Question multi_residuals',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'multi_residuals'
          >>> 'multi_residuals' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'multi_residuals'
          >>> # from its initial state (of ...)
          >>> multi_residuals is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # There should be one residual for each row in the data frame.
          >>> len(multi_residuals)
          506
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The mean of the residuals should be close to 0.
          >>> np.isclose(np.mean(multi_residuals), 0, atol=0.00001)
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
