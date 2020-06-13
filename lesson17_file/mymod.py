def count_lines(name):
    with open(name) as f:
        return len(f.readlines())

def count_chars(name):
    with open(name) as f:
        return len(f.read())

def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    return f"Lines: {lines} \nChars: {chars}"