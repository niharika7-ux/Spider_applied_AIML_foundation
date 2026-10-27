# Writing to and reading from a text file

from pathlib import Path

file_path = Path("practice_notes.txt")
notes = [
    "Python practice notes",
    "Functions help us reuse code.",
    "Files can keep information after a program ends."
]

file_path.write_text("\n".join(notes), encoding="utf-8")
print("Notes saved to:", file_path.resolve())

saved_text = file_path.read_text(encoding="utf-8")
print("\nFile contents:")
print(saved_text)

with file_path.open("a", encoding="utf-8") as file:
    file.write("\nRemember to practise a little every day.")

print("\nA final reminder was added to the file.")
