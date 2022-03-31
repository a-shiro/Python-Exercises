with open('text.txt', 'r+') as file:

    output = []
    symbols = {'-', ',', '.', '!', '?'}
    line_count = -1

    for line in file:
        line_count += 1
        for symbol in symbols:
            if symbol in line:
                line = line.replace(symbol, '@')
        if line_count % 2 == 0:
            output.append(line)

with open('text.txt', 'w') as file:
    for sentence in output:
        sentence = sentence.strip('\n')
        result = ' '.join(sentence.split(' ')[::-1])
        file.write(f"{result}\n")


# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.