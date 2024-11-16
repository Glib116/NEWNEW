from random import choice, shuffle
from time import sleep
from PyQt5.QTWidgets import QApplication

app = QApplication([])


from menu_window import *
from memo_card_layout import *


class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right +=1
    def got_wrong(self):
        self.count_ask +=1


radio_buttons = [rb_ans1,rb_ans2,rb_ans3,rb_ans4]
q1 = Question("Хто створив Пайтон?", "Гвідо Ван Россум", "Егор Ліс","Стів Джобс", "Черін Тімур")
q2 = Question("У якому році Титанік затонув в Атлантичному океані 15 квітня, в дівочому плаванні з Саутгемптона??", "2021", "3212","1929", "1912")
q3 = Question("Який метал був відкритий Гансом Крістіаном Ерстедом у 1825 році?", "залізо","золото", "алюміній","алмаз")
q4 = Question("Яка столиця Португалії?", "Дискорд", "Лісабон","Київ", "Рим")
q5 = Question("Скільки вдихів щодня робить людський організм?", "100000", "20000","50000", "0")
q6 = Question("Що таке хімічний символ для срібла?", "Ad", "Mg","S", "Al")
q7 = Question("Яка найменша у світі птах?", "Бджола колібрі", "Даніїл","Голуб", "Чайка")
q8 = Question("Яка тривалість життя бабки?", "24 год", "2 роки","100 год", "милиард років")
q9 = Question("Хто грав «Боді» та «Дойла» в «Професіоналах»?", "Льюїс Коллінз та Мартін Шоу", "я","Джон Сіна", "Черін Тімур")
q10 = Question("Хто винайшов консервну банку для консервування їжі в 1810 році?", "Пітер Дуранд", "Егор Ліс","я", "Кирюха")
questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
def new_questions():
    global cur_q
    cur_q = choice(questions)
    lb_questions.setText(cur_q.questions)
    lb_right_answer.setText(cur_q.answer)

new_questions()


def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                cur_q.got_right()
                lb_result.setText("Вірно")
                answer.setchecked(False)
                break
    else:
        lb_result.setText('Не вірно!')
        cur_q.got_wrong()

    RadioGroup.setText(True)


def click_ok():
    if btn_next.text()== 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()

        btn_next.setText("Наступне питання")
    else:
        new_question.hide()
        gb_answer.show()
        gb_answer.hide()

        btn_next.setText("Відповіти")


btn_next.clicked.connect(click_ok)


def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()


btn_rest.clicked.connect(rest)

def menu_generation():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right/cur_q.count_ask)*100

    text = f'Разів відповили:{cur_q.count_ask}/n' / 
           f'вірних відповідей:{cur_q.count_ask}/n' / 
           f'Успішність: {round(c, 2)}%'
    lb_statistic.setText(text)
    menu_win.show()
    window.hide()

btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)

def clear():
    le_question.clear()


             
