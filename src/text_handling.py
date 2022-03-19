def read_file(filename, encoding="utf8", remove_non_ascii=True):
    with open(filename, 'r', encoding=encoding) as file:
        content = file.read()
    if remove_non_ascii:
        from unidecode import unidecode
        content = unidecode(content)
    return content


def write_file(filename, content):
    f = open(filename, "a")
    f.write(content)
    f.close()
