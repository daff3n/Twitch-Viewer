import webbrowser
from Tkinter import *
import os

class Twitcher:

    def __init__(self):
        # Fetch a list with channels for the listbox from a file.
        self.favs = open("favs.txt","r+")
        self.fav = self.favs.read().split()
        self.lbHeight = len(self.fav)

        # Get your auth key at: http://www.twitchapps.com/tmi/
        self.twitchAuth = ""

    def init_window(self):
        self.root = Tk()
        self.root.title("Twitcher")
        self.customStream = StringVar()

        # Frame
        self.frame = Frame(self.root)
        self.frame.pack(padx=20,pady=20)

        # Listbox
        self.listbox = Listbox(self.frame, selectmode=SINGLE,height=self.lbHeight,width=35)
        for self.n in self.fav:
            self.listbox.insert(END, self.n)
        self.listbox.pack()

        # Button
        self.vlcButton = Button(self.frame, text="Open in vlc", command= lambda: self.runStream('vlc'))
        self.vlcButton.pack(pady=10, side=LEFT)

        self.brButton = Button(self.frame, text="Open in Browser", command= lambda: self.runStream('browser'))
        self.brButton.pack(pady=10,padx=10,side=LEFT)

        self.root.mainloop()

    def runStream(self,platform):
        self.platform = platform
        self.index = int(self.listbox.curselection()[0])
        self.channel = self.listbox.get(self.index)

        if self.platform == 'browser':
            webbrowser.open('http://twitch.tv/%s' % self.channel)
        elif self.platform == 'vlc':
            os.system("livestreamer --twitch-oauth-token %s twitch.tv/%s best &" % (self.twitchAuth,self.channel))

if __name__ == "__main__":
    t = Twitcher()
    t.init_window()
