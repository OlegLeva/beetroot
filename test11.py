from typing import List, Tuple
#1 O(n)
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

print(question1([1,5,66,88],[5,77,96,41]))
#2 O (n²)
def question2(n: int) -> int:
	for n in range(10):
		n **= 3
	return n

print(question2(3))

#3 O(1)
def question3(first_list: List[int], second_list: List[int])-> List[int]:
   temp: List[int] = first_list[:]
   for el_second_list in second_list:
      flag = False
      for check in temp:
         if second_list == check:
            flag = True
            break
      if not flag:
         temp.append(second_list)
   return temp

print(question3([1,5,66,88],[5,77,96,41]))

#4 O(n log n)
def question4(input_list: List[int]) -> int:
  res: int = 0
  for el in input_list:
    if el > res:
      res = el
  return res

print(question4([1,99,66,88]))

#5 O (n²)
def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res

print(question5(4))

#6 O (2 ^ n)
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n

print(question6(999945498864659848457656677525275757575888885765414444555555985))


def merge_sort(data):
    if len(data) <= 1:
        return

    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]

    merge_sort(left_data)
    merge_sort(right_data)

    left_index = 0
    right_index = 0
    data_index = 0

    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1

    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]


if __name__ == '__main__':
    data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    merge_sort(data)
    print(data)