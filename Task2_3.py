def columns(words: list) -> None :
   
   max_len = max(len(word) for word in words)  #find the longest word length in the list

   for i in range(max_len):
      row = ''
      for word in words:
        row += word[i] if i < len(word) else ' '  #add character if it exists, otherwise add a space
        row += ' '
      print(row)

columns(["Write","good","code","every","day"])