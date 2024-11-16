from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QTableWidget, QListWidget,
    QLineEdit, QFormLayout,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel, QSpinBox)
from memo_qss import *
from memo_app import app

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("відпочити")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_next = QPushButton("відповисти")
btn_next.setStyleSheet(QSS_OK)
lb_question = QLabel("Запитання")
lb_question.setStyleSheet(QSS_TextCardQuestion)

gb_question = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()

rb_ans1 = QRadioButton("1")
rb_ans2 = QRadioButton("2")
rb_ans3 = QRadioButton("3")
rb_ans4 = QRadioButton("4")

RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)


gb_ansewer = QGroupBox()
lb_result = QLabel("Правильно")
lb_result.setStyleSheet(QSS_TextResult)
lb_result = QLabel("Правильно")
lb_right_answer=QLabel("відповідь")
lb_result.setStyleSheet(QSS_TextCardResult)

layout_ans_1 = QHBoxLayout()
layout_ans_2 = QHBoxLayout()
layout_ans_3 = QHBoxLayout()
layout_ans_2.addWidget(rb_ans1)
layout_ans_2.addWidget(rb_ans1)
layout_ans_3.addWidget(rb_ans1)
layout_ans_3.addWidget(rb_ans1)

layout_ans_1.addLayout(layout_ans_2)
layout_ans_1.addLayout(layout_ans_3)

RadioGroupBox.setLayout(layout_ans_1)
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, aligment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_result, aligment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

h1_main = QHBoxLayout()
h2_main =QHBoxLayout()
h3_main= QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QHBoxLayout()



h1_main.addWidget(btn_menu)
h1_main.addStretch(1)
h1_main.addWidget(btn_rest)
h1_main.addWidget(sp_rest=QSpinBox)
h1_main.addWidget(lb_rest=("хвилин"))

h2_main.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
h3_main.addWidget (gb_ansewer)
h3_main.addWidget (gb_question)

h4_main.addStretch(1)
h4_main.addWidget(btn_next, stretch=2)
h4_main.addStretch(1)

v1_main.QVBoxLayout()
v1_main.addLayout(h1_main, stretch=1)
v1_main.addLayout((layout_line2, stretch=2)v1_main.addLayout(layout_line3, stretch=8))
v1_main.addStretch(1)
v1_main.addLayout(h4_main, stretch=1)
v1_main.addStretch(1)
v1_main.setSpacing(5)

def gb_answer():
    gb_question.hide()    
    gb_answer.show()
    btn_next.setText("Наступний")

def show_question():
    gb_question.show()
    gb_answer.hide()
    btn_next.setText('OK')
    RadioGroup.setExclusive(False)
    rb_ans1.setChecked(False)
    rb_ans2.setChecked(False)
    rb_ans3.setChecked(False)
    rb_ans4.setChecked(False)
    RadioGroup.setExclusive(True)
    
window = QWidget()
window.resize(500,500)
window.move(300,300)
window.setWindowTtitle('Тестування')
window.setLayout(v1_main)

window.show()
app.exec_()
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False) RadioGroup.setExclusive(True)