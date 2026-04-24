from datetime import datetime

students = {}

def add_student(name, age, grade):
    students[name] = {'age': age, 'grade': grade}
    print(f'{name} has been added to the students')
    log_action(f'Student {name} added')

def view_student():
    if len(students) != 0:
        for key, value in students.items():
            print(f'Name: {key} | Age: {value["age"]} | Grade: {value["grade"]}')
            log_action(f'Student {key} viewed')
    else:
        print('Students list is empty')

def save_records():
    with open("students.txt", "w") as file:
        for key, value in students.items():
            file.write(f"{key},{value['age']},{value['grade']}\n")
    print('Records saved successfully')
    log_action('Students record saved')

def load_records():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                add_student(parts[0], int(parts[1]), parts[2])
        log_action('Records loaded')
    except FileNotFoundError:
        print('Records not found')

def log_action(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("log.txt", "a") as file:
        file.write(f"{now} - {message}\n")

while True:
    print('\n--- Student Record System ---')
    print('1. Add student')
    print('2. View students')
    print('3. Save records')
    print('4. Load records')
    print('5. Exit')
    
    choice = input('Enter your choice: ')
    
    if choice == '1':
        name = input('Enter student name: ')
        age = int(input('Enter student age: '))
        grade = input('Enter student grade: ')
        add_student(name, age, grade)
    
    elif choice == '2':
        view_student()
        
    elif choice == '3':
        save_records()
        
    elif choice == '4':
        load_records()
        
    elif choice == '5':
        print('Goodbye!')
        break
    
    else:
        print('Invalid choice')
