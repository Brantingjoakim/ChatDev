'''
This is the main file of the Couples Counseling App.
It provides the user interface and handles user interactions.
'''
import tkinter as tk
from attachment_style import AttachmentStyle
from problem_solver import ProblemSolver
class CouplesCounselingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Couples Counseling App")
        self.attachment_style = AttachmentStyle()
        self.problem_solver = ProblemSolver()
        self.create_widgets()
    def create_widgets(self):
        # Create attachment style selection labels and radio buttons
        attachment_style_label = tk.Label(self.root, text="Select Your Attachment Style:")
        attachment_style_label.pack()
        self.attachment_style_var = tk.StringVar()
        attachment_style_radio_buttons = []
        for style in self.attachment_style.get_styles():
            radio_button = tk.Radiobutton(self.root, text=style, variable=self.attachment_style_var, value=style)
            attachment_style_radio_buttons.append(radio_button)
            radio_button.pack()
        # Create problem entry field and solve button
        self.problem_entry = tk.Entry(self.root)
        self.problem_entry.pack()
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_problem)
        solve_button.pack()
        # Create solution display area
        self.solution_text = tk.Text(self.root, height=10, width=50)
        self.solution_text.pack()
    def solve_problem(self):
        problem = self.problem_entry.get()
        attachment_style = self.attachment_style_var.get()
        solution = self.problem_solver.solve_problem(problem, attachment_style)
        if solution == "No solution found for the given problem and attachment style.":
            solution = f"No solution found for the problem '{problem}' and attachment style '{attachment_style}'."
        self.solution_text.delete(1.0, tk.END)
        self.solution_text.insert(tk.END, solution)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = CouplesCounselingApp()
    app.run()