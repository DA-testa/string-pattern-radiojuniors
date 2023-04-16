# python3

def read_input():
    input_type = input()

    if input_type == "i":
        pattern = input()
        text = input()
    elif input_type == "f":
        file_name = input()
        with open(file_name) as f:
            pattern = f.readline()
            text = f.readline()

    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    if len(pattern) > len(text):
        return []

    patternhash = hash(pattern)
    temphash = hash(text[:len(pattern)])
    occurrences = []

    for i in range(len(text) - len(pattern) + 1):
        if temphash == patternhash and text[i:i+len(pattern)] == pattern:
            occurrences.append(i)

        if i < len(text) - len(pattern):
            temphash = hash(text[i+1:i+len(pattern)+1])

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
