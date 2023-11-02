import os

# compiles all the code into a txt file
ignore = [
    './.git',
    './compiled.txt',
    './database.sqlite',
    './Makefile',
    './.idea',
    './test.py',
    './compile_code.py',
    './identifier.sqlite',
    './README.md',
]

def add_files_to_txt(file, path):
    files_dirs = os.listdir(path)

    #main.py should be on top
    if 'main.py' in files_dirs:
        index = files_dirs.index('main.py')
        main_file = files_dirs.pop(index)
        files_dirs.insert(0, main_file)

    for p in files_dirs:
        fullpath = f'{path}/{p}'

        # check ignored
        ignore_file = False
        for ign_path in ignore:
            if fullpath.startswith(ign_path):
                ignore_file = True
                break
        if ignore_file or '__init__.py' in fullpath or '__pycache__' in fullpath:
            continue

        if os.path.isfile(fullpath):
            print(fullpath)
            # add to compiled.txt
            with open(fullpath) as codefile:
                file.write(f'# ---- {fullpath} ----\n')
                for line in codefile:
                    if line == '' or line.isspace():
                        continue
                    file.write(line)
                file.write('\n\n')
        if os.path.isdir(fullpath):
            add_files_to_txt(file, fullpath)


with open('compiled.txt', 'w') as file:
    add_files_to_txt(file, '.')
