def count_words(text):
    word_count = len(text.split())
    return word_count

def get_character_count(text):
    lowercase_text = text.lower()
    characters = {}
    for i in lowercase_text:
        if i.isalpha():
            if i in characters:
                characters[i] += 1
            else:
                characters[i] = 1
    return characters

def generate_book_report(file_path, word_count, character_count):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    for key in character_count:
        print(f"The {key} character was found {character_count[key]} times")
    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        book_contents = f.read()

    num_words = count_words(book_contents)
    character_count = get_character_count(book_contents)
    generate_book_report(path_to_file,num_words,character_count)



if __name__ == "__main__":
    main()


