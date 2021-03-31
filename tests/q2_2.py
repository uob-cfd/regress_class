test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(train_movements) == num_train
          True
          >>> len(test_movements) + num_train == num_movements
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
