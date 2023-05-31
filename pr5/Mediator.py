class Course(object):
    """Посредник"""

    def displayCourse(self, user, course_name):
        print("Курс ведёт {}, название курса: {}".format(user, course_name))


class User(object):
    '''Класс, экземпляры которого хотят взаимодействовать друг с другом'''

    def __init__(self, name):
        self.name = name
        self.course = Course()

    def sendCourse(self, course_name):
        self.course.displayCourse(self, course_name)

    def __str__(self):
        return self.name


"""Основной метод"""

if __name__ == "__main__":
    rusakov = User('Русаков Алексей Михайлович')
    filatov = User('Филатов Вячеслав Валерьевич')
    serov = User('Серов Владимир Алесандрович')

    rusakov.sendCourse("Создание мессенджера")
    filatov.sendCourse("Асимптотический анализ алгоритмов")
    serov.sendCourse("Методы решения аналитических задач")
