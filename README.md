# locally
git clone https://github.com/<your-github-username>/comp163-personal-portfolio.git
cd comp163-personal-portfolio

# add the file with test data (Part 1)
cp /path/to/your/username_assignment_3.py .     # or create file directly
git add username_assignment_3.py
git commit -m "Initial portfolio with test data from Part 1"
git push origin main
# edit strings in username_assignment_3.py
git add username_assignment_3.py
git commit -m "Update personal information with real data"
git push origin main
# update current_courses, completed_courses, credit_hours_list, gpa_history
git add username_assignment_3.py
git commit -m "Add real academic data and course information"
git push origin main
# update current_skills_set, skills_to_learn_set, career_interests_set, hobbies_set
git add username_assignment_3.py
git commit -m "Customize skills, interests, and career goals"
git push origin main
# update monthly_budget_dict, study_hours_per_subject_dict, contact_directory_dict
git add username_assignment_3.py
git commit -m "Add personal budget and contact information"
git push origin main
git add README.md
git commit -m "Add professional project documentation"
git push origin main

# Assignment 3 - Personal Portfolio

## Author
Christopher Arnold - COMP 163, Fall 2025  
Email: crar@ncat.edu

## Description
This Python program demonstrates mastery of Chapter 3 data types (strings, lists, tuples, sets, dictionaries) by organizing a personal college life portfolio and performing required calculations and analytics.

## Features
- Stores personal and academic information using strings, lists, tuples, sets, and dictionaries.
- Calculates total credits, cumulative GPA, weekly study time, daily food budget, annual projection, and study cost per hour.
- Produces a formatted profile output (Academic Profile, Personal Development, Financial Overview, Connections & Contacts, Life Statistics).
- Uses no functions, loops, or conditionals (per assignment requirement).

## How to Run
1. Ensure Python 3 is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/<your-github-username>/comp163-personal-portfolio.git
   cd comp163-personal-portfolio

python username_assignment_3.py
