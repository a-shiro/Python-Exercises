def characters_between(char_1,char_2):
    list = []
    for character in range(ord(char_1) + 1, ord(char_2)):
        list.append(chr(character))
    return list

char_1 = input()
char_2 = input()

string = characters_between(char_1,char_2)

print(" ".join(string))