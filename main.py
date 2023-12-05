import requests
from bs4 import BeautifulSoup
import json

def tokenize_subtitle(subtitle):
    words_list = []
    # Tokenize the subtitle into words
    for sub in subtitle:
        words = sub.split()
        words_list.append(words)
    return words_list


def find_and_print_next_line(file_path):
    content = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

        finded = False
        for i in range(len(lines)):
            line = lines[i].strip()

            # Ensure there is a next line
            if finded:
                content.append(line)
                finded = False

            # Check if the current line contains the symbol -->
            if "-->" in line:
                finded = True
    return content


def search_word_definition(word):
    # Prepare the Google search URL for word definition
    search_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    # Send a request to Google
    response = requests.get(search_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        data = json.loads(soup.text)

        return True, data[0]
    else:
        return False, f"Failed to retrieve definition. Status code: {response.status_code}"


def extract_info(word_info):
    # Extract information about the word "hello"
    word = word_info["word"]
    phonetic = word_info["phonetic"]
    meanings = word_info["meanings"]

    # Print the information
    print(f"Word: {word}")
    print(f"Phonetic: {phonetic}")

    # Print meanings
    for meaning in meanings:
        part_of_speech = meaning["partOfSpeech"]
        definitions = meaning["definitions"]

        print(f"\nPart of Speech: {part_of_speech}")

        for definition in definitions:
            meaning_def = definition["definition"] if "definition" in definition else "N/A"
            example = definition["example"] if "example" in definition else "N/A"

            print(f"  Definition: {meaning_def}")
            print(f"  Example: {example}")


def main():
    # # Example subtitle
    # subtitle = "This is an example subtitle. Tokenize it!"
    path = "Poker.face.2023.S01E05.srt"
    subtitle = find_and_print_next_line(path)
    # Tokenize the subtitle
    words = tokenize_subtitle(subtitle[2:])

    # TODO: Add GUI to check the word you want to check the dictionary
    # # Search for the meaning of each word
    # for word in words:
    #     status, definition = search_word_definition(word)
    #     print(f"Word: {word}")
    #     if status:
    #         extract_info(definition)
    #     else:
    #         print(f"{definition}")
    #     print("---------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
