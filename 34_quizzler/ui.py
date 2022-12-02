import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#abcad9"

FONT = ("CarbonType", 16, "italic")


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.minsize(350, 350)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)
        self.label_score = tk.Label(self.window)
        self.label_score.config(bg=THEME_COLOR, fg="green", font=FONT, text=f"Score {self.quiz.score}")
        self.label_score.grid(column=1, row=0)
        self.txt_canvas = tk.Canvas(self.window, width=310, height=250, bg="white", highlightthickness=0)
        self.txt = self.txt_canvas.create_text(
            150,
            125,
            width=290,
            text=f"",
            font=FONT
        )
        self.txt_canvas.grid(column=0, row=1, columnspan=2, padx=10)
        im_true = tk.PhotoImage(file="./images/true.png")
        im_false = tk.PhotoImage(file="./images/false.png")
        self.btn_true = tk.Button(self.window, image=im_true, highlightthickness=0, command=self.push_btn_true)
        self.btn_true.grid(column=0, row=2, padx=53)
        self.btn_false = tk.Button(self.window, image=im_false, highlightthickness=0, command=self.push_btn_false)
        self.btn_false.grid(column=1, row=2, padx=53)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.txt_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            current_q = self.quiz.next_question()
            self.txt_canvas.itemconfig(self.txt, text=current_q)
        else:
            self.txt_canvas.itemconfig(self.txt, text='You finished the quiz!')
            self.btn_true["state"] = tk.DISABLED
            self.btn_false["state"] = tk.DISABLED

    def push_btn_true(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def push_btn_false(self):
        self.get_feedback(self.quiz.check_answer("False"))

    def get_feedback(self, is_right: bool):
        self.txt_canvas.config(bg="green")
        if is_right:
            self.label_score.config(text=f"Score {self.quiz.score}")
            self.txt_canvas.config(bg="green")
        else:
            self.txt_canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
