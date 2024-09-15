def match_pattern(input_line, pattern):
    "check if the pattern matches with the input sent"
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\d":
        for char in input_line:
            if char.isdigit():
                return True
        return False
    elif pattern == "\w":
        for char in input_line:
            if char.isalnum():
                return True
        return False
    elif pattern[0] == '[' and pattern[-1] == "]":
        characters_to_check = list(pattern.replace("[", "").replace("]", ""))
        if characters_to_check[0] == "^":
            characters_to_check.pop(0)
            for char_check in characters_to_check:
                if char_check in input_line:
                    return False
            return True
        for char_check in characters_to_check:
            if char_check in input_line:
                return True
        return False
    # check the amount of digits in front of the pattern but don't check for words
    elif ("\d" in pattern) and ("\w" not in pattern) and (len(pattern) > 2):
        # get the number of digits we need to check
        digits_count = pattern.split(" ")[0].count("\d")
        # text pattern to match
        text = pattern.split(" ")[1]

        # if text does not exist in the input line then return False
        if text not in input_line:
            return False

        # if the word exists, check if the word has a digit in front of it
        input_list = input_line.split(" ")

        # if len of the input list is less than 2 then there is no digit in front of the text
        if len(input_list) < 2:
            return False

        for index in range(len(input_list)):
            if text in input_list[index]:
                # if index is zero there is no digit in front of it
                if index == 0:
                    return False

                # check if the text in front is a digit
                if (input_list[index - 1].isnumeric()) and (len(input_list[index - 1]) == digits_count):
                    return True
        return False
    # check the amount of digits in front of the pattern but check for words as well
    elif ("\d" in pattern) and ("\w" in pattern) and (len(pattern) > 2):
        digits_count = pattern.split(" ")[0].count("\d")
        words_pattern = pattern.split(" ")[1]

        # if the word exists, check if the word has a digit in front of it
        input_list = input_line.split(" ")

        # if len of the input list is less than 2 then there is no digit in front of the text
        if len(input_list) < 2:
            return False

        for index in range(len(input_list)):
            # check if the word is a digit
            if input_list[index].isnumeric():
                # return false if this is the last word in the list as no word will follow
                if index == len(input_list) - 1:
                    return False

                # check if the digit length matches the pattern
                if len(input_list[index]) != digits_count:
                    return False

                # if the pattern for word is just to check \w occurence
                if words_pattern.count("\w") == len(words_pattern):
                    # just check if the length of the input word matches this
                    if input_list[index + 1] != words_pattern.count("\w"):
                        return False
                    return True
                else:
                    # fetch the pattern after the word count length
                    text_after_pattern = words_pattern.replace("\w", "")
                    if (input_list[index + 1].endswith(text_after_pattern)) and (len(input_list[index + 1]) == (words_pattern.count("\w") + len(text_after_pattern))) and (input_list[index + 1][:len(words_pattern)].isalpha()):
                        return True
        return False
    elif pattern.startswith("^"):
        # check if the input string startes with the given pattern
        pattern_word = pattern.replace("^", "")
        if input_line.startswith(pattern_word):
            return True
        return False
    elif pattern.endswith("$"):
        # check if the string ends with the given pattern
        pattern_word = pattern.replace("$", "")
        if input_line.endswith(pattern_word):
            return True
        return False
    elif "+" in pattern:
        # split the pattern with +
        pattern_list = pattern.split("+")
        print("pattern_list: ", pattern_list)

        # if length of the pattern list is 1, then check if the word starts or ends with the particular string
        if len(pattern_list) < 2:
            if pattern.startswith("+"):
                return input_line.endswith(pattern.replace("+", ""))
            if pattern.endswith("+"):
                return input_line.startswith(pattern.replace("+", ""))
        elif len(pattern_list) == 2:
            if (pattern_list[0] not in input_line) or (pattern_list[1] not in input_line):
                return False
            # split using the first pattern and check if the other pattern is in the second half
            input_split = input_line.split(pattern_list[0])
            if len(input_split) < 1:
                # second pattern does not exist after the first pattern
                return False
            if len(input_split) == 1:
                if pattern_list[1] in input_split[0]:
                    return True
                return False
            if pattern_list[1] in input_split[1]:
                return True
            return False
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")

print("match_pattern: ", match_pattern("caaats", "ca+t"))
