# 17. Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.

student1 = {"Python", "Java", "DBMS", "OS"}
student2 = {"Python", "C++", "DBMS", "CN"}

common_subjects = student1.intersection(student2)

print("Subjects studied by both students:", common_subjects)