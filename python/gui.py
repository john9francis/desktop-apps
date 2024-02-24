# creates a tkinter gui

import tkinter as tk
from chooser import Chooser



def main():

  def on_enter_pressed(event):
    input_text = entry.get()
    chooser.add_csv_to_word_list(input_text)
    update_words_display()

    # clear out textbox
    entry.delete(0, tk.END)


  def update_words_display():
    '''
    Update the words display with the
    words in the chooser
    '''
    updated_text = ' '.join(chooser.get_word_list())
    words.config(text=updated_text)

  
  def on_button_click():
    rand_word = chooser.get_random_word()
    label_result.config(text=rand_word)
    pass


  def update_textbox_pos(event):
    window_height = root.winfo_height()
    desired_y = .5 * window_height
    entry.pack(pady=(desired_y, 10))

  # create our random chooser
  chooser = Chooser()
  

  # Create the main window
  root = tk.Tk()
  root.title("Random Chooser")

  # Set dark theme
  root.tk_setPalette(background='#333', foreground='#fff')

  # set size
  root.geometry("800x400")

  # The gui elements go from top to bottom 

  # Title element
  title_font = ("Times New Roman", 20)
  title =  tk.Label(root, text="Random Chooser App", font=title_font)
  title.pack(pady=(10,0))

  # list of words element
  words = tk.Label(root, text="")
  words.pack()

  # text entry element
  entry = tk.Entry(root, width=30)
  entry.pack(pady=10)

  # choose random button
  button = tk.Button(root, text="Choose random", command=on_button_click)
  button.pack(pady=10)

  # Random choice button
  label_result = tk.Label(root, text="", foreground='#fff')
  label_result.pack(pady=10)

  # bind the enter button
  entry.bind("<Return>", on_enter_pressed)
  # bind changing window size to moving entry
  root.bind("<Configure>", update_textbox_pos)

  # Run the Tkinter event loop
  root.mainloop()


if __name__ == "__main__":
  main()