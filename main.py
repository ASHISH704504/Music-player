
from tkinter import filedialog
from tkinter import *
import pygame
import os

root= Tk()
root.title('music player')
root.geometry("500x400")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False


def load_music():
    global songs, current_song

    root.directory = filedialog.askdirectory()

    if not root.directory:
        return

    songs.clear()
    songlist.delete(0, END)

    for file in os.listdir(root.directory):
        if file.lower().endswith(".mp3"):
            songs.append(file)
            songlist.insert(END, file)

    if songs:
        current_song = songs[0]
        songlist.selection_set(0)
        songlist.activate(0)

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False


def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def prev_music():
    global current_song , paused

    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)-1)
        current_song =songs[songlist.curselection()[0]]
        play_music()
    except: 
        pass  


    

def next_music():
    global current_song, paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass



organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='select folder', command=load_music)
menubar.add_cascade(label='organise', menu=organise_menu)


songlist = Listbox(root, bg="black", fg="white",width=100,height=15)
songlist.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
prev_btn_image = PhotoImage(file='previous.png')
next_btn_image = PhotoImage(file='next.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image= play_btn_image, borderwidth=0,command=play_music)
pause_btn= Button(control_frame, image= pause_btn_image, borderwidth=0,command=pause_music)
prev_btn= Button(control_frame, image= prev_btn_image, borderwidth=0,command=prev_music)
next_btn= Button(control_frame, image= next_btn_image, borderwidth=0,command=next_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()

 