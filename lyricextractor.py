# import modules
from tkinter import *
from lyrics_extractor import SongLyrics

# user defined funtion
def get_lyric():
	
	extract_lyrics = SongLyrics("AIzaSyAcR5ITZBqyTuPRzJL4sO-dDdWnxdApoj0", "f6b728b02fe4839a2")
	
	temp = extract_lyrics.get_lyrics(str(e.get()))
	res = temp['lyrics']
	result.set(res)


# object of tkinter
# and background set to light grey
master = Tk()
master.configure(bg='skyblue')

# Variable Classes in tkinter
result = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Enter Song name : ",
	bg="skyblue").grid(row=0, sticky=W)

Label(master, text="Result :",
	bg="skyblue").grid(row=3, sticky=W)


# Creating lebel for class variable
# name using widget Entry
Label(master, text="", textvariable=result,
	bg="skyblue").grid(row=3, column=1, sticky=W)

e = Entry(master, width=50)
e.grid(row=0, column=1)

# creating a button using the widget
b = Button(master, text="Show",
		command=get_lyric, bg="Blue")

b.grid(row=0, column=2, columnspan=2,
	rowspan=2, padx=5, pady=5,)

mainloop()
