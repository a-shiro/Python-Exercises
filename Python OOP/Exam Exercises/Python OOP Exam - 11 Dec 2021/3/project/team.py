from typing import Dict


class Team:
    def __init__(self, name: str): # 1
        self.name = name
        self.members: Dict[str, int] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value): # 2
        if not value.isalpha(): # 1
            raise ValueError("Team Name can contain only letters!")
        self.__name = value # 1

    def add_member(self, **name_age): # 1
        added_members_by_name = []
        for name, age in name_age.items():
            if name not in self.members:
                self.members[name] = age
                added_members_by_name.append(name) # test list output
        return f"Successfully added: {', '.join(added_members_by_name)}" # test str output

    def remove_member(self, name: str): # 2
        if name in self.members:
            del self.members[name]
            return f"Member {name} removed" # 1
        else:
            return f"Member with name {name} does not exist" # 1

    def __gt__(self, other):  # "other" is another instance of class Team! # 2
        if len(self.members) > len(other.members):
            return True # 1
        return False # 1

    def __len__(self): # 1
        return len(self.members)

    def __add__(self, other):  # "other" is another instance of class Team!
        new_team_name = f"{self.name}{other.name}"
        new_team = Team(new_team_name)
        new_team.add_member(**self.members)
        new_team.add_member(**other.members)
        return new_team # 1

    def __str__(self): #
        result = [f"Team name: {self.name}"]
        members = list(sorted(self.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        return "\n".join(result)


team = Team('T')
team.add_member(john=3)
team2 = Team('TTwo')

print(team2 > team)