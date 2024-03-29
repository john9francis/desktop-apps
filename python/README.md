# Python random chooser app

Getting this project setup for dev (windows)
```
git clone https://github.com/john9francis/desktop-apps
python -m venv venv
.\venv\scripts\activate
pip install -r requirements.txt
```

# Options for creating python executables
1. pyinstaller
2. cx_Freeze
3. pyoxidizer
4. nuitka
5. briefcase

I decided to go with pyinstaller.

Here's how to compile your app with pyinstaller.

```
pyinstaller --onefile cli.py
```

For compiling with a gui and no console, note: must run as administrator:

```
pyinstaller --onefile --noconsole gui.py
```

# Using docker to compile for cross-platform
Finding macOS and linux images would be good for compiling for those platforms. The only issue is that macOS won't run apps unless they have been notarized by apple... That's complicated. The best way to compile on macOS or linux would be to run pyinstaller while using one of those operating systems. 

# Review of the experience with python
- Pyinstaller is a super easy tool
- I was surprised because I thought it would be harder to pack a python runtime into an executable
- The problem is cross-platform compiling, I just gave up
- Tkinter is relatively easy to get going fast
- Tkinter will definitely take some getting used to, especially to make it look nice
- It is also hard to get used to organizing elements in Tkinter.
- This may be a good option for making desktop apps, if I want to full send and commit to Tkinter. It is kind of a niche skill though, I think I would rather invest in learning react or something.