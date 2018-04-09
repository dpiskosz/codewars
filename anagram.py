te = "Creative"
org = "Reactive"


def is_anagram(test, original):
    len_or = len(original)
    len_test = len(test)
    if len_or == len_test:
        for x in test.lower():
            if x not in original.lower():
                return False
            else:
                new_org = original.lower().replace(x, "", 1)
            original = new_org
        return True
    else:
        return False


print(is_anagram(te, org))