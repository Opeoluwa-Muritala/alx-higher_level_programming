def remove_char_at(str, n):
    if n < len(str):
        str = str.replace(str[n],'')
    else:
        str = str
    return str
