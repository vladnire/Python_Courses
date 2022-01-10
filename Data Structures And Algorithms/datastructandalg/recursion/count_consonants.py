"""
Given a string, calculate the number of consonants present.
vowels: a e i o u
"""

vowels = "aeiou"
def iterative_count_consonants(input_str):
    consonants = 0
    for e in input_str:
        if e.lower() not in vowels and e.isalpha():
            consonants += 1
    return consonants


input_str = "abc de"
print(input_str)
print(iterative_count_consonants(input_str))


def recursive_count_consonants(input_str):
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():    
        return 1 + recursive_count_consonants(input_str[1:])
    return recursive_count_consonants(input_str[1:])


input_str = "LuCiDPrograMMiNG"
print(input_str)
print(recursive_count_consonants(input_str))