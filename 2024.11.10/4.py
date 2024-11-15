def countable_nouns(num: int, nouns: tuple[str, str, str]) -> str:
    second_noun_ending = [2, 3, 4]
    third_noun_ending = [0, 5, 6, 7, 8, 9]
    exclusion = [11, 12, 13, 14]
    if num % 10 == 1 and num % 100 not in exclusion:
        return nouns[0]
    if num % 10 in second_noun_ending and num % 100 not in exclusion:
        return nouns[1]
    if num % 10 in third_noun_ending or num % 100 in exclusion:
        return nouns[2]
        


# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'