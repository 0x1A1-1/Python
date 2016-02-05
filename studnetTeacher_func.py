lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
       total= float(sum(numbers))
       total/=len(numbers)
       return total
       
def get_average(student):
    homework=average(student["homework"])* 0.1
    quizzes=average(student["quizzes"]) *0.3
    tests=average(student["tests"])* 0.6
    return homework+quizzes+tests
    
def get_letter_grade(score):
    if score>= 90:
        return "A"
    elif score>= 80:
        return "B"
    elif score>= 70:
        return "C"
    elif score>= 60:
        return "D"
    else:
        return "F"
    
def get_class_average(students):
    result=[]
    for s in students:
        result.append(get_average(s))
    return average(result)
    
class_avg=get_class_average([lloyd, alice, tyler])
print class_avg
print get_letter_grade(class_avg)