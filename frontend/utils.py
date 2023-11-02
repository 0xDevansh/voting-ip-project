from re import sub

# Source: https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-97.php
def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()

def to_ordinal(index):
    suffix = 'th'
    if index % 10 == 1:
        suffix = 'st'
    if index % 10 == 2:
        suffix = 'nd'
    if index % 10 == 3:
        suffix = 'rd'
    if index in [11, 12, 13]:
        suffix = 'th'
    return str(index) + suffix