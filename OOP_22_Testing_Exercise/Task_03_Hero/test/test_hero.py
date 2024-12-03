from project.hero import Hero
from unittest import TestCase, main


class HeroTests(TestCase):
    def setUp(self):
        self.h = Hero("Test", 3, 15.5, 3.5)
        self.enemy = Hero("Enemy", 4, 10, 5)

    def test_init(self):
        self.assertEqual(self.h.username, "Test")
        self.assertEqual(self.h.level, 3)
        self.assertEqual(self.h.health, 15.5)
        self.assertEqual(self.h.damage, 3.5)

    def test_battle_yourself_raises(self):
        self.enemy.username = "Test"
        with self.assertRaises(Exception) as ex:
            result = self.h.battle(self.enemy)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_zero_health_raises(self):
        self.h.health = 0
        with self.assertRaises(Exception) as ex:
            result = self.h.battle(self.enemy)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_less_than_zero_health_raises(self):
        self.h.health = -5
        with self.assertRaises(Exception) as ex:
            result = self.h.battle(self.enemy)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_zero_health_raises(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            result = self.h.battle(self.enemy)
        self.assertEqual(str(ex.exception), "You cannot fight Enemy. He needs to rest")

    def test_battle_enemy_less_than_zero_health_raises(self):
        self.enemy.health = -5
        with self.assertRaises(Exception) as ex:
            result = self.h.battle(self.enemy)
        self.assertEqual(str(ex.exception), "You cannot fight Enemy. He needs to rest")

    def test_both_zero_health_draw(self):
        self.h.damage = 5
        self.h.level = 2
        self.h.health = 15
        self.enemy.damage = 5
        self.enemy.level = 3
        self.enemy.health = 10
        # h damage = 10 -> e health = 10 - 10 = 0
        # e damage = 15 -> h health = 15 - 15 = 0
        result = self.h.battle(self.enemy)
        self.assertEqual(self.h.health, 0)
        self.assertEqual(self.enemy.health, 0)
        self.assertEqual(result, "Draw")

    def test_hero_wins(self):
        self.h.damage = 5
        self.h.level = 2
        self.h.health = 20
        self.enemy.damage = 5
        self.enemy.level = 3
        self.enemy.health = 10
        # h damage = 10 -> e health = 10 - 10 = 0
        # e damage = 15 -> h health = 20 - 15 = 5
        result = self.h.battle(self.enemy)
        self.assertEqual(self.h.health, 10)
        self.assertEqual(self.enemy.health, 0)
        self.assertEqual(result, "You win")
        self.assertEqual(self.h.level, 3)
        self.assertEqual(self.h.health, 10)
        self.assertEqual(self.h.damage, 10)

    def test_hero_loses(self):
        self.h.damage = 5
        self.h.level = 2
        self.h.health = 15
        self.enemy.damage = 5
        self.enemy.level = 3
        self.enemy.health = 20
        # h damage = 10 -> e health = 20 - 10 = 10
        # e damage = 15 -> h health = 15 - 15 = 0
        result = self.h.battle(self.enemy)
        self.assertEqual(self.h.health, 0)
        self.assertEqual(self.enemy.health, 15)
        self.assertEqual(result, "You lose")
        self.assertEqual(self.enemy.level, 4)
        self.assertEqual(self.enemy.health, 15)
        self.assertEqual(self.enemy.damage, 10)

    def test_str(self):
        result = str(self.h)
        expected = f"Hero Test: 3 lvl\n" \
               f"Health: 15.5\n" \
               f"Damage: 3.5\n"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    main()