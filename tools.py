COURSES = {
 1: [("MS-251", "Probability & Statistics", 3.0),
 ("GE-160", "Applications of ICT", 3.0),
 ("GE-169", "Applied Physics", 3.0),
 ("GE-167", "Discrete Structures", 3.0),
 ("HQ-001", "Quran Translation - I", 0.5),
 ("GE-190", "Functional English", 3.0)],
 2: [("CC-112", "Programming Fundamentals", 3.0),
 ("CC-112-L", "Programming Fundamentals Lab", 1.0),
 ("CC-110", "Digital Logic Design", 2.0),
 ("CC-110-L", "Digital Logic Design Lab", 1.0),
 ("MS-252", "Linear Algebra", 3.0),
 ("GE-191", "Expository Writing", 3.0),
 ("GE-163", "Islamic Studies", 2.0),
 ("HQ-002", "Quran Translation - II", 0.5)],
 3: [("CC-211", "Object Oriented Programming", 3.0),
 ("CC-211-L", "Object Oriented Programming Lab", 1.0),
 ("CC-215", "Database Systems", 3.0),
 ("CC-215-L", "Database Systems Lab", 1.0),
 ("CC-210", "Computer Organization & Assembly Language", 3.0),
 ("GE-162", "Calculus & Analytical Geometry", 3.0),
 ("GE-192", "Introduction to Management", 2.0),
 ("HQ-003", "Quran Translation - III", 0.5)],
 4: [("CC-213", "Data Structures", 3.0),
 ("CC-213-L", "Data Structures Lab", 1.0),
 ("CC-312", "Information Security", 3.0),
 ("CC-214", "Computer Networks", 3.0),
 ("CC-212", "Software Engineering", 3.0),
 ("DC-220", "Advanced Database Management Systems", 3.0),
 ("HQ-004", "Quran Translation - IV", 0.5)],
 5: [("CC-313", "Analysis of Algorithms", 3.0),
 ("CC-310", "Artificial Intelligence", 3.0),
 ("DC-320", "Theory of Automata and Formal Languages", 3.0),
 ("DC-321", "Human Computer Interaction", 3.0),
 ("DC-322", "Computer Architecture", 3.0),
 ("EC-330", "Web Technologies / Elective", 3.0),
 ("HQ-005", "Quran Translation - V", 0.5)],
 6: [("CC-311", "Operating Systems", 3.0),
 ("EC-333", "Mobile Application Development / Elective", 3.0),
 ("EC-324", "Software Construction & Development / Elective", 3.0),
 ("EC-335", "Machine Learning / Elective", 3.0),
 ("EC-334", "Game Design and Development / Elective", 3.0),
 ("MS-253", "Multivariable Calculus", 3.0),
 ("HQ-006", "Quran Translation - VI", 0.5)],
 7: [("CC-411", "Final Year Project - I", 2.0),
 ("DC-328", "Parallel & Distributed Computing", 3.0),
 ("EC-345", "Computer Vision / Elective", 3.0),
 ("EC-425", "Software Quality Engineering / Elective", 3.0),
 ("MS-254", "Technical and Business Writing", 3.0),
 ("GE-263", "Entrepreneurship", 2.0),
 ("GE-262", "Professional Practices", 2.0),
 ("HQ-007", "Quran Translation - VII", 0.5)],
 8: [("CC-412", "Final Year Project - II", 4.0),
 ("DC-421", "Compiler Construction", 3.0),
 ("UE-272", "Introduction to Marketing", 3.0),
 ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
 ("GE-363", "Civics and Community Engagement", 2.0),
 ("HQ-008", "Quran Translation - VIII", 0.5)],
}


def marks_to_grade_points(marks: int) -> float | str:
    """Use this tool when student's marks need to be converted into grade points"""
    if marks<0 or marks>100:
        return "Error: marks out of range"
    elif marks>=85:
        return 4.0
    elif marks>=80:
        return 3.7
    elif marks>=75:
        return 3.3
    elif marks>=70:
        return 3.0
    elif marks>=65:
        return 2.7
    elif marks>=61:
        return 2.3
    elif marks>=58:
        return 2.0
    elif marks>=55:
        return 1.7
    elif marks>=50:
        return 1.0
    else:
        return 0.0


def calculate_semester_gpa(grade_points: list[float],credit_hours: list[float]) -> float | str:
    """Use this tool when the semester gpa needs to be calculated if the grade points and credit hours are given
    If marks are given instead of grade points, run the marks_to_grade_points tool"""
    if len(grade_points)==0 or len(credit_hours)==0:
        return "Error: Lists cannot be empty"
    if len(grade_points)!=len(credit_hours):
        return "Error: Invalid input"
    for i in range(len(grade_points)):
        if grade_points[i]<0.0:
            return "Error: Grade points cannot be negative"
    for i in range(len(credit_hours)):
        if credit_hours[i]<0.5 or credit_hours[i]>3:
         return "Error: Invalid credit hours"
    total_credit_hrs= sum(credit_hours)
    if total_credit_hrs<=0 or total_credit_hrs>134:
        return "Error: Invalid Total Credit Hours"
    sem_gpa=0.0
    for i in range(len(grade_points)):
        sem_gpa+=(grade_points[i]*credit_hours[i])
    sem_gpa=sem_gpa/total_credit_hrs
    return sem_gpa

