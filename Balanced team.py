n = int(input())
skills = list(map(int, input().split()))
 
skills.sort()
 
left = 0
right = 0
max_students = 0
 
while right < n:
    while skills[right] - skills[left] > 5:
        left += 1
    max_students = max(max_students, right - left + 1)
    right += 1
 
print(max_students)
