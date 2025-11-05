class Lesson:
    def __init__(self, name, credit, lesson_number,score_announcement=False, score=None):
        self.name = name
        self.credit = credit
        self.lesson_number = lesson_number
        self.score_announcement = score_announcement
        self.score = score
    def set_score(self, score):
        self.score = score
        self.score_announcement = True
    def __str__(self):
        return f"Lesson(Name: {self.name}, Credit: {self.credit}, Number: {self.lesson_number}, Score: {self.score if self.score_announcement else 'Not Announced'})"
    def __repr__(self):
        return self.__str__()

class Student:
    def __init__(self, name, birthday, student_id):
        self.name = name
        self.birthday = birthday
        self.student_id = student_id
        self.lessons = []

    def add_lesson(self, lesson):
        if lesson not in self.lessons:
            self.lessons.append(lesson)
        else:
            print(f"Lesson {lesson.name} already exists in the student's lessons.")
    
    def calc_avg(self):
        total_score = 0
        count = 0
        for lesson in self.lessons:
            if lesson.score_announcement:
                total_score += lesson.score
                count += 1
        if count == 0:
            return 0
        return total_score / count
    
    def show_current_lessons(self):
        print("------------------------------------")
        total_credits = 0
        print("Current Lessons without announced score:")
        for lesson in self.lessons:
            if not lesson.score_announcement:
                print(f"- {lesson.name} ({lesson.credit} credits)")
                total_credits += lesson.credit
        print(f"Total Credits (Unscored Lessons): {total_credits}")

    def show_all_lessons(self):
        print("------------------------------------")
        for lesson in self.lessons:
            print(f"Lesson: {lesson.name}, Credit: {lesson.credit}, Score: {lesson.score if lesson.score_announcement else 'Not Announced'}")
        
        print(f"Average Score: {self.calc_avg()}")
    
    def edit_score(self, lesson_id, new_score):
        print("------------------------------------")
        for lesson in self.lessons:
            if lesson.lesson_number == lesson_id:
                lesson.set_score(new_score)
                print(f"Score for {lesson_id} updated to {new_score}.")
                return
        print(f"Lesson {lesson_id} not found.")

    def delete_lesson(self, lesson_id):
        print("------------------------------------")
        for lesson in self.lessons:
            if lesson.lesson_number == lesson_id:
                self.lessons.remove(lesson)
                print(f"Lesson {lesson_id} deleted.")
                return
        print(f"Lesson {lesson_id} not found.")
    
    def __str__(self):
        print("------------------------------------")
        return f"Student(Name: {self.name}, Birthday: {self.birthday}, ID: {self.student_id})"
    def __repr__(self):
        return self.__str__()


math = Lesson("Math", 3, 101)
physics = Lesson("Physics", 4, 102)
chemistry = Lesson("Chemistry", 3, 103)
history = Lesson("History", 2, 104)
english = Lesson("English", 3, 105)

amir = Student("Amir", "2000-01-01", 1)
amir.add_lesson(math)
amir.add_lesson(physics)
amir.add_lesson(chemistry)
amir.show_all_lessons()

hossein = Student("Hossein", "2000-02-02", 2)
hossein.add_lesson(math)
hossein.add_lesson(english)
hossein.add_lesson(history)
hossein.show_all_lessons()

math.set_score(15)
print("set")
hossein.show_all_lessons()
amir.show_all_lessons()
print("")
hossein.edit_score(101, 20)
hossein.show_all_lessons()
amir.show_all_lessons()
