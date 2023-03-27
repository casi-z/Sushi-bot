def stringMap(first, array, last):

    str = ''
    for elem in array:
        str += (first + elem + last)

    return str
def text(array):
    return "\n".join(array)