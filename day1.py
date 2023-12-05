
def get_number(ln: str):
    word_number_dict = {
        "zero": '0',
        "zero"[::-1]: '0',
        "one": '1',
        "one"[::-1]: '1',
        "two": '2',
        "two"[::-1]: '2',
        "three": '3',
        "three"[::-1]: '3',
        "four": '4',
        "four"[::-1]: '4',
        "five": '5',
        "five"[::-1]: '5',
        "six": '6',
        "six"[::-1]: '6',
        "seven": '7',
        "seven"[::-1]: '7',
        "eight": '8',
        "eight"[::-1]: '8',
        "nine": '9',
        "nine"[::-1]: '9',
    }
    for i, ch in enumerate(ln):
        if ch.isdigit():
            return ch
        else:
            for word, digit in word_number_dict.items():
                found_word = ln[i:i+len(word)]
                print(f"i:{i}, {word} == {found_word}, len:{len(word)}")
                if word == found_word:
                    print(f"returning {digit}")
                    return digit


with open("./day1_part2input.txt") as infile:
    sum = 0
    for line in infile.readlines():
        line=line.replace("\n", "")
        first_digit = get_number(line)
        last_digit = get_number(line[::-1])
        print(f"{first_digit}{last_digit}")
        sum += int(f"{first_digit}{last_digit}")
        print(f"sum: {sum}")