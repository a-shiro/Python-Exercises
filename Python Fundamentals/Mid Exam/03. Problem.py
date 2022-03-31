shopping_cart = input().split("|")

command = input().split("%")

while not command[0] == "Shop!":
    if command[0] == "Important":
        if not command[1] in shopping_cart:
            shopping_cart.insert(0, command[1])
        else:
            product = shopping_cart.pop(shopping_cart.index(command[1]))
            shopping_cart.insert(0, product)

    elif command[0] == "Add":
        if not command[1] in shopping_cart:
            shopping_cart.append(command[1])
        else:
            print("The product is already in the list.")

    elif command[0] == "Swap":
        if command[1] in shopping_cart and command[2] in shopping_cart:
            index_1 = shopping_cart.index(command[1])
            index_2 = shopping_cart.index(command[2])
            shopping_cart[index_1], shopping_cart[index_2] = shopping_cart[index_2], shopping_cart[index_1]
        else:
            if not command[1] in shopping_cart:
                print(f"Product {command[1]} missing!")
            else:
                print(f"Product {command[2]} missing!")

    elif command[0] == "Remove":
        if command[1] in shopping_cart:
            shopping_cart.remove(command[1])
        else:
            print(f"Product {command[1]} isn't in the list.")

    elif command[0] == "Reversed":
       shopping_cart = shopping_cart[::-1]

    command = input().split("%")

product_position = 0
for product in shopping_cart:
    product_position += 1
    print(f"{product_position}. {product}")