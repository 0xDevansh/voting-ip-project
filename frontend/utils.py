from re import sub

# Source: https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-97.php
def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()