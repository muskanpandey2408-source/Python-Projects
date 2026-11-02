print("----------STUDENT REPORT CARD----------")

def student_data():
    name=input("Enter name:-")
    n=int(input("Enter total number of subjects:-"))
    subjects=[]
    total_obtained=0
    total_max=0

    for i in range(1,n+1):
        print(f"\nSubject{i}")

        subject=input("Enter subject name:-")
        max_marks=int(input("Enter total marks:-"))
        obtained=int(input("Enter obtained marks:-"))

        while obtained > max_marks or obtained < 0:
            print("Invalid marks! Please enter again.")
            obtained=int(input("Enter obtained marks:-"))

        subjects.append([subject,max_marks,obtained])

        total_obtained+=obtained
        total_max+=max_marks

    percentage=(total_obtained / total_max)*100

    return name,subjects,total_obtained,total_max,percentage

def grade_value(grade):
    if percentage>=90:
        return 'A+'
    elif percentage>=80:
        return 'A'
    elif percentage>=70:
        return 'B+'
    elif percentage>=60:
        return 'B'
    elif percentage>=50:
        return 'C'
    elif percentage>=40:
        return 'D'
    else:
        return 'F'

def remarks(percentage):
    if percentage >= 90:
        return "Outstanding"
    elif percentage >= 80:
        return "Excellent"
    elif percentage >= 70:
        return "Very Good"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 50:
        return "Average"
    elif percentage >= 40:
        return "Needs Improvement"
    else:
        return "Poor"

def result(subject):
    for subject in subjects:
        if subject[2] < 40:
            return "FAIL"
    return "PASS"

def display_report(name,subjects,total_obtained,total_max,percentage,grade,remark,status):
   
    print("\n")
    print("=" * 58)
    print("                     REPORT CARD")
    print("=" * 58)

    print("Student Name :", name)

    print("\n+----+----------------+-----------+----------+")
    print("|No. | Subject        | Max Marks | Obtained |")
    print("+----+----------------+-----------+----------+")

    for i in range(len(subjects)):
        print(f"|{i+1:<4}|{subjects[i][0]:<16}|{subjects[i][1]:<11}|{subjects[i][2]:<10}|")

    print("+----+----------------+-----------+----------+")

    print(f"\nTotal Obtained : {total_obtained}")
    print(f"Total Maximum  : {total_max}")
    print(f"Percentage     : {percentage:.2f}%")
    print(f"Grade          : {grade}")
    print(f"Remarks        : {remark}")
    print(f"Result         : {status}")

    print("=" * 58)

#MAIN PROGRAMME
name, subjects, total_obtained, total_max, percentage = student_data()

grade = grade_value(percentage)
remark = remarks(percentage)
status = result(subjects)

display_report(name, subjects, total_obtained, total_max, percentage, grade, remark, status)
