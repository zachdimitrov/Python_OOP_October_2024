from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class SoccerPlayerTests(TestCase):
    def setUp(self):
        self.s = SoccerPlayer("Testplayer", 20, 10, "Barcelona")
        self._VALID_TEAMS = ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"]

    def test_init(self):
        self.assertEqual("Testplayer", self.s.name)
        self.assertEqual(20, self.s.age)
        self.assertEqual(10, self.s.goals)
        self.assertEqual("Barcelona", self.s.team)
        self.assertEqual({}, self.s.achievements)

    def test_name_too_short_raises(self):
        with self.assertRaises(Exception) as ex:
            self.s.name = "T"
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

    def test_name_setter(self):
        self.s.name = "Testtest"
        self.assertEqual("Testtest", self.s.name)

    def test_age_too_low_raises(self):
        with self.assertRaises(Exception) as ex:
            self.s.age = 10
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

    def test_age_setter(self):
        self.s.age = 30
        self.assertEqual(30, self.s.age)

    def test_team_not_valid_raises(self):
        with self.assertRaises(Exception) as ex:
            self.s.team = "CSKA"
        self.assertEqual(f"Team must be one of the following: {', '.join(self._VALID_TEAMS)}!", str(ex.exception))

    def test_team_setter(self):
        self.s.team = "PSG"
        self.assertEqual("PSG", self.s.team)

    def test_change_team_not_valid(self):
        result = self.s.change_team("CSKA")
        self.assertEqual(f"Invalid team name!", result)

    def test_change_team(self):
        result = self.s.change_team("Manchester United")
        self.assertEqual("Team successfully changed!", result)

    def test_add_achievement(self):
        self.assertEqual({}, self.s.achievements)
        result = self.s.add_new_achievement("Goals")
        self.assertEqual("Goals has been successfully added to the achievements collection!", result)
        self.assertEqual({"Goals": 1}, self.s.achievements)
        self.s.add_new_achievement("Goals")
        self.assertEqual({"Goals": 2}, self.s.achievements)

    def test_less_than_if_more(self):
        other = SoccerPlayer("HasLessGoals", 20, 5, "PSG")
        result = self.s < other
        self.assertEqual("Testplayer is a better goal scorer than HasLessGoals.", result)

    def test_less_than_if_less(self):
        other = SoccerPlayer("HasMoreGoals", 20, 25, "PSG")
        result = self.s < other
        self.assertEqual("HasMoreGoals is a top goal scorer! S/he scored more than Testplayer.", result)


if __name__ == "__main__":
    main()
