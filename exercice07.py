def get_letter_count(word):
    count = 0
    for i in word:
      if i.isalpha():
        count +=1
    return count

#def isalpha(x):
#    return x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #'[^a-zA-Z]'

def run():
   assert get_letter_count("Oui") == 3
   assert get_letter_count("Bonjour") == 7
   assert get_letter_count("") == 0
   assert get_letter_count(".........hein???") == 4
   assert get_letter_count("Attention y'a quatre mots !") == 21
