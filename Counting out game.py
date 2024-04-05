from tkinter import messagebox
from tkinter import *


class CountingOutGame:
    def __init__(self, rt):
        self.root = rt
        self.root.title("Counting-Out Game")
        self.root.minsize(350, 260)
        self.root.configure(bg="black")
        print('hello there')

        # Create N and K to be String so entry doesn't show 0
        self.N = StringVar()
        self.K = StringVar()
        self.round = 1 # Create the round counter

        # Create labels, entry fields, and start button
        self.label_N = Label(root, text="Enter the value of N (1 < N < 12):",
                             pady=20, fg="white", bg="black", font=("Arial", 15))
        self.entry_N = Entry(root, textvariable=self.N, font=("Arial", 14))

        self.label_K = Label(root, text="Enter the value of K (K >= 1):",
                             pady=20, fg="white", bg="black", font=("Arial", 15))
        self.entry_K = Entry(root, textvariable=self.K, font=("Arial", 14))

        self.spacer = Label(root, text="", bg="black")

        self.start_button = Button(root, text="START", command=self.start_game,
                                   width=13, fg="white", bg="black", font=("Arial Bold", 15))

        # Pack labels, entry fields, and start button
        self.label_N.pack()
        self.entry_N.pack()
        self.label_K.pack()
        self.entry_K.pack()
        self.spacer.pack()
        self.start_button.pack()

        # Create eliminate button and players list
        self.eliminate_button = Button(root, text="ELIMINATE", command=self.eliminate_player,
                                       width=20, fg="white", bg="black", font=("Arial BOlD", 15))
        self.players = []

        # Create info_window so it can be manipulated later
        self.info_window = None

    def start_game(self):
        try:
            # Get values of N and K from entry fields
            n = int(self.N.get())
            k = int(self.K.get())
            # Validate input values
            if not (1 < n < 12 and k >= 1):
                messagebox.showinfo("Invalid Input", "Please enter valid values for N and K.")
                return

            # Hide labels, entry fields, and start button
            self.label_N.pack_forget()
            self.entry_N.pack_forget()
            self.label_K.pack_forget()
            self.entry_K.pack_forget()
            self.spacer.forget()
            self.start_button.pack_forget()

            # Create a new window for game information
            self.info_window = Toplevel(self.root)
            self.info_window.title("Game Information")

            # Create a text widget to display game information
            self.info_text = Text(self.info_window, height=10, width=35)
            self.info_text.pack()
            self.info_text.insert(END, f"Game started. N={n} K={k}\n")

            # Display the eliminate button
            self.eliminate_button.pack()
            self.spacer.pack()

            # Create player labels and display them
            for i in range(n):
                player_label = Label(self.root, text=str(i), bg="black", fg="white", pady=1,
                                     relief="ridge", font=("Comic Sans MS", 16))
                player_label.pack()
                self.players.append(player_label)

            # Reset round to 1
            self.round = 1

        # Intercept if user input something other than number
        except ValueError:
            messagebox.showinfo("Invalid Input", "Please enter valid integer values for N and K.")

    def eliminate_player(self):
        if len(self.players) <= 2:
            winner = self.players[0].cget("text")
            messagebox.showinfo("Game Over", f"The winner is Player {winner}!")
            # Hide player labels
            for player in self.players:
                player.pack_forget()

            # Destroy eliminate button
            self.eliminate_button.pack_forget()
            self.spacer.forget()

            # Display labels, entry fields, and start button
            # Reset players list and entry labels
            self.players = []
            self.label_N.pack()
            self.entry_N.pack()
            self.entry_N.delete(0, 'end')
            self.label_K.pack()
            self.entry_K.pack()
            self.entry_K.delete(0, 'end')
            self.spacer.pack()
            self.start_button.pack()

            # Destroy the info_window
            if self.info_window:
                self.info_window.destroy()
            return

        # Remove player label based on the elimination rule
        k = int(self.K.get())
        eliminated = self.players.pop((k - 1) % len(self.players))
        eliminated.pack_forget()
        # Display elimination message in the game information text widget
        # Increment round
        self.info_text.insert(END, f"Round {self.round}: Player {eliminated.cget('text')} eliminated.\n")
        self.round += 1


root = Tk()
game = CountingOutGame(root)
root.mainloop()
