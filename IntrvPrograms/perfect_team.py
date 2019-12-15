
#skills = "pcmzpzpmc"

# print("Enter the list of students skills ")
# skill = input()


def perfectTeam(skills):
    ar = sorted(skills)

    #ar_set = sorted(list(set(ar)))
    ar_set = ('b', 'c', 'm', 'p', 'z')
    # print(ar_set)

    skill_dict = dict.fromkeys(ar)
    # print(skill_dict)

    #b, c, m, p, z = 0, 0, 0, 0, 0
    for i in ar_set:
        if i == "b":
            skill_dict["b"] = ar.count(i)
        elif i == "c":
            skill_dict["c"] = ar.count(i)
        elif i == "m":
            skill_dict["m"] = ar.count(i)
        elif i == "p":
            skill_dict["p"] = ar.count(i)
        elif i == "z":
            skill_dict["z"] = ar.count(i)

    # print(skill_dict)

    #print(min(skill_dict, key=skill_dict.get))
    min_key = min(skill_dict, key=skill_dict.get)
    min_value = skill_dict[min_key]
    #print(min_value)

    if int(min_value) == 0:
        #print("no teams can be created")
        return 0
    else:
        #print("number of teams that can be created is =",  min_value)
        return min_value


print(perfectTeam("zpmcb"))
