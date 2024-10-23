# Peer-Review-Assigner
Peer Review Assigner Pseudocode

Class PeerReviewAssigner

Initialize(students_list):
- Store list of students (each containing first name, last name, student number)
- Extract student numbers into separate list
- Create empty dictionary for assignments

AssignPeerReviews(number_of_reviews_per_student):
- Create empty assignments dictionary with student numbers as keys

    FOR each review round (1 to number_of_reviews_per_student):
    - Create copy of all student numbers as available_assignments
    - Create copy of all student numbers as students_needing_reviews

        WHILE students_needing_reviews is not empty:
        - Get first student from students_needing_reviews

        - Find possible assignments where:
            - Assignment is in available_assignments
            - Assignment is not the current student
            - Assignment hasn't been already assigned to current student

        IF no possible assignments exist:
            - Start over with AssignPeerReviews (recursive call)

        - Randomly select one assignment from possible assignments
        - Add selected assignment to current student's assignment list
        - Remove selected assignment from available_assignments

- RETURN assignments dictionary

ExportToCSV(filename):
- Create empty list for rows

    FOR each student in students list:
    - Get assigned reviews for student
    - IF assigned reviews less than 3:
        - Fill remaining slots with empty strings

    - Create row dictionary with:
        - First Name
        - Last Name
        - Student Number
        - Review Assignment 1, 2, 3
        - Grade 1, 2, 3 (empty)

    - Add row to rows list

- Convert rows to DataFrame
- Save DataFrame to CSV file
- RETURN filename

Main Program Flow
- Define list of students with:
    - First Name
    - Last Name
    - Student Number

- Create PeerReviewAssigner instance with students list
- Generate peer review assignments (3 per student)
- Export assignments to CSV

- Print assignments:
    FOR each student and their assigned reviews:
    - Print student name and number
    - FOR each assigned review:
        - Print reviewer name and number
