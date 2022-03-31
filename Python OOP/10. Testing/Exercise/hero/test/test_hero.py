from unittest import TestCase, main
from project import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Hero1', 1, 100, 10)
        self.enemy = Hero('Enemy1', 1, 100, 10)

    def test_initializer(self):
        self.assertEqual('Hero1', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_str_of_of_the_obj_returns_correct_string(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        result = str(self.hero)
        self.assertEqual(expected, result)

    def test_the_opponent_of_hero_if_with_the_same_name_raises_error(self):
        opponent = Hero('Hero1', 10, 1000, 100)
        self.assertEqual(opponent.username, self.hero.username)

        with self.assertRaises(Exception) as cm:
            self.hero.battle(opponent)
        self.assertEqual('You cannot fight yourself', str(cm.exception))

    def test_hero_tries_to_battle_with_zero_or_less_health_raises_error(self):
        for health in [0, -1]:
            self.hero.health = health

            with self.assertRaises(ValueError) as cm:
                self.hero.battle(self.enemy)
            self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(cm.exception))

    def test_hero_tries_to_battle_enemy_with_zero_or_less_health_raises_error(self):
        for health in [0, -1]:
            self.enemy.health = health

            with self.assertRaises(ValueError) as cm:
                self.hero.battle(self.enemy)
            self.assertEqual('You cannot fight Enemy1. He needs to rest', str(cm.exception))

    def test_hero_battles_enemy_and_they_draw(self):
        self.hero.health = 10
        self.enemy.health = 10
        self.hero.level, self.hero.damage = 1, 10
        self.enemy.level, self.enemy.damage = 1, 10

        battle_result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual('Draw', battle_result)

    def test_hero_wins_after_the_battle(self):
        self.hero.health = 20
        self.enemy.health = 10
        self.hero.level, self.hero.damage = 1, 10
        self.enemy.level, self.enemy.damage = 1, 10

        battle_result = self.hero.battle(self.enemy)

        self.assertEqual(1 + 1, self.hero.level)
        self.assertEqual(10 + 5, self.hero.health)
        self.assertEqual(10 + 5, self.hero.damage)
        self.assertEqual('You win', battle_result)

    def test_enemy_wins_after_the_battle(self):
        self.hero.health = 10
        self.enemy.health = 20
        self.hero.level, self.hero.damage = 1, 10
        self.enemy.level, self.enemy.damage = 1, 10

        battle_result = self.hero.battle(self.enemy)

        self.assertEqual(1 + 1, self.enemy.level)
        self.assertEqual(10 + 5, self.enemy.health)
        self.assertEqual(10 + 5, self.enemy.damage)
        self.assertEqual('You lose', battle_result)


if __name__ == '__main__':
    main()