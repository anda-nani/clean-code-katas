def get_vowels(s: str) -> str:
    
    r = ""
    
    for char in s:
        if char in "aeiouAEIOU":
            if r.__len__() > 0:     #Not the first vowel, add a comma before adding the next one
                r += ", "
            r += char
    
    return r

print(get_vowels("Umuzi"))  