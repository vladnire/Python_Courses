import string

def get_key_to_letters():
    possible_letters = string.ascii_lowercase
    possible_keys = string.digits
    key_to_letters = {}
    start_index = 0

    for key in possible_keys:   
        if key == "0":
            key_to_letters[key] = " "
        elif key == "1":
            key_to_letters[key] = ""
        else:
            num_letters = 3
            if key in {"7", "9"}:
                num_letters = 4
            letters = possible_letters[start_index:start_index + num_letters]
            key_to_letters[key] = letters
            start_index += num_letters
    
    return key_to_letters  


KEY_TO_LETTERS = get_key_to_letters()
print(KEY_TO_LETTERS)


def keypad_string(keys):
    """
    Given a string consisting of 0-9,
    find the string that is created using 
    a standard phone keypad
    | 1       | 2(abc) | 3(def)  |
    | 4(ghi)  | 5(jkl) | 6(mno)  |
    | 7(pqrs) | 8(tuv) | 9(wxyz) |
    | *       | 0( )   | #       |
    You can ignore 1, and 0 correspondes to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    >>> keypad_string("&")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid key
    """
    # build the map from keys to letter

    # loop through the keys and add the corresponding letter
    # taking into account keys pressed multiple times
    result = ""
    count = 0
    prev_key = ""
    cur_key = ""
    valid_keys = set(string.digits)

    for cur_key in keys: # O(n)
        assert cur_key in valid_keys, "Invalid key"
        if cur_key == "1":
            pass
        else:
            if not prev_key:
                prev_key = cur_key
                count = 1    
            else:
                curr_key_letter = KEY_TO_LETTERS[cur_key]
                # press the same key
                if prev_key == cur_key:
                    # press x times
                    if count == len(curr_key_letter):
                        result += curr_key_letter[-1]
                        count = 1
                    # hasn't pressed x times
                    else:
                        count += 1
                # press different key
                else:
                    prev_letters = KEY_TO_LETTERS[prev_key]
                    result += prev_letters[count - 1]
                    prev_key = cur_key
                    count = 1

    if cur_key:                
        curr_key_letters = KEY_TO_LETTERS[cur_key]
        if len(curr_key_letters) > 0:
            result += curr_key_letters[count - 1]

    return result
