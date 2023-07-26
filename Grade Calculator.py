# Constants for maximum points
HOMEWORK_MAX = 800.0
QUIZZES_MAX = 400.0
MIDTERM_MAX = 150.0
FINAL_MAX = 200.0

# Step 1: Read input student status and scores
status = input("Enter student status (UG, G, DL): ")

try:
    homework = float(input("Enter homework score: "))
    quizzes = float(input("Enter quizzes score: "))
    midterm = float(input("Enter midterm score: "))
    final = float(input("Enter final exam score: "))
except ValueError:
    print("Error: Invalid score input")
    exit()

# Step 2: Set any average to 100% if average is above 100%
homework_avg = (homework / HOMEWORK_MAX) * 100
if homework_avg > 100:
    homework_avg = 100

quizzes_avg = (quizzes / QUIZZES_MAX) * 100
if quizzes_avg > 100:
    quizzes_avg = 100

midterm_avg = (midterm / MIDTERM_MAX) * 100
if midterm_avg > 100:
    midterm_avg = 100

final_avg = (final / FINAL_MAX) * 100
if final_avg > 100:
    final_avg = 100

# Step 3: Calculate course average based on student status
if status == "UG":
    course_avg = (homework_avg * 0.20) + (quizzes_avg * 0.20) + (midterm_avg * 0.30) + (final_avg * 0.30)
elif status == "G":
    course_avg = (homework_avg * 0.15) + (quizzes_avg * 0.05) + (midterm_avg * 0.35) + (final_avg * 0.45)
elif status == "DL":
    course_avg = (homework_avg * 0.05) + (quizzes_avg * 0.05) + (midterm_avg * 0.40) + (final_avg * 0.50)
else:
    print("Error: Invalid student status")
    exit()

# Step 4: Identify course letter grade based on course average
if course_avg >= 90.0:
    letter_grade = "A"
elif course_avg >= 80.0:
    letter_grade = "B"
elif course_avg >= 70.0:
    letter_grade = "C"
elif course_avg >= 60.0:
    letter_grade = "D"
else:
    letter_grade = "F"

# Step 5: Output category averages, course average, and letter grade
print(f"Homework: {homework_avg:2.1f}%")
print(f"Quizzes: {quizzes_avg:2.1f}%")
print(f"Midterm: {midterm_avg:2.1f}%")
print(f"Final Exam: {final_avg:2.1f}%")
print(f"{status} average: {course_avg:2.1f}%")
print(f"Course grade: {letter_grade}")
