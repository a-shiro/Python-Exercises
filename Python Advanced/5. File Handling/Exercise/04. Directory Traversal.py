import os


def do_directory_search(path, result):
    for d in os.listdir(path):
        file_path = os.path.join(path, d)

        if os.path.isfile(file_path):
            extension = d.split('.')[-1]
            if extension not in result:
                result[extension] = []
        elif os.path.isdir(file_path):
            do_directory_search(file_path, result)


result = {}
do_directory_search(os.getcwd(), result)

with open('output.txt', 'w') as result_file:
    for ext, files in sorted(result.items()):
        result_file.write(f'.{ext}')
        result_file.write('\n')
        for file in sorted(files):
            result_file.write(f'--- {file}')
            result_file.write('\n')