from typing import Dict, Set
import functools

f = open("resources/0079_keylog.txt")
inputs = f.readlines()


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.data = data


number_to_precedents_map: Dict[int, Set[int]] = {}
all_numbers = set()

def compare(n1: int, n2: int):
    return 1 if n2 in number_to_precedents_map[n1] else -1

for numbers in inputs:
    ordered_numbers = list(map(int, list(numbers[:-1])))
    all_numbers.update(ordered_numbers)
    for i in range(0, len(ordered_numbers)):
        number = ordered_numbers[i]
        precedents = ordered_numbers[:i]
        num_map = number_to_precedents_map.setdefault(number, set())
        num_map.update(precedents)

sorted_list = sorted(list(all_numbers) )
sorted_list.sort(key=functools.cmp_to_key(compare))

print(''.join(map(str, sorted_list)))