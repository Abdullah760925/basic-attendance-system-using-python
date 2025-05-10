# Initialize an empty dictionary to store attendance
att_system = {}

# Input total number of students
total_students = int(input("Enter the total number of students in the class: "))

# Collect attendance using roll numbers
for i in range(1, total_students + 1):
    roll_no = input(f"Enter the roll number of student {i}: ")
    status = input(f"Enter the status (P for Present / A for Absent) for Roll No {roll_no}: ").lower()
    
    # Make sure the status is either 'P' or 'A'
    while status not in ['p', 'a']:
        print("Invalid input! Please enter 'P' for Present or 'A' for Absent.")
        status = input(f"Enter the status (P for Present / A for Absent) for Roll No {roll_no}: ").lower()

    # Store the attendance with roll number as key
    att_system[roll_no] = status

# Print attendance marked successfully
print("Attendance has been marked successfully!")

# Function to display all absent students
def show_absent_students():
    print("List of absent students (Roll Numbers):")
    absent_students = []
    for roll_no, status in att_system.items():
        if status == 'a':
            absent_students.append(roll_no)
    
    if absent_students:
        print(", ".join(absent_students))
    else:
        print("No students are absent.")

# Function to count present and absent students
def count_attendance():
    present_count = 0
    absent_count = 0
    
    for status in att_system.values():
        if status == 'p':
            present_count += 1
        elif status == 'a':
            absent_count += 1
    
    print(f"Total Present Students: {present_count}")
    print(f"Total Absent Students: {absent_count}")

# Display the list of absent students
show_absent_students()

# Display the count of present and absent students
count_attendance()
