def print_upper_words(words, must_start_with):
    """For a list of words, print out each word on a separate line, but in all uppercase. The function print_upper_words only prints words in variable print_upper_words [] that start with the letters in variable must_start_with {} (either upper or lowercase).
    
    For example:
    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

    Should print:
      HELLO
      HEY
      YO
      YES
    """  
    #loop through word list
    for word in words:
        #loop through must_start_with chars
        for char in must_start_with:
          #if the word starts with the must_start_with char print the word in uppercase
          if (word[0] == char):
            print(word.upper())

# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
