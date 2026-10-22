# 21. Find students enrolled in both courses and students enrolled in only one course.

python_students = {"Amit", "Bhakti", "Sneha", "Rahul"}
java_students = {"Bhakti", "Rahul", "Priya", "Neha"}

both_courses = python_students.intersection(java_students)
only_one_course = python_students.symmetric_difference(java_students)

print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)