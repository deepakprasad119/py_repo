# numCities = 10
# originCities = [1, 2, 3]
# destinationCities = [4, 5, 6]
# threshold = 2


def gcd(a, b):
    # choose the smaller number
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd


# print(gcd(35, 700))


def connectedCities(numCities, threshold, originCities, destinationCities):
    path = []
    for i in range(len(originCities)):
        route = gcd(originCities[i], destinationCities[i])
        if route > threshold:
            path.append(1)
        else:
            path.append(0)

    return path


print(connectedCities(10, 1, [4, 10, 4, 3, 6], [4, 3, 6, 2, 9]))
