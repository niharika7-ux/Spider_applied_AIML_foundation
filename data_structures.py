# Examples of list, tuple, set, and dictionary

weekly_tasks = ["revise Python", "finish lab work", "practise questions"]
fixed_days = ("Monday", "Wednesday", "Friday")
unique_topics = {"loops", "functions", "loops", "lists"}
study_hours = {"Monday": 2, "Tuesday": 1.5, "Wednesday": 2}

weekly_tasks.append("review notes")
study_hours["Thursday"] = 1

print("Task list:", weekly_tasks)
print("First task:", weekly_tasks[0])
print("Study days:", fixed_days)
print("Unique topics:", unique_topics)
print("Study hours:", study_hours)

print("\nHours planned each day:")
for day, hours in study_hours.items():
    print(f"{day}: {hours} hour(s)")
