tickets = [t.strip() for t in input().split(",") if not t.isspace()]

symbol_left = ""
symbol_right = ""

for ticket in tickets:

    if len(ticket) == 20: # IF WORKS
        if "@" in ticket or "#" in ticket or "$" in ticket or "^" in ticket: # IF WORKS

            left_half = ticket[:10]
            right_half = ticket[10:]

            continuous_in_left = 0
            for i in range(len(left_half)):
                if left_half[i] == "@" or left_half[i] == "#" or left_half[i] == "$" or left_half[i] == "^":
                    symbol_left = left_half[i]
                    continuous_in_left += 1
                    if i + 1 in range(len(left_half)):
                        next_el = left_half[i + 1]
                        if not next_el == left_half[i]:
                            break

            continuous_in_right = 0
            for j in range(len(right_half)):
                if right_half[j] == "@" or right_half[j] == "#" or right_half[j] == "$" or right_half[j] == "^":
                    symbol_right = right_half[j]
                    continuous_in_right += 1
                    if j + 1 in range(len(right_half)):
                        next_el = right_half[j + 1]
                        if not next_el == right_half[j]:
                            break

            if continuous_in_left == continuous_in_right and symbol_left == symbol_right:
                if continuous_in_left == 10 and continuous_in_right == 10:
                    print(f'ticket "{ticket}" - {continuous_in_left}{symbol_left} Jackpot!')

                elif continuous_in_left >= 6:
                    print(f'ticket "{ticket}" - {continuous_in_left}{symbol_left}')
        else: # ELSE WORKS
            print(f'ticket "{ticket}" - no match')
    else: # ELSE WORKS
        print("invalid ticket")

# asd$$$$$asasd$$$$$as    # checks if both sides are equal but are not enough to print

   # validticketnomatch:(,   asd$$$$$asasd$$$$$as, sd ,     $$$$$$$$$$$$$$$$$$$$