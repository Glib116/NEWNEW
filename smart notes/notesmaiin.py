from PyQt5.Qtcore import Qt

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QListWidgets, QInputDialog, QHBoxLayout,
                             QFormLayout, QLineEdit, QTextEdit)

app = QApplication([])
app.setStyleSheet('
                  Qwidget {
                    background-color: gray;
                  }
                  QPushbutton {
                  background-color: black;
                  border: 1 px solid black;
                  color: white;
                  bordor-radius: 10px;
                  font-family: Montserrat;
                  font-size: 20px;
                  font-weight: bold
                  }
                  QInputDialog {
                  background-color: white;
                  border: 3 px solid black;
                  color: white;
                  font-family: Montserrat;
                  font-size: 16px;
                  bordor-radius: 10px;
                  }
                  QLabel {
                  border: 3 px solid black;
                  color: black;
                  font-family: Montserrat;
                  font-size: 20px;
                  }
                  QListWidget {
                  background-color: white;
                  border: 3 px solid black;
                  color: black;
                  font-family: Montserrat;
                  font-size: 16px;
                  bordor-radius: 10px;
                  font-weight: bold
                  }
                  QLineEdit {
                  background-color: white;
                  border: 1 px solid black;
                  color: black;
                  font-family: Montserrat;
                  font-size: 16px;
                  bordor-radius: 10px;
                  }
                  QTextEdit {
                  background-color: white;
                  border: 3 px solid black;
                  color: black;
                  font-family: Montserrat;
                  font-size: 22px;
                  bordor-radius: 10px;
                  font-weight: bold
                  }
                  ')
notes = []

notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(800,600)

list_notes = QListWidget()
list_notes_label = QLabel('Список заміток')
button_note_create = QPushButton("Створити замітку")
button_note_del = QPushButton("Видалити замітку")
button_note_save = QPushButton("Зберегти замітку")

field_tag = QLineEdit()
field_tag.setPlaceholderText('Введіть тег...')

field_text = QTextEdit()

button_tag_add = QPushButton('Додати тег')
button_tag_del = QPushButton('Видалити тег')
button_tag_search = QPushButton('Пошук тег')


list_tags = QListWidget()
list_tags_label = QLabel('Списоок тегів')

layout_notes = QHBoxLayout()

col1 = QVBoxLayout()
col1.addWidget(field_text)

col1 = QVBoxLayout()
col1.addWidget(field_text)

col2 = QVBoxLayout()
col2.addWidget(list_notes_label)
col2 = addWidget(list_notes)

row1 = QHBoxLayout()
row1.addWidget(button_note_create)
row1.addWidget(button_note_del)

row2 = QHBoxLayout()
row2.addWidget(button_note_save)

col2.addLayout(row1)
col2.addLayout(row2)

col2.addWidget(list_tags_label)
col2.addWidget(list_tags)
col2.addWidget(field_tag)

row3 = QHBoxLayout()
row3.addWidget(button_tag_add)
row3.addWidget(button_tag_del)

row4 = QHBoxLayout()
row4.addWidget(button_tag_search)

col2.addLayout(row3)
col2.addLayout(row4)

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

notes_win.setLayout(layout_notes)



