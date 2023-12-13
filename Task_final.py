import json
import os
from datetime import datetime

class NotesApp:
    def __init__(self, data_file='notes.json'):
        self.data_file = data_file 
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    notes = json.load(file)
                except json.JSONDecodeError:
                    notes = []
        else:
            notes = []
        return notes

    def save_notes(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.notes, file, indent=2)

    def show_notes(self):
        for note in self.notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Date: {note['date']}")

    def show_note(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                print(f"ID: {note['id']}, Title: {note['title']}, Body: {note['body']}, Date: {note['date']}")
                return
        print("Note not found.")

    def add_note(self, title, body):
        note = {
            'id': len(self.notes) + 1,
            'title': title,
            'body': body,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.notes.append(note)
        self.save_notes()
        print("Note added successfully!")

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = title
                note['body'] = body
                note['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                print("Note edited successfully!")
                return
        print("Note not found.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note['id'] != note_id]
        self.save_notes()
        print("Note deleted successfully!")

    def run(self):
        while True:
            print("\n1. Show Notes\n2. Add Note\n3. Edit Note\n4. Delete Note\n5. Show note by ID \n6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.show_notes()
            elif choice == '2':
                title = input("Enter note title: ")
                body = input("Enter note body: ")
                self.add_note(title, body)
            elif choice == '3':
                note_id = int(input("Enter note ID to edit: "))
                title = input("Enter new title: ")
                body = input("Enter new body: ")
                self.edit_note(note_id, title, body)
            elif choice == '4':
                note_id = int(input("Enter note ID to delete: "))
                self.delete_note(note_id)
            elif choice == '5':
                note_id = int(input("Enter note ID: "))
                self.show_note(note_id)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = NotesApp()
    app.run()
