def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        number_of_words = get_num_words(file_contents)
        characters = get_character_counts(file_contents)
        print(f"{number_of_words} words found in the document")
        for character in characters:
            print(f"The '{character}' character was found {characters[character]} times")
        print("--- End report ---")
        

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    characters = {}
    for i in range(0, len(text)):
        character = text[i].lower()
        if character in characters:
            characters[character] += 1
        else:
            if character.isalpha():
                characters[character] = 1
    return dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))



main()