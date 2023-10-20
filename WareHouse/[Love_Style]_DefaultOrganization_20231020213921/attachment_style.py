'''
This file defines the AttachmentStyle class which represents the attachment styles of partners.
'''
class AttachmentStyle:
    def __init__(self):
        self.styles = ["Secure", "Anxious", "Avoidant"]
    def get_styles(self):
        return self.styles