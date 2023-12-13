# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

marks = []
for _ in range(m):
    marks.append(list(map(float, input().split())))

for student_marks in zip(*marks):
    average = sum(student_marks) / m
    print("{:.1f}".format(average))
