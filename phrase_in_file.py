def phrase_finder(phrase, file_path):
    with open(file_path, 'r') as file_content:
        phrase_found = False
        lines = file_content.readlines()

        for row in lines:
            if row.find(phrase) != -1:
                phrase_found = True

        return phrase_found

if __name__ == "__main__":
    print("Insert phrase: ")
    phrase = input()
    print("Insert file path: ")
    file_path = input()
    phrase_found = phrase_finder(phrase, file_path)
    print(phrase_found)
