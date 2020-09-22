import os
import pathspec
import sys
from typing import List


def find_all_files(current_path: str, ignore_spec: pathspec.PathSpec, match_spec: pathspec.PathSpec) -> List[str]:
    '''recursively searches for all files, returns a list with complete paths for the current os'''
    if ignore_spec.match_file(current_path):
        return []
    elif os.path.isfile(current_path) and match_spec.match_file(current_path):
        return [os.path.realpath(current_path)]
    elif os.path.isdir(current_path):
        all_files = []
        for obj in os.listdir(current_path):
            all_files += find_all_files(os.path.join(current_path, obj), ignore_spec, match_spec)
        return all_files
    else:
        return []


def compile_mypy_command(root_directory: str, ignore_globs: List[str]) -> str:
    '''creates a cli friendly string for mypy'''
    assert os.path.isdir(root_directory)
    assert type(ignore_globs) == list
    for glob in ignore_globs:
        assert type(glob) == str
    ignore_patterns = map(pathspec.patterns.GitWildMatchPattern, ignore_globs)
    match_patterns = map(pathspec.patterns.GitWildMatchPattern, ['**/*.py'])
    return 'mypy ' + ' '.join(find_all_files(root_directory, pathspec.PathSpec(ignore_patterns), pathspec.PathSpec(match_patterns)))


if __name__ == '__main__':
    ignore_globs = ['.git', '.github']
    for path in sys.argv[1:]:
        if os.path.isfile(path):
            with open(path, 'r') as ignore_file:
                ignore_globs += ignore_file.readlines()
    print(compile_mypy_command(os.getcwd(), ignore_globs))
