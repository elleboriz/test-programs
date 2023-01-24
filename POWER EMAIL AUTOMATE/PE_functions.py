import regex
"""
OPENING TEXT FILE AND READING CONTENT
:returns FILE CONTENT

"""
#input('Enter file PATH:')
def file_open():
    try:
        with open(r"C:\Users\gmb\Desktop\Good.txt",errors='replace') as opened_file:
            r_file = opened_file.read()
            opened_file.close()
            return r_file
    except:
        print(Exception ,"""OOPS.. AN ERROR OCCURRED 
                        TRY THESE TO TROUBLESHOOT:
                        * Verify Your File PATH if its correct
                        * Verify your File name
                        * Verify your File Type (.txt)
                        """)

read_file = file_open()

"""  STILL UNDER DEVELOPEMENT
test = regex.regex_filter(read_file)

"""