def calculate_new_cgpa(current_cgpa:
float, completed_ch: float, semester_gpa: float,
semester_ch: float) -> float|str:
    """Use this tool when current cgpa, completed credit hours , semester GPA and semester 
    credit hours are given to calculate student's new CGPA
    """
    if completed_ch<0.5:
        return "Error: Invalid Completed Credit Hrs"
    if current_cgpa<0.0 or current_cgpa>4.0:
         return "Error: Current CGPA out of range"
    if semester_gpa<0.0 or semester_gpa>4.0:
         return "Error: Semester GPA out of range"
    if semester_ch<0.5:
         return "Error: Invalid Semester Credit Hrs"

    new_cgpa=(current_cgpa * completed_ch + semester_gpa * semester_ch)/ (completed_ch+semester_ch)
    return new_cgpa

def required_gpa_for_target(target_cgpa:
float, current_cgpa: float, completed_ch: float,
remaining_ch: float) -> float | str:
    """Use this tool when target cgpa , current cgpa , completed credit hours and remaining credit hours
    are given to calculate student's required gpa for target """
    if target_cgpa<=0.0 or target_cgpa>4.0:
        return "Error : Invalid target CGPA"
    if current_cgpa<0.0 or current_cgpa>4.0:
        return "Error: Current CGPA out of range"
    if completed_ch<=0.0 or completed_ch>134:
        return "Error: Invalid Completed Credit Hrs"
    if remaining_ch<0.5:
        return "Error: Invalid Input"
    
    required_gpa=(target_cgpa *(completed_ch + remaining_ch) - current_cgpa * completed_ch) / remaining_ch
    return required_gpa

def get_semester_courses(semester: int) -> str:
    """Use this tool when a student asks for semester details like code, name or credit hours for a specific semester"""
    if semester<1 or semester>8:
        return "Error: Semester must be between 1 and 8"
    course = COURSES[semester]
    res = f"Semester {semester} courses:\n"
    for code, name, credits in course:
        res += f"{code}: {name} - {credits} credits\n"
    return res
    

def get_remaining_credit_hours(current_semester: int) -> float | str:
     """Use this tool when students asks to get remaining credit hours"""
     if current_semester<1 or current_semester>8:
            return "Error: Current Semester must be between 1 and 8"
     rem_ch=0

     for sem in range(current_semester,9):
         for code, name, credits in COURSES[sem]:
             rem_ch+=credits
     return rem_ch

def save_report(filename: str, content: str) -> str:
    """Use this tool when a student asks to save a worth-keeping GPA or CGPA result"""
    if not filename:
        return "Error: Empty file cannot be accepted"
    if not content:
        return "Error : Empty content cannot be saved"
    try:
        with open(filename, "w") as file:
            file.write(content)

        return f"Report saved successfully to {filename}"

    except Exception as e:
        return f"Error: could not save report - {e}"

#  Test marks_to_grade_points
# print("marks_to_grade_points(90):", marks_to_grade_points(90))      
# print("marks_to_grade_points(84):", marks_to_grade_points(84))       
# print("marks_to_grade_points(-5):", marks_to_grade_points(-5))  


# # Test calculate_semester_gpa
# print("semester_gpa normal:", calculate_semester_gpa([4.0, 2.7, 3.0], [3.0, 3.0, 3.0]))  
# print("semester_gpa empty:", calculate_semester_gpa([], []))                            
# print("semester_gpa mismatch:", calculate_semester_gpa([4.0, 3.0], [3.0]))              

# # Test calculate_new_cgpa
# print("new_cgpa normal:", calculate_new_cgpa(3.0, 60, 3.6, 15))       
# print("new_cgpa bad current:", calculate_new_cgpa(5.0, 60, 3.6, 15)) 

# # Test required_gpa_for_target
# print("required_gpa V only:", required_gpa_for_target(3.4, 3.0, 64.0, 18.5)) 
# print("required_gpa V-VI:", required_gpa_for_target(3.4, 3.0, 64.0, 37.0))     
# print("required_gpa V-VII:", required_gpa_for_target(3.4, 3.0, 64.0, 55.5))    

# # Test get_semester_courses
# print(get_semester_courses(5))     
# print(get_semester_courses(9))    

# # Test get_remaining_credit_hours
# print("remaining sem5:", get_remaining_credit_hours(5))   
# print("remaining sem8:", get_remaining_credit_hours(8))  
# print("remaining sem0:", get_remaining_credit_hours(0))  

# # Test save_report
# print(save_report("test_report.txt", "This is a test report."))
# print(open("test_report.txt").read()) 