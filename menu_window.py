from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, /
    QHBoxLayout, QPushButton, QLabel


menu_win = QWidget()
lb_quest = QLabel("Введіть запитання:")
lb_right_ans = QLabel("Введіть вірну відповідь")
lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь відповідь")
lb_wrong_ans2 = QLabel("Введіть першу хибну відповідь відповідь")
lb_wrong_ans3 = QLabel("Введіть першу хибну відповідь відповідь")

lb_question = QLineEdit()
lb_right_ans = QLineEdit()
lb_wrong_ans1 = QLineEdit()
lb_wrong_ans2 = QLineEdit()
lb_wrong_ans3 = QLineEdit()

lb_header_stat = QLabel("Статистика")
lb_header_stat.setStyleSheet("font-size: 19 px; font-weight: bold;")

lb_statistics = QLabel()

vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)


h1_question = QHBoxLayout()
h1_question.addLayout(v1_labels)
h1_question.addLayout(v1_lineEdits)

btn_back = QPushButton("назва")
btn_add_question = QPushButton("Додати запитання")
btn_clean = QPushButton("Очистити")
h1_buttons = QHBoxLayout()
h1_buttons.addWidget(btn_add_question)
h1_buttons.addWidget(btn_clear)

v1_res = QVBoxLayout()
v1_res.addLayout(h1_question)
v1_res.addLayout(h1_buttons)
v1_res.addLayout(lb_header_stat)
v1_res.addLayout(lb_header_stat)
v1_res.addLayout(btn_back)

menu_win.setLayout(v1_res)
menu_win.resize(400, 300)




