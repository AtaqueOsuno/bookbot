def main():
    num_char = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_list = list(file_contents)
        for i in char_list:
            i = i.lower()
            if i in num_char:
                num_char[i] += 1
            else:
                num_char.update({i:1})
        print("--- Begin report of books/frankenstein.txt ---")

    for i in num_char:
        if i.isalpha():
            print(f"The '{i}' character was found {num_char[i]} times")






main()
