def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        str1_sorted = sorted(str1)
        str2_sorted = sorted(str2)
        if str1_sorted == str2_sorted:
            return True
        else:
            return False
