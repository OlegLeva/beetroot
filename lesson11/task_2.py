def remove_positives(list2):
    result = []
    for i in range(len(list2)):
        if list2[i] < 0:
            result.append(list2[i])
    return result


class Mathematician():
    pass

    def square_nums(self, list1):
        return [i ** 2 for i in list1]

    def filter_leaps(self, list1):
        result = []
        for i in range(len(list1)):
            if list1[i] % 4 == 0:
                result.append(list1[i])
        return result



m = Mathematician()

print(m.square_nums([5, 8, 15, 77]))
print(remove_positives([5, -3, 7, -44, 0]))
print(m.filter_leaps([1980, 1979, 1986, 2000]))
