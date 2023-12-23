student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades={}
for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="outstanding"
    elif score<90 and score>80:
        student_grades[student]="exeeds expectations"
    elif score<80 and score>70:
        student_grades[student]="acceptable"
    else:
        student_grades[student]="fail"
print(student_grades)

