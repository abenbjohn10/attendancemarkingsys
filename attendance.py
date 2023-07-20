import datetime

def mark_attendance(attendance_dict, employee_name):
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")

    if employee_name in attendance_dict:
        if date_str in attendance_dict[employee_name]:
            print(f"{employee_name} has already marked attendance for today.")
        else:
            attendance_dict[employee_name].append(date_str)
            print(f"{employee_name} marked attendance for {date_str}.")
    else:
        attendance_dict[employee_name] = [date_str]
        print(f"{employee_name} marked attendance for {date_str}.")

def main():
    attendance = {}
    while True:
        print("\nAttendance Management System")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            employee_name = input("Enter your name: ")
            mark_attendance(attendance, employee_name)
        elif choice == '2':
            employee_name = input("Enter employee name to view attendance: ")
            if employee_name in attendance:
                print(f"{employee_name} attendance:")
                for date in attendance[employee_name]:
                    print(date)
            else:
                print(f"No attendance records found for {employee_name}.")
        elif choice == '3':
            print("Exiting the Attendance Management System.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
