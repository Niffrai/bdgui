import sqlite3
from sqlite3 import Error
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PySide6.QtCore import Qt
import ctypes

pathdb = sqlite3.connect("zadan.db")

# def execute_query(path, query):
#     cursor = path.cursor()
#     try:
#         cursor.executescript(query)
#         path.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# # create_tabl = """
# # CREATE TABLE `users` (
# # 	`id` INTEGER PRIMARY KEY,
# # 	`name` TEXT NOT NULL,
# # 	`age` INTEGER NOT NULL,
# # 	`gender` TEXT NOT NULL,
# # 	`nationality` TEXT NOT NULL
# # );

# # CREATE TABLE `likes` (
# # 	`id` INTEGER PRIMARY KEY,
# # 	`user_id` INTEGER NOT NULL,
# # 	`post_id` INTEGER NOT NULL,
# # 	FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
# # 	FOREIGN KEY (`post_id`) REFERENCES `posts`(`id`)
# # );

# # CREATE TABLE `posts` (
# # 	`id` INTEGER PRIMARY KEY,
# # 	`title` TEXT NOT NULL,
# # 	`description` TEXT NOT NULL,
# # 	`user_id` INTEGER NOT NULL,
# # 	FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
# # );

# # CREATE TABLE `comments` (
# # 	`id` INTEGER PRIMARY KEY,
# # 	`text` TEXT NOT NULL,
# # 	`user_id` INTEGER NOT NULL,
# # 	`post_id` INTEGER NOT NULL,
# # 	FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
# # 	FOREIGN KEY (`post_id`) REFERENCES `posts`(`id`)
# # );
# # """

# execute_query(pathdb, create_tabl)

class PostEntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Entry")
        self.layout = QVBoxLayout()

        self.table_label = QLabel("Table Name:")
        self.table_input = QLineEdit()
        self.layout.addWidget(self.table_label)
        self.layout.addWidget(self.table_input)

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)

        self.gender_label = QLabel("Gender:")
        self.gender_input = QLineEdit()
        self.layout.addWidget(self.gender_label)
        self.layout.addWidget(self.gender_input)

        self.nationality_label = QLabel("Nationality:")
        self.nationality_input = QLineEdit()
        self.layout.addWidget(self.nationality_label)
        self.layout.addWidget(self.nationality_input)

        self.add_button = QPushButton("Find")
        self.add_button.clicked.connect(self.add_data)
        self.layout.addWidget(self.add_button)

        self.add_button = QPushButton("AddSoft")
        self.add_button.clicked.connect(self.switch_to_data_entry)  # Connect to switch to the second window
        self.layout.addWidget(self.add_button)

        self.add_button = QPushButton("DeleteS")
        self.add_button.clicked.connect(self.switch_to_delete_entry)  # Connect to switch to the second window
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)
    
    def switch_to_data_entry(self):
        window2.show()

    def switch_to_delete_entry(self):
        window3.show()

    def add_data(self):
        table_name = self.table_input.text()
        name = self.name_input.text()
        age = self.age_input.text()
        gender = self.gender_input.text()
        nationality = self.nationality_input.text()

        cursor = pathdb.cursor()
        cursor.execute(f"INSERT INTO {table_name} (name, age, gender, nationality) VALUES (?, ?, ?, ?)",
                       (name, age, gender, nationality))
        pathdb.commit()
        
        ctypes.windll.user32.MessageBoxW(0, "Пользователь существует", ":)", 1)

class DataEntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Entry")
        self.layout = QVBoxLayout()

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)

        self.gender_label = QLabel("Gender:")
        self.gender_input = QLineEdit()
        self.layout.addWidget(self.gender_label)
        self.layout.addWidget(self.gender_input)

        self.nationality_label = QLabel("Nationality:")
        self.nationality_input = QLineEdit()
        self.layout.addWidget(self.nationality_label)
        self.layout.addWidget(self.nationality_input)

        self.add_button = QPushButton("Add Data")
        self.add_button.clicked.connect(self.add_data)
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)
	
	
    def add_data(self):
        name = self.name_input.text()
        age = self.age_input.text()
        gender = self.gender_input.text()
        nationality = self.nationality_input.text()

        cursor = pathdb.cursor()
        cursor.execute("INSERT INTO users (name, age, gender, nationality) VALUES (?, ?, ?, ?)",
                       (name, age, gender, nationality))
        pathdb.commit()
        print("Data added successfully")

class DeleteEntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DeleteEntryWidget")
        self.layout = QVBoxLayout()

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)

        self.gender_label = QLabel("Gender:")
        self.gender_input = QLineEdit()
        self.layout.addWidget(self.gender_label)
        self.layout.addWidget(self.gender_input)

        self.nationality_label = QLabel("Nationality:")
        self.nationality_input = QLineEdit()
        self.layout.addWidget(self.nationality_label)
        self.layout.addWidget(self.nationality_input)

        self.add_button = QPushButton("Delete Data")  
        self.add_button.clicked.connect(self.delete_data) 
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)

    def delete_data(self):
        name = self.name_input.text()
        age = self.age_input.text()
        gender = self.gender_input.text()
        nationality = self.nationality_input.text()

        cursor = pathdb.cursor()
        cursor.execute("DELETE FROM users WHERE name = ? AND age = ? AND gender = ? AND nationality = ?",
                       (name, age, gender, nationality))
        pathdb.commit()
        print("Data deleted successfully")

	
if __name__ == "__main__":
    app = QApplication([])
    window1 = PostEntryWidget()
    window2 = DataEntryWidget()
    window3 = DeleteEntryWidget()  

    def switch_to_data_entry():
        window1.close()
        window2.show()

    
    def switch_to_delete_entry():
        window1.close()
        window3.show()

    window1.show()
    sys.exit(app.exec())
