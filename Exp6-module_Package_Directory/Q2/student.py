# Create a module containing functions to calculate total marks, percentage, and grade.

def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"