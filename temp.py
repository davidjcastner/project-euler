import os

if __name__ == '__main__':
    for (dirpath, dirnames, filenames) in os.walk('.\\project_euler'):
        for fn in filenames:
            if fn.startswith('test_'):
                filepath = os.path.join(dirpath, fn)
                new_name = f's_{fn[5:8]}_test.py'
                new_filepath = os.path.join(dirpath, new_name)
                print(fn, filepath, new_name)
                os.rename(filepath, new_filepath)
