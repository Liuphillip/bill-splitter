import random

people_dict = {} # dictionary Key: people in party, Value: amount they are each paying
bill_value = 0 # total bill value
arr = [] # contains the names of the people in the party
lucky = '' # lucky person choice. String: ('yes'/'no')

people = int(input("Enter the number of friends joining (including you):"))

if people < 1:
    print("No one is joining for the party")
else:
    for _ in range(people):
        value = input("Enter the name of every friend (including you), each on a new line:")
        arr.append(value)

    # get total bill value
    bill_value = int(input("Enter the total bill value"))

    # determine if user wants to use who-is-lucky feature
    lucky = input('Do you want to use "Who is Lucky" feature? Write Yes/No')

    if lucky.lower() == 'yes':
        picked = random.choice(arr)
        print(f'{picked} is the lucky one!')

        # initialize dictionary with 0.0 as all values being a float, and keys being the names of people in arr
        people_dict = {key: 0.0 for key in arr}

        # split the value of the bill and round to the nearest 2 decimal places
        split_value = round(bill_value / (len(arr) - 1), 2)

        # replace values in people dict to value of split_value
        for key in people_dict:
            if key == picked:
                continue
            people_dict[key] = split_value

        # print the dictionary if there are people in the party.
        if people > 0:
            print(people_dict)


    else:
        print("No one is going to be lucky")

        # initialize dictionary with 0.0 as all values being float, and keys being the names of people in arr
        people_dict = {key: 0.0 for key in arr}

        # split the value of the bill and round to the nearest 2 decimal places
        split_value = round(bill_value / len(arr), 2)

        # replace values in people dict to value of split_value
        for key in people_dict:
            people_dict[key] = split_value

        # print the dictionary if there are people in the party.
        if people > 0:
            print(people_dict)