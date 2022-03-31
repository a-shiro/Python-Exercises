from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team('Team')

    def test_constructor(self):
        self.assertEqual('Team', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_raises_error_when_is_not_isalpha(self):
        with self.assertRaises(ValueError) as cm:
            self.team.name = 'Team1'
        self.assertEqual('Team Name can contain only letters!', str(cm.exception))

    def test_name_setter_sets_name_correctly(self):
        self.team.name = 'TeamOne'
        self.assertEqual('TeamOne', self.team.name)

    def test_add_member_adds_member_successfully(self):
        self.team.members = {}

        result = self.team.add_member(John=5)

        self.assertEqual({'John': 5}, self.team.members)
        self.assertEqual('Successfully added: John', result)

    def test_remove_member_if_member_is_not_in_team(self): # 1 test works
        result = self.team.remove_member('Maria')
        self.assertEqual('Member with name Maria does not exist', result)

    def test_remove_member_if_member_is_in_team(self): # 2 tests work
        self.team.members = {'John': 5}
        result = self.team.remove_member('John')

        self.assertEqual({}, self.team.members)
        self.assertEqual('Member John removed', result)

    def test_magic_gt_method_returns_correct_results(self): # 1 test works
        other_team = Team('TeamTwo')
        other_team.members = {'John': 1}

        self.assertEqual(True, other_team > self.team)
        self.assertEqual(False,self.team > other_team)

    def test_magic_len_method_returns_count_of_members(self): # 1 test works
        self.team.members = {'John': 1}
        result = len(self.team)
        self.assertEqual(1, result)

    def test_magic_add_method(self): # 2 tests work
        self.team.members = {'Maria': 1}

        other_team = Team('TeamTwo')
        other_team.members = {'John': 1}

        new_team = self.team + other_team

        self.assertEqual('TeamTeamTwo', new_team.name)
        self.assertEqual({'Maria': 1, 'John': 1}, new_team.members)

    def test_magic_str_method(self): # 2 tests work
        self.team.members = {'Maria': 1, 'John': 2}
        result = str(self.team)
        self.assertEqual(f'Team name: Team' + '\n' 'Member: John - 2-years old' + '\n' + 'Member: Maria - 1-years old', result)


if __name__ == '__main__':
    main()
