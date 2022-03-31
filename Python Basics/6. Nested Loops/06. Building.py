number_floors = int(input())
number_rooms = int(input())

for i in range(number_floors, 0, -1):
     for j in range(0, number_rooms):
         if i == number_floors:
             print(f"L{i}{j}", end = " ")

         elif i % 2 == 0:
             print(f"O{i}{j}", end = " ")

         elif i % 2 != 0:
             print(f"A{i}{j}", end = " ")

     print()
