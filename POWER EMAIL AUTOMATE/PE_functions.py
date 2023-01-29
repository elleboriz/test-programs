import re

"""
extracts emails from string text and filter out all emails in it,
return: List of extracted emails 
"""


class Email:
    def __init__(self, file_data: str):
        assert len(file_data) > 1, f"input file must contain data"
        self.email = file_data

    def find_emails(self):

        """
        extracts emails from string text using regex pattern and filter them out ,
        :return: List of extracted emails

        """
        try:
            pattern = re.compile(r'([a-zA-Z0-9-._]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')
            matches = pattern.finditer(self.email)
            result = [match.group(0) for match in matches]
            return "\n".join(result)
        except:
            return print(Exception, "Oops An Error occurred ")

    def match_domain(self):

        domains = input(
            """Enter a Domain Or a list of Domains e.g(@gmail.com , @yahoo.com etc) you want to filter out: """
        )
        assert len(domains) > 0, f"{domains} must contain 1 or more domain name for search match cases "
        domains = domains.split(',')

        """
        filters out  emails of chosen domain name or names and appending to results
        
        """
        results = []
        for domain in domains:
            domain = domain.strip()

            data = self.email.replace("\n", ',').split(',')

            result = set(filter(lambda email: domain in email, data))
            results.append(result)

        """
        collecting the results sets (non duplicate) converting to list and joining 
        
        return: match emails 
        """

        match_list = [list(i) for i in results]
        final_result = []
        for match in match_list:
            final_result += match
        return "\n".join(final_result)
