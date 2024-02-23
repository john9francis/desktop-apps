import random

class Chooser:

  def __init__(self) -> None:
    self.word_list = []
    pass

  def add_to_word_list(self, new_word):
    self.word_list.append(new_word)

  
  def clear_word_list(self):
    self.word_list.clear()


  def get_random_word(self):
    return random.choice(self.word_list)
  

  def get_word_list(self):
    return self.word_list


  def add_csv_to_word_list(self, csv_string):
    '''
    Take in a csv string and add each value to the word list.
    '''
    words = csv_string.split(',')
    cleaned_words = [word.strip() for word in words]
    self.word_list.extend(cleaned_words)