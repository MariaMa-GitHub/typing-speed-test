# TYPING SPEED TEST
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import time

# program settings
PROGRAM_NAME = "Typing Speed Test"
BG_COLOR = "#A9A9A9"
WINDOW_SIZE = "687x440"
TEST_TIME = 60


# program class
class Program:

    # initialize settings
    def __init__(self):

        self.wpm = 0

        self.window = Tk()
        self.window.title(PROGRAM_NAME)
        self.window.config(padx=50, pady=50, bg=BG_COLOR)
        self.window.geometry(WINDOW_SIZE)
        self.window.resizable(width=0, height=0)

        self.title_label = Label(text=PROGRAM_NAME, font=("Arial", 16, "bold"), bg=BG_COLOR, justify="center")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(10, 0), sticky='we')

        self.sample_textbox = Text(self.window, width=68, height=8, font=("Times New Roman", 12, "normal"), padx=10, pady=10)
        self.sample_textbox.grid(row=1, column=0, columnspan=2, padx=10, pady=(30, 0), sticky='we')
        self.get_sample_text()

        self.user_textbox = ScrolledText(self.window, wrap=WORD, width=40, height=2, font=("Times New Roman", 12, "normal"), padx=10, pady=10)
        self.user_textbox.grid(row=2, column=0, padx=10, pady=(20, 0), sticky='we')
        self.user_textbox.focus()

        self.time_wpm_label = Label(text="TIME: 0s", font=("Arial", 14), bg="white", justify="center")
        self.time_wpm_label.grid(row=2, column=1, padx=10, pady=(20, 0), sticky='nswe')

        self.typing_speed_test()

        self.window.mainloop()

    # get data
    def get_sample_text(self):

        with open("text.txt", "r") as f:

            self.sample_text = f.read().rstrip()

        self.sample_textbox.insert(INSERT, self.sample_text)
        self.sample_textbox.config(state=DISABLED)

    # perform test
    def typing_speed_test(self):

        if self.user_textbox.get("1.0", END).strip() != "":

            self.start = time.time()
            self.words_per_minute()

        else:

            self.window.after(1, self.typing_speed_test)

    # count wpm
    def words_per_minute(self):

        self.stop = time.time()

        elapsed_time = int(self.stop - self.start)

        if elapsed_time >= TEST_TIME:

            self.user_textbox.config(state=DISABLED)

            self.user_text = self.user_textbox.get("1.0", END).strip().replace("\n\n", " ").split(" ")
            self.sample_text = self.sample_text.replace("\n\n", " ").split(" ")

            for w in self.user_text:
                if w in self.sample_text:
                    self.sample_text.remove(w)
                    self.wpm += 1

            self.time_wpm_label.config(text=f"WPM: {self.wpm}")

        else:

            self.window.after(1000, self.words_per_minute)
            self.time_wpm_label.config(text=f"TIME: {elapsed_time}s")


# main program
program = Program()
