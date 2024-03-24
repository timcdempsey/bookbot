
def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = words_count(text)
    char_dict = chars_count_dict(text)
    report = prepare_report(word_count, char_dict)
    print(f"--- Begin report of {path} ---")
    for line in report:
        print(line)
    print("--- End report ---")

# Used for array sorting.
def sort_on_count(dict):
    return dict["count"]

# Prepares report that gives word count and character count of alphabet characters
# characters are sorted from greatest occurrence to least.
def prepare_report(word_count, char_dict):
    report = []
    report.append(f"{word_count} words have been found in the document.")
    report.append("")
    char_info = []
    for key in char_dict:
        info = {
            "char": key,
            "count": char_dict[key]
        }
        char_info.append(info)
    char_info.sort(key=sort_on_count, reverse=True)
    for info in char_info:
        if str(info["char"]).isalpha():
            report.append(f"The '{info["char"]}' character was found {info["count"]} times")
    return report


# Returns word count of text
def words_count(text):
    words = text.split()
    return len(words)

# Returns dictionary of characters with value of how many times they occurred
def chars_count_dict(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

# Returns text of file provided in path
def get_text(path):
    with open(path) as f:
        return f.read()


main()