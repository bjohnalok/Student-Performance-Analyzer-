class StudentRecords:
    def __init__(self):
        self.records = {}

    def add_record(self, student_id, subjects):
        self.records[student_id] = subjects

    def update_record(self, student_id, subjects):
        if student_id in self.records:
            self.records[student_id] = subjects
        else:
            print("Student ID not found in records.")

    def delete_record(self, student_id):
        if student_id in self.records:
            del self.records[student_id]
        else:
            print("Student ID not found in records.")

    def calculate_total_marks(self, student_id):
        if student_id in self.records:
            total_marks = sum(self.records[student_id].values())
            return total_marks
        else:
            print("Student ID not found in records.")
            return None

    def calculate_percentage(self, student_id):
        if student_id in self.records:
            total_marks = self.calculate_total_marks(student_id)
            percentage = (total_marks / (len(self.records[student_id]) * 100)) * 100
            return percentage
        else:
            print("Student ID not found in records.")
            return None

    def calculate_rank(self, student_id):
        if student_id in self.records:
            student_percentage = self.calculate_percentage(student_id)
            rank = 1
            for sid, subjects in self.records.items():
                if sid != student_id:
                    if self.calculate_percentage(sid) > student_percentage:
                        rank += 1
            return rank
        else:
            print("Student ID not found in records.")
            return None

# Example
student_records = StudentRecords()
student_records.add_record("01", {"Maths": 90, "Science": 85, "English": 88})
student_records.add_record("02", {"Maths": 95, "Science": 92, "English": 89})

# Print records of all students at once
for student_id, subjects in student_records.records.items():
    total_marks = student_records.calculate_total_marks(student_id)
    percentage = student_records.calculate_percentage(student_id)
    rank = student_records.calculate_rank(student_id)
    
    print(f"Student {student_id}: Total Marks - {total_marks}, Percentage - {percentage}%, Rank - {rank}")
