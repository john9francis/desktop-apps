import os
import sys

from chooser import Chooser

def clear_console():
  if sys.platform.startswith('win'):
    # close in windows
    os.system('cls')
  else:
    # close in macOS or linux
    os.system('clear')


def main():

  # create a interface the user can interact with

  chooser = Chooser()

  running = True
  while running:
    # clear console and write prompt
    clear_console()
    print("Here is your list:")

    print(chooser.get_word_list())

    print("enter the following:")
    print("\"q\" to quit")
    print("\"a\" to add to the list")
    print("\"r\" to get a random choice from the list")
    print("\"c\" to clear the list")


    # get user input
    user_input = input(">> ")

    if user_input == "q":
      print("Quitting...")
      running = False

    elif user_input == "a":
      # add to word list
      print("Please enter your word, or several words separated by commas.")
      words = input(">> ")
      chooser.add_csv_to_word_list(words)

    elif user_input == "r":
      # print random word
      print(chooser.get_random_word())
      print("Press enter to continue...")
      input(">> ")

    elif user_input == "c":
      # make sure user wants to clear
      print("Are you sure you would like to clear the list?")
      
      while True:
        response = input("(y/n)>> ")
        response = response.lower()

        if response == "y":
          print("Clearing list...")
          chooser.clear_word_list()
          break
        elif response == "n":
          print("Not clearing list.")
          break

        else: 
          print("Please enter \"y\" or \"n\".")


    else:
      # unknown input
      print(f"{user_input} is not recognized, please enter q, a, or r.")
      input("Press enter to continue...")
    




if __name__ == "__main__":
  main()