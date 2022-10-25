def get_hat_count():
    hats = {}

    for dwarf in dwarfs_list:
        if dwarf.hat_color not in hats:
            hats[dwarf.hat_color] = 0
        hats[dwarf.hat_color] += 1

    return hats


def create_dwarf_list():
    while True:
        inp = input()

        if inp == 'Once upon a time':
            break

        name, hat_color, physics = inp.split(' <:> ')
        dwarf = Dwarf(name, hat_color, int(physics))

        if twins(dwarf):
            filter_out_twins(dwarf)
        else:
            dwarfs_list.append(dwarf)


def twins(current_dwarf):
    for dwarf in dwarfs_list:
        if dwarf.name == current_dwarf.name and dwarf.hat_color == current_dwarf.hat_color:
            return True
    return False


def filter_out_twins(current_dwarf):
    for dwarf in dwarfs_list:
        if dwarf.name == current_dwarf.name and dwarf.hat_color == current_dwarf.hat_color:
            if dwarf.physics < current_dwarf.physics:
                dwarfs_list.remove(dwarf)
                dwarfs_list.append(current_dwarf)
                break
            break


class Dwarf:
    def __init__(self, name, hat_color, physics):
        self.name = name
        self.hat_color = hat_color
        self.physics = physics

    def __getitem__(self, index):
        return self.hat_color


dwarfs_list = []
create_dwarf_list()
hats = get_hat_count()

dwarfs_list.sort(key=lambda x: (-int(x.physics), -hats[x[1]]))

for dwarf in dwarfs_list:
    print(f'({dwarf.hat_color}) {dwarf.name} <-> {dwarf.physics}')


