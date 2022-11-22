from application.db import people
from application.salary import calculate_salary


if __name__ == '__main__':
    print(f'{people.get_employees()} earned {calculate_salary()} dollars.')
