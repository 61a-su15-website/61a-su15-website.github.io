# Pokemon with inheritance

class Pokemon:
    "Pokemon base class"

    def __init__(self, owner):
        self.owner = owner
        self.hp = 10

class Pikachu(Pokemon):
    "Pikachu is a species of Pokemon"

    def attack(self, other):
        "Attacks the other Pokemon if pikachu has positive hp"
        if self.hp <= 0:
            return
        print('Pikachu used '
              'thunder!')
        other.hp -= 5

class Squirtle(Pokemon):
    "Squirtle is a species of Pokemon"

    def attack(self, other):
        "Attacks the other Pokemon if pikachu has positive hp"
        if self.hp <= 0:
            return
        print('Squirtle used '
              'bubble beam!')
        other.hp -= 3

def inheritance():
    pika = Pikachu('Mike')
    squirt = Squirtle('Molly')
    pika.owner
    squirt.owner
    pika.attack(squirt)
    squirt.attack(pika)
    pika.hp
    squirt.hp

# Cleaner Pokemon implementation

class Pokemon:
    """General Pokemon superclass"""

    name = None
    damage = 0
    attack_name = None

    def __init__(self, owner):
        self.owner = owner
        self.hp = 10

    def attack(self, other):
        """Attack other pokemon is self has HP left."""
        if self.hp <= 0:
            print(self.name + 'is too tired.')
        else:
            print('{} used {}!'.format(self.name, self.attack_name))
            other.hp -= self.damage

class Pikachu(Pokemon):
    """Pikachu is a species of Pokemon"""
    name = 'Pikachu'
    damage = 5
    attack_name = 'thunder'

class Squirtle(Pokemon):
    """Squirtle is a species of Pokemon"""
    name = 'Squirtle'
    damage = 3
    attack_name = 'water gun'

# Method overriding

class Zubat(Pokemon):
    """Zubat is a species of Pokemon with a special attack"""
    name = 'Zubat'
    damage = 2
    attack_name = 'leech life'

    def attack(self, other):
        Pokemon.attack(self, other)
        if self.hp > 0:
            bonus = self.damage // 2
            self.hp += bonus
            print('{} gained {} hp.'.format(self.name, bonus))

def zubat():
    zuzu = Zubat('Sarah')
    squirt = Squirtle('Sam')
    zuzu.attack(squirt)
    zuzu.hp
    squirt.hp

# Exceptions

def errors():
    abs('hello') # TypeError
    hello # NameError
    {}['hello'] # KeyError
    def f(): f()
    f() # RuntimeError

class MyBadError(Exception):
    pass

def assert_eq():
    assert 0 == 1, 'Math broke!'

def raise_error():
    raise MyBadError('Aw shucks!')

def exception_handling_1():
    try:
        1 / 0
        print("Won't print")
    except ZeroDivisionError as err:
        print("Yay! Stopped:", err)

def zip(seq1, seq2):
    """
    >>> zip([1, 2, 3], [4, 5, 6])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [[seq1[i], seq2[i]] for i in range(len(seq1))]

def exception_handling_2():
    try:
        zip([1, 2, 3], [4, 5])
    except ZeroDivisionError as err:
        print(type(err))
    except IndexError as err:
        print(type(err))
