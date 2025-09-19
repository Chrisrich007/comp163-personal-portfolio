#1. Personal Information (strings)
full_name = "Christopher Arnold"
student_email = "crarnold@ncat.edu"
hometown = "Wake Forest, NC"
graduation_semester = "Spring 2029"
major = "Computer Science"

#2. Academic Data (lists)
current_courses = ["COMP 163", "MATH 131", "ENG 119", "HIS 103"]
completed_courses = ["Biology", "Chemistry", "Calculus", "Spanish 1I", "World History"]
credit_hours_list = [3, 3, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]

#3. Contact Information (tuples) - aaccess by index only 
emergency_contact = ("Mom", "Shelly", "342-423-1343")
home_address = ("234 Croodstaff Ave", "Raliegh, NC", "45734")
instagram_info = ("Instagram", "@chrisrich2007", 312)
twitter_info = ("Twitter", "@chrisrich2007", 127)
birthday_info = ("Birthday", 8, 27, 2007)

#4. Interest Tracking (sets)
current_skills_set = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn_set = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests_set = {"Software development", "Web development", "Data science", "Game development"}
hobbies_set = {"Gaming", "Photography", "Reading", "Soccer", "Music" }
entertainment_backlog_set = {"Naruto", "Barry", "Life", "Incantation", "Memento"}

#5. Organizational Mapping (dictionaries)
course_credits_dict = {"COMP 163":3, "MATH 131": 3, "ENG 119": 3, "HIS 103": 3}
course_professors_dict = {"COMP 163": "Prof. Rhodes", "MATH 131": "Prof. Gibson", "ENG 119": "Prof. George", "HIS 103": "Prof. Ndege"}
course_rooms_dict = {"COMP 163": "Mcnair 300", "MATH 131": "Marteena 201", "ENG 119": "Academic Building 121", "HIS 103": "Obline"}
monthly_budget_dict = {"Food": 30, "Entertainment": 0, "Books": 10, "Transportation": 30}
study_hours_per_subject_dict = {"Programming": 10, "Math": 8, "English":4, "History": 3}
contact_directory_dict = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisory": "336-334-5000"}

#6. Required Calulations

total_current_credits = sum(credit_hours_list)

cumulative_gpa = sum(gpa_history) / len(gpa_history)
cumulative_gpa_rounded = round(cumulative_gpa, 2)
completed_courses_count = len(completed_courses)

total_weekly_study_hours = sum(study_hours_per_subject_dict["Programming"] +
study_hours_per_subject_dict["Math"] +
study_hours_per_subject_dict["English"] +
study_hours_per_subject_dict["History"]
for _ in (0,))

total_weekly_study_hours = (study_hours_per_subject_dict["Programming"] +
study_hours_per_subject_dict["Math"] +
study_hours_per_subject_dict["English"] +
study_hours_per_subject_dict["History"])

academic_load = total_current_credits + total_weekly_study_hours
monthly_budget_total = (monthly_budget_dict["Food"] + 
monthly_budget_dict["Entertainment"] +
monthly_budget_dict["Books"] +
monthly_budget_dict["Transportation"])

daily_food_budget = round(monthly_budget_dict["Food"] / 30, 2)

annual_budget_projections = monthly_budget_total * 12
study_cost_per_hour = round(monthly_budget_dict["Books"] / total_weekly_study_hours, 2)

#7. Analytics Calculations
instagram_followers = instagram_info[2]
twitter_followers = twitter_info[2]
total_social_media_followers = instagram_followers + twitter_followers

current_skills_count = len(current_skills_set)
skills_to_learn_count = len(skills_to_learn_set)

contact_directory_size = len(contact_directory_dict)

entertainment_backlog_count = len(entertainment_backlog_set)

average_study_hours_per_credit = round(total_weekly_study_hours / total_current_credits, 2)

#Output: Professionally formatted display using f-strings 
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")

# Personal Info

print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating : {graduation_semester}\n")
print(f"Major: {major}\n")

# Academic Data
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_gpa_rounded}")
print(f"Weekly Study Time: {total_weekly_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour\n")

print("Current Courses:")
print(f"{current_courses[0]} - {course_credits_dict['COMP 163']} credits - {course_professors_dict['COMP 163']} - {course_rooms_dict['COMP 163']}")
print(f"{current_courses[1]} - {course_credits_dict['MATH 150']} credits - {course_professors_dict['MATH 150']} - {course_rooms_dict['MATH 150']}")
print(f"{current_courses[2]} - {course_credits_dict['ENG 101']} credits - {course_professors_dict['ENG 101']} - {course_rooms_dict['ENG 101']}")
print(f"{current_courses[3]} - {course_credits_dict['HIS 105']} credits - {course_professors_dict['HIS 105']} - {course_rooms_dict['HIS 105']}\n")

# === PERSONAL DEVELOPMENT ===
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills_set}")
print(f"Learning Goals: {skills_to_learn_set}")
print(f"Career Interests: {career_interests_set}")
print(f"Skills Currently Have: {current_skills_count}")
print(f"Skills Want to Learn: {skills_to_learn_count}\n")

# === FINANCIAL OVERVIEW ===
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget_dict['Food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget_dict['Entertainment']}")
print(f"Books: ${monthly_budget_dict['Books']}")
print(f"Transportation: ${monthly_budget_dict['Transportation']}")
print(f"Annual Projection: ${annual_budget_projections}\n")

# === CONNECTIONS & CONTACTS ===
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]}")
print(f"Social Media Presence: {total_social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_directory_size} people in directory\n")

# === LIFE STATISTICS ===
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {entertainment_backlog_count} items")
print(f"Current Hobbies: {len(hobbies_set)} activities")

print("================================================================")




