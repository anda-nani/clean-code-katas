def find_common_characters(s1: str, s2: str) -> str:
    
    common_chars = ""

    for char in s1:
        if char in s2 and char not in common_chars:

            if common_chars.__len__() > 0:     #Not the first character, add a comma before adding the next one
                common_chars += ", "
                
            common_chars += char
    
    return common_chars

print(find_common_characters("house", "computers"))  