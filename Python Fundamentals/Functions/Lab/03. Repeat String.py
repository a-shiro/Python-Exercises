# MY CODE:

def string_plus_string(word,counter):
    answer = ""
    for _ in range(counter):
        answer += word
    return answer

word = input()
counter = int(input())

print(string_plus_string(word,counter))

# OPTIMAL CODE:

# def string_plus_string(word,counter):
#     return word * counter
#
# word = input()
# counter = int(input())
#
# print(string_plus_string(word,counter))
