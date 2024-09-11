BOOK = "books/frankenstein.txt"

def main():
    with open(BOOK) as f:
        file_contents = f.read()
        print(f"--- Begin the report of {BOOK} ---")
        print(f"{count_words(file_contents)} words found in the document")
        dict = count_characters(file_contents)
        chars = characters_to_character_list(dict)
        chars.sort(reverse=True, key=sort_on)
        for char in chars:
            print(f"The {char["name"]} character was found {char["num"]} times")
        print("--- End Report ---")
    

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    characters = {}
    for character in lowered_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def characters_to_character_list(dict):
    character_list = []
    for item in dict:
        if item.isalpha():
            character_list.append({"name": item, "num": dict[item]})
    return character_list

def sort_on(dict):
    return dict["num"]


main()