from random import randint

n_friends = int(input("Enter the number of friends joining (including you):\n"))

if n_friends > 0:
    print("Enter the name of every friend (including you), each on a new line:\n")

    friends = [input() for _ in range(n_friends)]
    len_friends = len(friends)

    print()
    bill = float(input("Enter the total bill value:\n"))
    print()
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    print()
    if lucky == "Yes":
        lucky = friends[randint(0, len_friends - 1)]
        print(f"{lucky} is the lucky one!\n")
        len_friends -= 1
    else:
        print("No one is going to be lucky\n")

    payment = round(bill / len_friends, 2)
    dict_friends = dict.fromkeys(friends, payment)
    if lucky != "No":
        dict_friends[lucky] = 0

    print(dict_friends)

else:
    print("No one is joining for the party\n")
