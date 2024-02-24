# creates a tkinter gui

import tkinter as tk



def main():

  def on_button_click():
    input_text = entry.get()
    label_result.config(text=f"You entered: {input_text}")


  def on_enter_pressed(event):
    label_result.config(text=f"Enter pressed")

  def adjust_pady(pady_factor):
    root.update_idletasks()
    current_height = root.winfo_height()
    pady = current_height * pady_factor
    return pady
  
  def update_textbox_pos(event):
    window_height = root.winfo_height()
    desired_y = .5 * window_height
    entry.pack(pady=(desired_y, 10))

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

  # text entry element
  entry = tk.Entry(root, width=30)
  entry.pack(pady=10)

  # choose random button
  button = tk.Button(root, text="Submit", command=on_button_click)
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