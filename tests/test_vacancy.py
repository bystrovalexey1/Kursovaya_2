from src.vacancy import Vacancy


def test_init_vacancy(test_vacancies):
    assert test_vacancies.name == "Разработчик Python"
    assert test_vacancies.url == "<https://hh.ru/vacancy/test>"
    assert test_vacancies.salary == {"from": 70000, "to": 120000}
    assert test_vacancies.snippet == "Требования: опыт работы от 3 лет..."

    Vacancy().clear_list()


def test_list_vacancies(test_vacancies, test_filtered_vacancies):
    assert test_vacancies.list_vacancies()[0] == test_filtered_vacancies

    Vacancy().clear_list()


def test_filtered_salary_vacancies(
    capsys, vacancy_1, vacancy_2, test_filtered_vacancies_salary
):
    assert len(Vacancy.list_vacancies()) == 2

    Vacancy.filtered_salary(0, 130000)
    message = capsys.readouterr()
    assert message.out.strip() == f"{test_filtered_vacancies_salary}"

    Vacancy().clear_list()


def test_ge_vacancies(capsys, vacancy_1, vacancy_2):
    print(Vacancy.__ge__(vacancy_2, vacancy_1))
    message = capsys.readouterr()
    assert message.out.strip() == "True"

    Vacancy().clear_list()


def test_cast_to_object_list(test_cast_to_object_vacancy, test_cast_to_add_vacancy):
    Vacancy().clear_list()
    Vacancy.cast_to_object_list(test_cast_to_object_vacancy)
    assert Vacancy.list_vacancies() == test_cast_to_add_vacancy
