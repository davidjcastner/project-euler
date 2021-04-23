'''pulls the problem information from project euler website'''

from bs4 import BeautifulSoup
import os
import requests
import sys

NEW_LINE = '\n'

##############################################
# directory methods
##############################################


def solution_dir(n: int) -> str:
    directory = os.path.dirname(__file__)
    directory = os.path.join(directory, 'solutions')
    dir_start_num = n - (n % 25)
    dir_end_num = dir_start_num + 24
    subdirectory = f'{str(dir_start_num).zfill(3)}_{str(dir_end_num).zfill(3)}'
    return os.path.join(directory, subdirectory)


def solution_filepath(n: int) -> str:
    filename = f's_{str(n).zfill(3)}.py'
    return os.path.join(solution_dir(n), filename)


def solution_test_filepath(n: int) -> str:
    filename = f's_{str(n).zfill(3)}_test.py'
    return os.path.join(solution_dir(n), filename)


def solution_files_exist(n: int) -> bool:
    return os.path.exists(solution_filepath(n)) or os.path.exists(solution_test_filepath(n))


def touch_directory(p: str) -> None:
    if os.path.exists(p):
        return
    os.makedirs(p)

##############################################
# making the problem
##############################################


def comment(*args: list[str]) -> str:
    comments = [c.split(NEW_LINE) for c in args]
    comments = [[f'# {line}{NEW_LINE}' if len(line) > 0 else NEW_LINE for line in lines] for lines in comments]
    return str().join([str().join(lines) for lines in comments])


def problem_url(n: int) -> str:
    return f'https://projecteuler.net/problem={n}'


def write_solution_file(n: int) -> None:
    page = requests.get(problem_url(n))
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find(id='content')
    title = content.find('h2').text
    description = content.find('div', class_='problem_content').text
    with open(solution_filepath(n), 'w') as f:
        f.write(comment(title, f'Problem {str(n)}', description))
        f.write(f'''
def solve() -> str:
    \'\'\'Problem {str(n)} - {title}\'\'\'
    return str()


if __name__ == \'__main__\':
    print(solve())
''')


def write_solution_test_file(n: int) -> None:
    with open(solution_test_filepath(n), 'w') as f:
        f.write(f'''from s_{str(n).zfill(3)} import solve


def test_simplified_version() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '0'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '0'
''')


def make_problem(n: int) -> None:
    # check for overwriting
    if solution_files_exist(n):
        print('solution files exist already')
        return
    # ensure directory exists
    touch_directory(solution_dir(n))
    write_solution_file(n)
    write_solution_test_file(n)


if __name__ == '__main__':
    problem_number = None
    try:
        problem_number = int(sys.argv[1])
        assert problem_number > 0 and problem_number < 1000
    except Exception:
        print('please provide a number between 1 and 999')
    if problem_number is not None:
        make_problem(problem_number)
