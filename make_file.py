import bs4
import os
import re
import requests
import sys
import textwrap

NEW_LINE = '\n'


def touch_directory(directory: str) -> None:
    """makes all directories in a given path if they don't exist"""
    if os.path.exists(directory):
        return
    os.makedirs(directory)


def get_file_name(problem_number: int) -> str:
    """returns the file name for a given problem"""
    return f's_{problem_number:04d}.py'


def get_problem_dir_name(problem_number: int) -> str:
    """returns the directory name for a given problem

    problems are group into directories of 50 with a format of 0001_0050, 0051_0100, etc.
    """
    problem_group = problem_number // 50
    lower_bound = problem_group * 50 + 1
    upper_bound = lower_bound + 49
    return f'{lower_bound:04d}_{upper_bound:04d}'


def get_full_file_dir(problem_number: int) -> str:
    """gets the full file directory for a given problem number"""
    return os.path.join('src', 'solutions', get_problem_dir_name(problem_number))


def get_full_file_path(problem_number: int) -> str:
    """gets the full file path for a given problem number"""
    return os.path.join(get_full_file_dir(problem_number), get_file_name(problem_number))


def does_solution_file_exist(problem_number: int) -> bool:
    """checks if a solution file exists for a given problem number"""
    file_path = get_full_file_path(problem_number)
    return os.path.exists(file_path)


def next_problem_number() -> int:
    """finds the next problem number to make"""
    problem_number = 1
    while does_solution_file_exist(problem_number):
        problem_number += 1
    return problem_number


def comment(*args: list[str]) -> str:
    comments = [c.split(NEW_LINE) for c in args]
    comments = [[f'# {line}{NEW_LINE}' if len(line) > 0 else NEW_LINE
                 for line in lines] for lines in comments]
    return str().join([str().join(lines) for lines in comments])


def problem_url(n: int) -> str:
    return f'https://projecteuler.net/problem={n}'


def problem_code(title: str, description: str) -> str:
    return f'''
def solve() -> str:
    """Problem {str(problem_number)} - {title}"""
    return str()


if __name__ == \'__main__\':
    print(solve())
'''


def make_file(problem_number: int) -> None:
    """scrapes the problem page and makes a new solution file"""
    page = requests.get(problem_url(problem_number))
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    content = soup.find(id='content')
    title = content.find('h2').text
    description = content.find('div', class_='problem_content').text
    # Remove LaTeX characters
    title = re.sub(r'\$', '', title)
    description = re.sub(r'\$', '', description)
    description = re.sub(r'\\dots', '...', description)
    description = description.strip()
    # Split description into lines of 118 or fewer characters
    description = '\n'.join(textwrap.wrap(description, width=78))
    touch_directory(get_full_file_dir(problem_number))
    with open(get_full_file_path(problem_number), 'w') as f:
        # write all decodeable characters
        for c in comment(
            title,
            f'Problem {str(problem_number)}',
            problem_url(problem_number), '',
                description), '':
            try:
                f.write(c)
            except Exception as e:
                print(e)
        f.write(problem_code(title, description))


if __name__ == '__main__':
    # makes the next sequential problem if not sys arg given
    problem_number = None
    try:
        problem_number = int(sys.argv[1])
    except:
        problem_number = next_problem_number()
    make_file(problem_number)
