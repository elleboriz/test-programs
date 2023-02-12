import re

"""
extrats emails from a string of sentences

:return List of extrated emails 
"""

def text_emails(text):
    try:

        pattern = re.compile(r'([a-zA-Z0-9-._]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')
        matches = pattern.finditer(text)

        return [match.group(0) for match in matches]
    except:
        return print(Exception,"AN ERROR OCCURRED")

    
    """
    BY @elleboriz
    """
