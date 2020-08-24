def largest(largelist):
    largenumber = largelist[0]
    for i in largelist:
        if i >= largenumber:
            largenumber = i
    return largenumber


random_numbers = [23, 124, 4312, 1, 2]

print(largest(random_numbers))