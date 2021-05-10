# student number: 2086876

def pluralize(word):
    '''
    Determines the plural of an English word.
    
    Args:
        word: The word provided by the user.
        
    Returns: The pluralized version of the input argument word.
    '''
    #open proper_nouns.txt and then using regex to create a list with the words included in this txt file
    import re
    try:
        f = open(r'proper_nouns.txt', 'r')
        mylist = re.findall(r'[a-zA-Z]+', str(f.read()))
        f.close()
    except:
        return 'proper_nouns.txt file not found. Please try again !'
    
    #if-elif statement to check the different cases
    if word == '':
        word_in_plural = ''
        x = 'empty_string'
    #word[-1] is the last letter of the word provided by the user
    elif word[-1] == 's':
        word_in_plural = word
        x = 'already_in_plural'
    #The lower() function is needed as the words in the proper_nouns.txt are all letters in lowercase
    elif word.lower() in mylist:
        word_in_plural = word
        x = 'proper_noun'
    else:
        #assign the last letter of the word provided in a new variable called last_letter
        last_letter = word[-1]
        #to reach this part of the code it means we have x as success based on the description of the function
        x = 'success'
#         if len(re.findall(r'\w+[aeio]', last_letter)) > 0:
#             word_in_plural = word + 's'
#         elif last_letter == 'y':
#             if len(re.findall(r'[^aeioy]', word[-2])) > 0:
#                 word_in_plural = word[:-1] + 'ies'
#             else:
#                 word_in_plural = word + 's'
        if last_letter == 'y':
            #we use word[-2] as we want to check if the 'y' is preceded by a consonant
            if len(re.findall(r'[^aeioy]', word[-2])) > 0:
                #word[:-1] is the word provided by the user without the last letter
                word_in_plural = word[:-1] + 'ies'
            else:
                word_in_plural = word + 's'
        elif last_letter == 'f':
            #word[:-1] is the word provided by the user without the last letter
             word_in_plural = word[:-1] + 'ves'
        elif len(re.findall(r'[sh|ch|z]', last_letter)) > 0:
             word_in_plural = word + 'es'
        else:
             word_in_plural = word + 's'
            
    my_dict = {'plural': word_in_plural, 'status': x}
    
    return my_dict

### --- IMPORTANT: DO NOT REMOVE OR CHANGE THE CODE BELOW ---
TEST_CASES = """failure
food
Zulma
injury
elf
buzz
computers
PCs

highway
presentation
pouch
COVID-19
adam""".split('\n')

if __name__ == '__main__':

  for test_noun in TEST_CASES:

    print(test_noun,'-->',pluralize(test_noun))
    print('----')