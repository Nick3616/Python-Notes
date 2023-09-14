import json
import datetime

class Notes:
    def __init__(self, file_name="notes.json"):
        self.file_name = file_name
        try:
            with open(self.file_name, 'r') as file:
                self.notes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.notes = []

    def add(self, title, msg):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "message": msg,
            "date": datetime.datetime.now().isoformat()
        }
        self.notes.append(note)
        self.save()
        return "Заметка успешно сохранена"

    def edit(self, note_id, title, msg):
        for note in self.notes:
            if note["id"] == note_id:
                note["title"] = title
                note["message"] = msg
                note["date"] = datetime.datetime.now().isoformat()
                self.save()
                return "Заметка успешно отредактирована"
        return "Заметка не найдена"

    def delete(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                self.notes.remove(note)
                self.save()
                return "Заметка успешно удалена"
        return "Заметка не найдена"

    def list_notes(self, date=None):
        if date:
            return [note for note in self.notes if note["date"].startswith(date)]
        return self.notes

    def save(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.notes, file)

def interactive_mode():
    notes_app = Notes()

    while True:
        command = input("Введите команду (add, edit, delete, list, exit): ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            msg = input("Введите тело заметки: ")
            print(notes_app.add(title, msg))

        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            msg = input("Введите новое тело заметки: ")
            print(notes_app.edit(note_id, title, msg))

        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            print(notes_app.delete(note_id))

        elif command == "list":
            date = input("Введите дату для фильтрации (YYYY-MM-DD) или оставьте пустым: ")
            for note in notes_app.list_notes(date if date else None):
                print(f"ID: {note['id']} | Заголовок: {note['title']} | Тело: {note['message']} | Дата: {note['date']}")

        elif command == "exit":
            break

        else:
            print("Неизвестная команда. Пожалуйста, введите одну из следующих команд: add, edit, delete, list, exit.")

if __name__ == "__main__":
    interactive_mode()
