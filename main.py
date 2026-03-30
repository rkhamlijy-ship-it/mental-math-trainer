# main.py
"""
Mental Math Trainer - GUI version using Tkinter
Shows questions, allows user input, validates answers, and displays results.
"""

import tkinter as tk
from mental_math_trainer.trainer import generate_questions, check_answers

class MentalMathApp:
    def __init__(self, master):
        self.master = master
        master.title("Mental Math Trainer")

        self.rounds = 5
        self.level = None
        self.questions = []
        self.entries = []

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Welcome to Mental Math Trainer!", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.master, text="Train your mental math skills", font=("Arial", 12)).pack(pady=5)

        tk.Label(self.master, text="Choose difficulty level:").pack(pady=5)
        self.level_var = tk.StringVar(value="easy")
        levels = ["easy", "medium", "hard"]
        for lvl in levels:
            tk.Radiobutton(self.master, text=lvl.capitalize(), variable=self.level_var, value=lvl).pack()

        tk.Button(self.master, text="Start Game", command=self.start_game).pack(pady=20)

    def start_game(self):
        self.level = self.level_var.get()
        self.questions = generate_questions(self.level, self.rounds)
        self.create_question_screen()

    def create_question_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="Solve the following questions:", font=("Arial", 14)).pack(pady=10)
        self.entries = []

        for idx, (q, _) in enumerate(self.questions):
            frame = tk.Frame(self.master)
            frame.pack(pady=3)
            tk.Label(frame, text=f"{q} = ").pack(side="left")
            entry = tk.Entry(frame, width=5)
            entry.pack(side="left")
            self.entries.append(entry)

        tk.Button(self.master, text="Submit Answers", command=self.show_results).pack(pady=20)

    def show_results(self):
        user_answers = [e.get() for e in self.entries]
        results = check_answers(user_answers, self.questions)
        self.clear_screen()

        tk.Label(self.master, text="Results:", font=("Arial", 14, "bold")).pack(pady=10)
        for question, user_input, correct, status in results:
            if status == "correct":
                color = "green"
                msg = f"{question} = {user_input} ✅"
            elif status == "wrong":
                color = "red"
                msg = f"{question} = {user_input} ❌ (Correct: {correct})"
            else:
                color = "orange"
                msg = f"{question} = {user_input} ⚠️ (Invalid, Correct: {correct})"
            tk.Label(self.master, text=msg, fg=color).pack()

        tk.Button(self.master, text="Play Again", command=self.create_welcome_screen).pack(pady=15)
        tk.Button(self.master, text="Exit", command=self.master.quit).pack(pady=5)

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MentalMathApp(root)
    root.mainloop()