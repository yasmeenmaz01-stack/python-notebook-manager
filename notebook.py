import json
from datetime import datetime

# -----------------------------------
# Load notes from JSON file
# -----------------------------------
def load_notes(filename="notes.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# -----------------------------------
# Save notes to JSON file
# -----------------------------------
def save_notes(notes, filename="notes.json"):
    with open(filename, "w") as f:
        json.dump(notes, f, indent=4)
    print("Notes saved successfully!")


# -----------------------------------
# Add a new note
# -----------------------------------
def add_note(notes):
    print("\n--- Add a New Note ---")

    title = input("Enter title: ")
    content = input("Enter content: ")
    tags_input = input("Enter tags separated by commas: ")
    tags = [tag.strip() for tag in tags_input.split(",")]

    date = datetime.now().strftime("%d-%m-%y")

    note = {
        "title": title,
        "content": content,
        "tags": tags,
        "date": date
    }

    notes.append(note)
    print("The Note was added successfully!")


# -----------------------------------
# Show all notes
# -----------------------------------
def show_notes(notes):
    if not notes:
        print("No notes available.")
        return

    for i, note in enumerate(notes):
        print(f"\nNote {i + 1}:")
        print("Title:", note["title"])
        print("Content:", note["content"])
        print("Tags:", ", ".join(note["tags"]))
        print("Date:", note["date"])

#------------------------------------
#Search notes by keyword
#------------------------------------
def search_notes(notes):
    keyword = input("Enter keyword to search: ").lower()
    found = False

    for i, note in enumerate(notes):
        if keyword in note["title"].lower() or keyword in note["content"].lower():
            found = True
            print(f"\nNote {i+1}:")
            print("Title:", note["title"])
            print("Content:", note["content"])
            print("Tags:", ", ".join(note["tags"]))

    if not found:
        print("No notes found with that keyword.")
#-------------------------------------------------
#Filter notes by tag
#-------------------------------------------------
def filter_by_tag(notes):
    tag = input("Enter tag to filter by: ").lower()
    found = False

    for i, note in enumerate(notes):
        tags_lower = [t.lower() for t in note["tags"]]
        if tag in tags_lower:
            found = True
            print(f"\nNote {i+1}:")
            print("Title:", note["title"])
            print("Content:", note["content"])
            print("Tags:", ", ".join(note["tags"]))

    if not found:
        print("No notes found with that tag.")
#---------------------------------------------------
#Edit an existing note
#---------------------------------------------------
def edit_note(notes):
    show_notes(notes)
    index = int(input("Enter note number to edit: ")) - 1

    if 0 <= index < len(notes):
        note = notes[index]

        new_title = input(f"New title (leave empty to keep '{note['title']}'): ")
        new_content = input(f"New content (leave empty to keep current): ")
        new_tags = input("New tags (comma separated, leave empty to keep current): ")

        if new_title:
            note["title"] = new_title
        if new_content:
            note["content"] = new_content
        if new_tags:
            note["tags"] = [t.strip() for t in new_tags.split(",")]

        print("Note updated!")
    else:
        print("Invalid note number.")
#-------------------------------------------------------
#Delete a note
#------------------------------------------------------
def delete_note(notes):
    show_notes(notes)
    index = int(input("Enter note number to delete: ")) - 1

    if 0 <= index < len(notes):
        notes.pop(index)
        print("Note deleted!")
    else:
        print("Invalid note number.")
#------------------------------------------------



# -----------------------------------
# Main Menu
# -----------------------------------
def main():
    notes = load_notes()

    while True:
        print("\n--- Notebook Manager ---")
        print("1. Add Note")
        print("2. Show Notes")
        print("3. Search Notes")
        print("4. Filter by Tag")
        print("5. Edit Note")
        print("6. Delete Note")
        print("7. Save Notes")
        print("8. Exit")

        choice = input("Choose an option: ")


        if choice == "1":
            add_note(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            filter_by_tag(notes)
        elif choice == "5":
            edit_note(notes)
        elif choice == "6":
            delete_note(notes)
        elif choice == "7":
            save_notes(notes)
        elif choice == "8":
            save_notes(notes)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


# Run the app
main()

