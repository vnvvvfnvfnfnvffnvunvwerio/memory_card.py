from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox , QButtonGroup, QGroupBox
from random import shuffle
from random import randint
#создай приложение для запоминания информации

class Question():
    def __init__(self, question, right_answer, wron1, wron2 , wron3):
        self.question = question
        self.right_answer = right_answer
        self.wron1 = wron1
        self.wron2 = wron2
        self.wron3 = wron3




app = QApplication([])
main_win = QWidget()
main_win.resize(500,500)

text = QLabel('Какой национальности несуществует')
button = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')

an = QRadioButton('Чулымцы')
an1 = QRadioButton('Энцы')
an2 = QRadioButton('Смурфы')
an3 = QRadioButton('Алеуты')

v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()

v1.addWidget(an)
v1.addWidget(an1)
v2.addWidget(an2)
v2.addWidget(an3)

h1.addLayout(v1)
h1.addLayout(v2)

RadioGroupBox.setLayout(h1)

RadioGroup = QButtonGroup()
RadioGroup.addButton(an)
RadioGroup.addButton(an1)
RadioGroup.addButton(an2)
RadioGroup.addButton(an3)

AnsGroup = QGroupBox('Результат теста')
correct = QLabel('Правильно/Неправильно')
r_answer = QLabel('Правильный ответ')

rt = QVBoxLayout()
rt.addWidget(correct)
rt.addWidget(r_answer)

AnsGroup.setLayout(rt)
AnsGroup.hide()
rf = QVBoxLayout()

rf.addWidget(text)
rf.addWidget(RadioGroupBox)
rf.addWidget(AnsGroup)
rf.addWidget(button)
main_win.setLayout(rf)

main_win.cur_question = -1

def show_result():
    RadioGroupBox.hide()
    AnsGroup.show()
    button.setText("Следующий вопрос")


def show_question():
    RadioGroupBox.show()
    AnsGroup.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    an.setChecked(False)
    an1.setChecked(False)
    an2.setChecked(False)
    an3.setChecked(False)
    RadioGroup.setExclusive(True)


def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


answers = [an, an1 , an2 , an3]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wron1)
    answers[2].setText(q.wron2)
    answers[3].setText(q.wron3)
    text.setText(q.question)
    r_answer.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')
    print('Статистика')
    print("-Всего вопросов: ",main_win.total)
    print('-Правильных ответов: ', main_win.score)
    print('Рейтинг:',main_win.score/main_win.total * 100,'%' )
def next_question():
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
    main_win.total += 1
    print('Статистика')
    print('-Всего вопросов: ', main_win.total)
    print('-Правильных ответов: ', main_win.score)



def show_correct(res):
    correct.setText(res)
    show_result()
question_list = []
q = Question('Государственный язык Бразилии', 'Португальский', 'Русский', 'Английский', "Энцы")
question_list.append(q)
question_list.append(Question('Сколько было пилотируемых высадок на Луну?', 'Шесть', 'Семь', 'Восемь', 'Пять'))

question_list.append(Question('Как долго длилась Столетняя война?', '116 лет', '100 лет', '50 лет', '101 год'))

question_list.append(Question('Что означает термин ДНК?', 'Дезоксирибонуклеиновая кислота', 'Дуорибонуклеиновая кислота', 'Дуоксирибонуклеиновая кислота', 'Дезоксирибонуклеарная кислота'))

question_list.append(Question('“K” - это химический символ какого элемента?', 'Калий', 'Водород', 'Хром', 'Титан'))
main_win.score = 0
main_win.total = 0
next_question()




button.clicked.connect(click_OK)
main_win.show()
app.exec_() 