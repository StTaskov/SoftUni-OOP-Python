import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Pesho", 1, 100, 20)
        self.enemy = Hero("Dragan", 1, 100, 20)

    def test_init_work(self):
        self.assertEqual(self.hero.username, 'Pesho')
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 20)

    def test_battle_with_yourself_raises(self):
        Pesho = Hero("Pesho", 1, 20, 3)
        Enemy = Hero("Pesho", 2, 15, 6)
        with self.assertRaises(Exception) as ex:
            Pesho.battle(Enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_our_hp_less_than_zero(self):
        Pesho = Hero("Pesho", 1, -5, 20)
        with self.assertRaises(ValueError) as ex:
            Pesho.battle(self.enemy)
        self.assertEqual(str(ex.exception),
                             "Your health is lower than or equal to 0. You need to rest")

    def test_enemy_hp_less_than_zero(self):
        Dragan = Hero("Dragan", 1, 0, 20)
        evil_name = "Dragan"
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(Dragan)
        self.assertEqual(str(ex.exception),
                             f"You cannot fight {evil_name}. He needs to rest")

    def test_battle_draw(self):
        Pesho = Hero("Pesho", 1, 5, 20)
        Dragan = Hero("Dragan", 1, 5, 20)
        result = Pesho.battle(Dragan)
        expected_r = "Draw"
        self.assertEqual(result, expected_r)

    def test_Pesho_win_battle(self):
        Pesho = Hero("Pesho", 1, 100, 20)
        Dragan = Hero("Dragan", 1, 5, 20)
        result = Pesho.battle(Dragan)
        expected_r = "You win"
        self.assertEqual(result, expected_r)
        self.assertEqual(2, Pesho.level)
        self.assertEqual(85, Pesho.health)
        self.assertEqual(25, Pesho.damage)

    def test_Pesho_lose_battle(self):
        Pesho = Hero("Pesho", 1, 5, 20)
        Dragan = Hero("Dragan", 1, 100, 20)
        result = Pesho.battle(Dragan)
        expected_r = "You lose"
        self.assertEqual(result, expected_r)
        self.assertEqual(2, Dragan.level)
        self.assertEqual(85, Dragan.health)
        self.assertEqual(25, Dragan.damage)

    def test_str(self):
        username = self.hero.username
        lvl = self.hero.level
        health = self.hero.health
        damage = self.hero.damage
        result = f"Hero {username}: {lvl} lvl\nHealth: {health}\nDamage: {damage}\n"
        expected_r = str(self.hero)
        self.assertEqual(result, expected_r)


if __name__ == '__main__':
    unittest.main()