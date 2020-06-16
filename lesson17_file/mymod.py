def count_lines(name):
    with open(name) as f:
        return len(f.readlines())


def count_chars(name):
    with open(name) as f:
        return len(f.read())


def test(name):
    with open(name) as f:
        lines = len(f.readlines())
        f.seek(0)
        chars = len(f.read())
    return f"Lines: {lines} \nChars: {chars}"
