from chooser import Chooser


def main():
  c = Chooser()

  c.add_csv_to_word_list("John, Jane, Jack, Jill, Jacob")
  c.add_csv_to_word_list("John Francis, Jane Doe, Hello World")

  print(c.get_random_word())



if __name__ == "__main__":
  main()