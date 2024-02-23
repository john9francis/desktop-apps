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

  c = Chooser()

  running = True
  while running:
    # clear console and write prompt
    clear_console()
    print("Here is your list:")
    print(c.get_word_list())
    print("enter the following:")
    print("\"q\" to quit")
    print("\"a\" to add to the list")
    print("\"r\" to get a random choice from the list")


    # get user input
    user_input = input(">> ")

    print(user_input)

    if user_input == "q":
      print("Quitting...")
      running = False




if __name__ == "__main__":
  main()