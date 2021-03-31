test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 36000 <= sum(calc_residuals(boston,
          ...                             'crime_rate',
          ...                             'median_home_value')**2) <= 37000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> my_df = pd.DataFrame()
          >>> my_df['x'] = [1, 2, 3, 4]
          >>> my_df['y'] = [5, 6, 10, 12]
          >>> my_residuals = calc_residuals(my_df, 'x', 'y')
          >>> # Oh dear - are you using "input_df" in your function,
          >>> # or are you accidentally using "boston" directly?
          >>> len(my_residuals) != len(boston)
          True
          >>> len(my_residuals) == 4
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
