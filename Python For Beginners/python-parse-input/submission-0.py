from typing import List

def read_integers() -> List[int]:
    string_input = input()
    list_of_strings = string_input.split(",")
    list_of_int = []

    for s in list_of_strings:
        list_of_int.append(int(s))
    return list_of_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
