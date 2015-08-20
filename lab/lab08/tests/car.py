test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> roberts_car = Car("Tesla")
          >>> roberts_car.model
          caf8043b86fba6c84a64b1974fae87b2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> roberts_car = Car("Tesla")
          >>> Car.headlights
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> roberts_car.headlights
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Car.headlights = 3
          >>> roberts_car.headlights
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          >>> roberts_car.headlights = 2
          >>> Car.headlights
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> roberts_car = Car("Tesla")
          >>> roberts_car.wheels = 2
          >>> roberts_car.wheels
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Car.num_wheels
          612ff2a71cad53bc4c7f85fac678a06d
          # locked
          >>> roberts_car.drive()
          9239e3f706096ee8d8c5139a537263c2
          # locked
          >>> roberts_car.gas
          2b5c8adf725274c931c4272b26ac97ea
          # locked
          >>> Car.gas
          e0c9124d3360b0721b517ec33d41b017
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}