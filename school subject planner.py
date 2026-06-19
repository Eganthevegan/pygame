student_profile = ("Aarav", "Grade 6", "Section A", 6)

print("Student Name:", student_profile[0])
print("Grade & Section:", student_profile[1:3])

monday_subjects = {"Math", "Science", "English", "Computer", "Art"}
tuesday_subjects = {"Math", "History", "English", "Sports", "Music"}

monday_subjects.add("Coding")
tuesday_subjects.discard("Music")

all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects)

print("\n--- Planner Summary ---")
print("All unique subjects across two days:", all_subjects)
print("Subjects present on both days:", common_subjects)