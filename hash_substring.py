# python3

def read_input():
    cmd = input()
    pattern = ""
    text = ""

    if cmd.startswith('I'):
        pattern = input().rstrip()
        text = input().rstrip()
    elif cmd.startswith('F'):
        with open("tests/06") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    # print(pattern.rstrip(),text.rstrip())
    # if pattern == None or text == None:
    #     return []
    
    return (pattern, text)


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(patterninput, textinput):
    length = len(patterninput)
    if length > len(textinput):
        return []

    patternhash = hash(patterninput)
    temphash = hash(textinput[:length])
    occurrences = []

    for i in range(len(textinput) - length + 1):
        if temphash == patternhash and textinput[i:i+length] == patterninput:
            occurrences.append(i)

        if i < len(textinput) - length:
            temphash = hash(textinput[i+1:i+length+1])

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
