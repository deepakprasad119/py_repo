

# <h1> Basic Programs

# <h2> Remove duplicates from a list

# <h5> sol1
    test_list = [2, 4, 10, 20, 5, 2, 20, 4]


    def Remove(test_list):
        final_test_list = []
        for num in test_list:
            if num not in final_test_list:
                final_test_list.append(num)
        return final_test_list


    print(Remove(test_list))


# <h5> sol2 - converting into set


    test_list = [2, 4, 10, 20, 5, 2, 20, 4]

    A = list(set(test_list))
    print(A)



# <h5> sol3 - converting into dictionary

    mylist = ["a", "b", "a", "c", "c"]
    mylist = list( dict.fromkeys(mylist) )      #using list elements as keys for dictionary
    print(mylist)



# <h2> find factorial of a number



    print("Enter a number:")

    num = int(input())

    f = 1

    if f < 0:
        print("Factorial does'nt exist for negative number.")
    elif f == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, 1 + num):
            # print(i)
            f = f * i
        print("Factorial of {} is {}".format(num, f))


# <h2> python program for simple interest



    #python program to find simple interest

    print("Enter the principal amount:")
    p = int(input())

    print("Enter the tenure:")
    t = int(input())

    print("Enter the rate of interest:")
    r = int(input())

    SI = int((p * t * r) / 100)

    print("Simple Interest is {}".format(SI))

