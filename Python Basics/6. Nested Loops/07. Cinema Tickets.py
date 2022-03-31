command = input()

student_ticket = 0
standard_ticket = 0
kid_ticket = 0

while command != "Finish":

    seats = int(input())
    ticket_type = input()
    tickets_sold = 0
    while seats > tickets_sold:

        tickets_sold += 1
        if ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1

        if tickets_sold == seats:
            break
        ticket_type = input()

        if ticket_type == "End":
            break

    print(f"{command} - {tickets_sold / seats * 100:.2f}% full.")

    command = input()

total_tickets = student_ticket + standard_ticket + kid_ticket

print(f"Total tickets: {total_tickets}")
print(f"{student_ticket / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_ticket / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_ticket / total_tickets * 100:.2f}% kids tickets.")