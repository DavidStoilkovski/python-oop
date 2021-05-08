from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = 'Hero1'
    health = 100.00
    damage = 20.00
    level = 12

    enemy_username = 'Enemy'
    enemy_health = 240
    enemy_damage = 10.00
    enemy_level = 10

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)
        self.enemy = Hero(self.enemy_username, self.enemy_level, self.enemy_health, self.enemy_damage)

    def test_initialize_correct_values(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)
        self.assertEqual(self.level, self.hero.level)

    def test_can_not_fight_yourself(self):
        with self.assertRaises(Exception):
            self.hero.battle(self.hero)

    def test_can_not_fight_when_hero_health_is_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError):
            self.hero.battle(self.enemy)

        # self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_can_not_fight_when_enemy_health_is_zero(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError):
            self.hero.battle(self.enemy)

        # self.assertEqual(f"You cannot fight {self.enemy_username}. He needs to rest", str(ex.exception))

    def test_hero_and_enemy_health_is_zero(self):
        self.assertEqual('Draw', self.hero.battle(self.enemy))

    def test_hero_wins_after_battle_and_values_increase(self):
        self.hero.health += 100

        self.assertEqual('You win', self.hero.battle(self.enemy))
        self.assertEqual(self.level + 1, self.hero.level)
        self.assertEqual(self.health + 5, self.hero.health)
        self.assertEqual(self.damage + 5, self.hero.damage)

        self.assertTrue(self.enemy.health <= 0)

    def test_enemy_wins_after_battle_and_values_increase(self):
        self.enemy.health += 240

        self.assertEqual('You lose', self.hero.battle(self.enemy))
        self.assertEqual(self.enemy_level + 1, self.enemy.level)
        self.assertEqual(self.enemy_health + 5, self.enemy.health)
        self.assertEqual(self.enemy_damage + 5, self.enemy.damage)

        self.assertTrue(self.hero.health <= 0)

    def test_hero_string_representation(self):
        self.assertEqual(f"Hero {self.username}: {self.level} lvl\nHealth: {self.health}\nDamage: {self.damage}\n",
                         self.hero.__str__())

    def test_enemy_string_representation(self):
        self.assertEqual(
            f"Hero {self.enemy_username}: {self.enemy_level} lvl\nHealth: {self.enemy_health}\nDamage: {self.enemy_damage}\n",
            self.enemy.__str__())


if __name__ == '__main__':
    main()
