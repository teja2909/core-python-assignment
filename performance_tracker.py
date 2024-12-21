class Student:
    def __init__(self,students):
        self.students=students
    def avg_marks(self):
        averages={}
        for name,marks in self.students.items():
            avg=round(sum(marks)/len(marks),2)
            averages[name]=avg
        return averages
    def top_performer(self):
        averages=self.avg_marks()
        topper=max(averages,key=averages.get)
        return f"Top Performer:{topper}"
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
std=Student(students)
print(std.avg_marks())
print(std.top_performer())