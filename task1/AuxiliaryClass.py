import re 
def syllable_counter(frase):
      return len(re.split(r'[аеоуиэыёяю]', frase))-1

class AuxiliaryClass:
   def __init__(self):
      pass 
   
   def input_method(self, message):
      return input(message)

   def checking_for_rhythm_method(self, poem):
      poems_words = poem.split(' ')
      result = set([syllable_counter(i) for i in poems_words])
      if len(result) == 1: return "Парам пам-пам"
      else: return "Пам парам" 
         