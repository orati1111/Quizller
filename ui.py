from tkinter import *
from tkinter import messagebox

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_FONT = ("Arial",20,"italic")
CANVAS_HEIGHT = 250
CANVAS_WIDTH = 300
WINDOW_X_PADDING = 20
WINDOW_Y_PADDING = 20


class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizller")
        self.window.config(padx=WINDOW_X_PADDING,pady=WINDOW_Y_PADDING,background=THEME_COLOR)
        self.true_img = PhotoImage(file="images\\true.png")
        self.false_img = PhotoImage(file="images\\false.png")
        self.create_label()
        self.create_canvas()
        self.create_buttons()
        self.get_next_question()
        self.window.mainloop()

    def create_label(self):
        self.score_label = Label(text=f"Score: {self.quiz.score}",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)


    def create_canvas(self):
        self.canvas = Canvas(width=CANVAS_WIDTH,height=CANVAS_HEIGHT,bg="white")
        self.question_text = self.canvas.create_text(150,
                                                    125,
                                                    width=CANVAS_WIDTH-20,
                                                    text="Some Text",
                                                    font=CANVAS_FONT,
                                                    fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


    def create_buttons(self):
        self.correct_button = Button(image=self.true_img,command=lambda answer="true":self.answer_question(answer))
        self.wrong_button = Button(image=self.false_img,command=lambda answer="false":self.answer_question(answer))
        self.correct_button.grid(row=2,column=0)
        self.wrong_button.grid(row=2,column=1)


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.display_score()
            self.wrong_button.config(state="disabled")
            self.correct_button.config(state="disabled")

    
    def answer_question(self,answer):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
            self.update_score_label()
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
    
    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
    
    def display_score(self):
        final_score =f"Your final score is : {self.quiz.score}/{self.quiz.question_number}"
        self.canvas.itemconfig(self.question_text,text="")
        game_ending_messege = messagebox.askretrycancel(message=final_score,title="Game Over!")
        if not game_ending_messege:
            exit()
