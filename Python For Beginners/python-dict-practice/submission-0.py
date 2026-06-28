from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    character_dict = {}
    for character in word:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict
            




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
