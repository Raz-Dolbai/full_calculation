import requests
import pytest

endpoint = 'https://partner.agentapp.ru/v1/agreements/1b6bffb6-566b-4b7e-a86c-e714bc1855ee/results/{}'

username = 'qa@qa.qa'
password = '111'

def check_status_code(response, status_code=200):
    assert response.status_code == status_code, f'Ожидаемый ответ сервера - {status_code} не совпадает с фактическим {response.status_code}'

@pytest.mark.parametrize('ins_company_code',
                         ["ZETTA", "ALPHA_STRAH", "SDS", "RENAISSANCE", "RGS", "SNGI", "UGORIA", "INGOSSTRAH",
                          "TINKOFF"])
def test_full_calculation(ins_company_code):
    response = requests.post(endpoint.format(ins_company_code), auth=(username, password))
    check_status_code(response)
    if response.status_code == 200:
        ans = response.json()
        print(ans["parameters"]["integrated_company_title"])
        print(ans["parameters"]["integrated_company_code"])
        print(ans["parameters"]["premium"])

# Для запуска
# Нужно быть в директории с проектом
# pytest -s -v main.py::test_full_calculation
