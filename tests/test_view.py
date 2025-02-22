from src.view import filter_vacancies, get_vacancies_by_salary


def test_filter_vacancies_no_res():
    vacancies_list = [
        {
            "name": "Разработчик Python",
            "snippet": "Описание",
            "salary": {"from": 100000, "to": 150000},
        },
        {
            "name": "Разработчик JAVA",
            "snippet": "Тоже описание",
            "salary": {"from": 50000, "to": 70000},
        },
    ]
    filter_words = ["Basic"]
    result = filter_vacancies(vacancies_list, filter_words)
    assert result == []


def test_get_vacancies_by_salary(vacancies_list, vacancies_list_res):
    salary_range = "60000 - 200000"
    result = get_vacancies_by_salary(vacancies_list, salary_range)
    assert result == vacancies_list_res
