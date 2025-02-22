from src.api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.view import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies
from src.vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    platforms = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = platforms.load_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_add_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Получение списка вакансий из класса Vacancy
    vacancies_list = Vacancy.list_vacancies()

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    #  Функция фильтрации вакансий по ключевым словам
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    #  Функция сортировки вакансий по зарплате
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    #  Функция сортировки вакансий (вывод топ № вакансий)
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

    #  Функция вывода вакансий в консоль
    print_vacancies(top_vacancies)

    # Пример работы контструктора класса с одной вакансией
    vacancy = Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "100 000-150 000 руб.",
        "Требования: опыт работы от 3 лет...",
    )

    # Vacancy.validate_salary()
    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)

    #  циклом создаем каждый словарь обьектом класса Vacancy
    for filtered_vacancy in [tuple(d.values()) for d in top_vacancies]:
        vacancy_obj = Vacancy(*filtered_vacancy)
        json_saver.add_vacancy(vacancy_obj)


if __name__ == "__main__":
    user_interaction()