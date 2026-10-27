# Extra practice: calculate a student's marks summary

def get_average(marks):
    return sum(marks) / len(marks) if marks else 0


def main():
    name = input("Enter student name: ").strip() or "Student"
    marks = []

    for subject_number in range(1, 4):
        while True:
            try:
                score = float(input(f"Enter marks for subject {subject_number}: "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a number.")

    average = get_average(marks)
    print("\n--- Marks Summary ---")
    print("Student:", name)
    print("Marks:", marks)
    print(f"Average: {average:.2f}/100")
    print("Overall result:", "Pass" if all(mark >= 40 for mark in marks) else "Needs improvement")


if __name__ == "__main__":
    main()
