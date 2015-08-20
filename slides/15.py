class Pokemon:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 5 * self.level
        self.damage = 2 * self.level

    def talk(self):
        print(self.name + '!')

    def level_up(self):
        self.level += 1
        self.hp = 5 * self.level
        self.damage = 2 * self.level

    def decrease_hp(self, amount):
        """Decreases this Pokemon's hp by amount.
        HP cannot go below 0.

        >>> pikachu = Pokemon('pikachu')
        >>> pikachu.hp
        5
        >>> pikachu.decrease_hp(3)
        >>> pikachu.hp
        2
        >>> pikachu.decrease_hp(100)
        >>> pikachu.hp
        0
        """
        "*** YOUR CODE HERE ***"
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def attack(self, other):
        """Prints out "<name> attacks <other name>"
        decreases other Pokemon's hp by self.damage.

        >>> pikachu = Pokemon('pikachu')
        >>> jigglypuff = Pokemon('jigglypuff')
        >>> pikachu.damage
        2
        >>> jigglypuff.hp
        5
        >>> pikachu.attack(jigglypuff)
        pikachu attacks jigglypuff
        >>> jigglypuff.hp
        3
        """
        "*** YOUR CODE HERE ***"
        print(self.name + ' attacks ' + other.name)
        other.decrease_hp(self.damage)


