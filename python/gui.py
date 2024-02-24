# creates a tkinter gui

import tkinter as tk



def main():

  def on_button_click():
    input_text = entry.get()
    label_result.config(text=f"You entered: {input_text}")


  def on_enter_pressed(event):
    label_result.config(text=f"Enter pressed")


  # Create the main window
  root = tk.Tk()
  root.title("Random Chooser")

  # Set dark theme
  root.tk_setPalette(background='#333', foreground='#fff')

  # set size
  root.geometry("800x400")

  # text entry element
  entry = tk.Entry(root, width=30)
  entry.pack(pady=(250,0))

  # choose random button
  button = tk.Button(root, text="Submit", command=on_button_click)
  button.pack(pady=10)

  # Random choice button
  label_result = tk.Label(root, text="", foreground='#fff')
  label_result.pack(pady=10)

  # bind the enter button
  entry.bind("<Return>", on_enter_pressed)

  # Run the Tkinter event loop
  root.mainloop()


if __name__ == "__main__":
  main()