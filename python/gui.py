# creates a tkinter gui

import tkinter as tk
from chooser import Chooser



def main():

  def add_to_list(event=None):
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
    updated_text = '\n'.join(chooser.get_word_list())
    words.config(text=updated_text)

  
  def on_button_click():
    rand_word = chooser.get_random_word()
    label_result.config(text=rand_word)
    pass


  def update_frame_pos(event):
    window_height = root.winfo_height()
    desired_y = .3 * window_height
    frame.pack(pady=(desired_y, 10))

  def clear_list():
    chooser.clear_word_list()
    update_words_display()

  # create our random chooser
  chooser = Chooser()
  

  # Create the main window
  root = tk.Tk()
  root.title("Random Chooser")

  # Set dark theme
  root.tk_setPalette(background='#333', foreground='#fff')

  # set size
  root.geometry("800x400")
  root.minsize(600, 400)

  # The gui elements go from top to bottom 

  # Title element
  title_font = ("Times New Roman", 50)
  title =  tk.Label(root, text="Random Chooser App", font=title_font)
  title.pack(pady=(10,0))

  # list of words element
  words_frame = tk.Frame(root)
  words_frame.pack()
  words = tk.Label(words_frame, text="")
  words.pack()

  # element for the entry and submit buttons
  frame = tk.Frame(root)
  frame.pack()

  # text entry element
  entry = tk.Entry(frame, width=30)
  entry.pack(side="left", padx=5)

  # submit button
  submit = tk.Button(frame, text="Add to list", command=add_to_list)
  submit.pack(side="right", padx=5)

  # clear list button
  clear_button = tk.Button(root, text="Clear list", command=clear_list)
  clear_button.pack(pady=10)

  # choose random button
  button = tk.Button(root, text="Choose random", command=on_button_click)
  button.pack(pady=10)

  # Random choice button
  label_result = tk.Label(root, text="", foreground='#fff')
  label_result.pack(pady=10)

  # bind the enter button
  entry.bind("<Return>", add_to_list)
  # bind changing window size to moving entry
  root.bind("<Configure>", update_frame_pos)

  # Run the Tkinter event loop
  root.mainloop()


if __name__ == "__main__":
  main()