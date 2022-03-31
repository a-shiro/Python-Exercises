with open('text.txt', 'r') as file, open('text2.txt', 'w') as output:

    punctuation_marks = {'.', ',', ':', ';', '?', '!', "'", '"', '_', '-'}
    output_data = {}

    for i, l in enumerate(file):
        output_data[i + 1] = [0, 0]
        line = l.strip('\n').split(' ')

        for word in line:
            for char in word:
                if char.isalpha():
                    output_data[i + 1][0] += 1
                elif not char.isdigit():
                    output_data[i + 1][1] += 1

        output.write(f'Line {i + 1}: {" ".join(line)} ({output_data[i + 1][0]})({output_data[i + 1][1]})\n')


