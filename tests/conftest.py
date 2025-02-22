import pytest

from src.vacancy import Vacancy


@pytest.fixture
def test_vacancies():
    return Vacancy(
        "Разработчик Python",
        "<https://hh.ru/vacancy/test>",
        {"from": 70000, "to": 120000},
        "Требования: опыт работы от 3 лет...",
    )


@pytest.fixture
def test_filtered_vacancies():
    return {
        "name": "Разработчик Python",
        "url": "<https://hh.ru/vacancy/test>",
        "salary": {"from": 70000, "to": 120000},
        "snippet": "Требования: опыт работы от 3 лет...",
    }


@pytest.fixture
def vacancy_1():
    return Vacancy(
        "Разработчик Python",
        "<https://hh.ru/vacancy/test>",
        {"from": 70000, "to": 130000},
        "Требования: опыт работы от 3 лет...",
    )


@pytest.fixture
def vacancy_2():
    return Vacancy(
        "Разработчик Python",
        "<https://hh.ru/vacancy/test>",
        {"from": 70000, "to": 200000},
        "Требования: опыт работы от 3 лет...",
    )


@pytest.fixture
def test_filtered_vacancies_salary():
    return {
        "name": "Разработчик Python",
        "url": "<https://hh.ru/vacancy/test>",
        "salary": {"from": 70000, "to": 130000},
        "snippet": "Требования: опыт работы от 3 лет...",
    }


@pytest.fixture
def test_cast_to_object_vacancy():
    return [
        {
            "name": "Python",
            "url": "<https://hh.ru/vacancy/test>",
            "salary": {"from": 35000, "to": 70000},
            "snippet": {"requirement": "Требования: опыт работы от 1 лет..."},
        },
        {
            "name": "Разработчик",
            "url": "<https://hh.ru/vacancy/test1>",
            "salary": {"from": 50000, "to": 80000},
            "snippet": {"requirement": "Требования: опыт работы от 2 лет..."},
        },
        {
            "name": "Python Разработчик",
            "url": "<https://hh.ru/vacancy/test2>",
            "salary": {"from": 90000, "to": 150000},
            "snippet": {"requirement": "Требования: опыт работы от 3 лет..."},
        },
    ]


@pytest.fixture
def test_cast_to_add_vacancy():
    return [
        {
            "name": "Python",
            "url": "<https://hh.ru/vacancy/test>",
            "salary": {"from": 35000, "to": 70000},
            "snippet": "Требования: опыт работы от 1 лет...",
        },
        {
            "name": "Разработчик",
            "url": "<https://hh.ru/vacancy/test1>",
            "salary": {"from": 50000, "to": 80000},
            "snippet": "Требования: опыт работы от 2 лет...",
        },
        {
            "name": "Python Разработчик",
            "url": "<https://hh.ru/vacancy/test2>",
            "salary": {"from": 90000, "to": 150000},
            "snippet": "Требования: опыт работы от 3 лет...",
        },
    ]


@pytest.fixture
def vacancies_list():
    return [
        {
            "name": "Разработчик Python",
            "snippet": "Требования: опыт работы от 2 лет...",
            "salary": {"from": 140000, "to": 200000},
        },
        {
            "name": "Тестировщик ПО",
            "snippet": "Без опыта...",
            "salary": {"from": 50000, "to": 70000},
        },
        {
            "name": "Разработчик JAVA",
            "snippet": "Требования: опыт работы от 4 лет...",
            "salary": {"from": 95000, "to": 170000},
        },
    ]


@pytest.fixture
def vacancies_list_res():
    return [
        {
            "name": "Разработчик Python",
            "snippet": "Требования: опыт работы от 2 лет...",
            "salary": {"from": 140000, "to": 200000},
        },
        {
            "name": "Разработчик JAVA",
            "snippet": "Требования: опыт работы от 4 лет...",
            "salary": {"from": 95000, "to": 170000},
        },
    ]
