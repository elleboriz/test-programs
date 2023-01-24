import re

def REgex_filter(value):
    try:

        pattern = re.compile(r'([a-zA-Z0-9-._]+)@([a-zA-Z-]+)\.([a-zA-Z]+)\B:(\S+)')
        matches = pattern.finditer(value)

        return [match.group(0) for match in matches]
    except:
        return print(Exception,"AN ERROR OCCURRED")
