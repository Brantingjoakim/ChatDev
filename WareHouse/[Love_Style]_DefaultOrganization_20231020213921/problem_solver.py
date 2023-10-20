'''
This file defines the ProblemSolver class which solves problems based on attachment styles.
'''
class ProblemSolver:
    def __init__(self):
        self.solutions = {
            "Secure": {
                "communication": "Openly communicate your feelings and needs to your partner.",
                "trust": "Build trust through honesty and reliability.",
                "conflict": "Address conflicts calmly and seek compromise.",
            },
            "Anxious": {
                "communication": "Express your concerns and fears to your partner.",
                "trust": "Seek reassurance and establish clear boundaries.",
                "conflict": "Avoid escalating conflicts and practice active listening.",
            },
            "Avoidant": {
                "communication": "Be more open and express your emotions to your partner.",
                "trust": "Work on building trust by being consistent and reliable.",
                "conflict": "Take time to reflect and come back to discuss conflicts calmly.",
            }
        }
    def solve_problem(self, problem, attachment_style):
        if attachment_style not in self.solutions:
            return f"Attachment style '{attachment_style}' is not supported."
        elif problem in self.solutions[attachment_style]:
            return self.solutions[attachment_style][problem]
        else:
            return f"No solution found for the problem '{problem}' and attachment style '{attachment_style}'."