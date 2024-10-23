import random
from typing import List, Tuple, Dict
import pandas as pd

class PeerReviewAssigner:
    def __init__(self, students: List[Tuple[str, str, str]]):
        self.students = students
        self.student_numbers = [student[2] for student in students]
        self.assignments = {}
        
    def assign_peer_reviews(self, reviews_per_student: int = 3) -> Dict[str, List[str]]:
        self.assignments = {student_num: [] for student_num in self.student_numbers}
        
        for _ in range(reviews_per_student):
            available_assignments = self.student_numbers.copy()
            students_needing_reviews = self.student_numbers.copy()
            
            while students_needing_reviews:
                current_student = students_needing_reviews.pop(0)
                possible_assignments = [x for x in available_assignments 
                                     if x != current_student and 
                                     x not in self.assignments[current_student]]
                
                if not possible_assignments:
                    return self.assign_peer_reviews(reviews_per_student)
                
                selected_assignment = random.choice(possible_assignments)
                self.assignments[current_student].append(selected_assignment)
                available_assignments.remove(selected_assignment)
                
        return self.assignments
    
    def export_to_csv(self, filename: str = "peer_review_assignments.csv"):
        rows = []
        for student in self.students:
            first_name, last_name, student_num = student
            assigned_reviews = self.assignments.get(student_num, [])
            while len(assigned_reviews) < 3:
                assigned_reviews.append('')
                
            row = {
                'First Name': first_name,
                'Last Name': last_name,
                'Student Number': student_num,
                'Review Assignment 1': assigned_reviews[0],
                'Grade 1': '',
                'Review Assignment 2': assigned_reviews[1],
                'Grade 2': '',
                'Review Assignment 3': assigned_reviews[2],
                'Grade 3': ''
            }
            rows.append(row)
            
        df = pd.DataFrame(rows)
        df.to_csv(filename, index=False)
        return filename

def main():
    students = [
        ("Ezekiel", "Stone", "2024101"),
        ("Zephyr", "Rayne", "2024102"),
        ("Atlas", "Phoenix", "2024103"),
        ("Nova", "Blackwood", "2024104"),
        ("Quest", "Sterling", "2024105"),
        ("Sage", "Winters", "2024106"),
        ("Echo", "Rivers", "2024107"),
        ("Orion", "Drake", "2024108"),
        ("Genesis", "Frost", "2024109"),
        ("Phoenix", "Storm", "2024110"),
        ("Raven", "Nightshade", "2024111"),
        ("Azure", "Skye", "2024112"),
        ("Lyric", "Moon", "2024113"),
        ("Zenith", "Steele", "2024114"),
        ("Onyx", "Shadow", "2024115")
    ]
    
    assigner = PeerReviewAssigner(students)
    assignments = assigner.assign_peer_reviews(3)
    csv_file = assigner.export_to_csv()
    
    print("\nPeer Review Assignments:")
    for student_num, reviews in assignments.items():
        student_name = next(s[0] + " " + s[1] for s in students if s[2] == student_num)
        print(f"\n{student_name} (#{student_num}) will review assignments from:")
        for review_num in reviews:
            reviewer_name = next(s[0] + " " + s[1] for s in students if s[2] == review_num)
            print(f"- {reviewer_name} (#{review_num})")

if __name__ == "__main__":
    main()