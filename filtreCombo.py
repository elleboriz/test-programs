import math
import os


unsorted_folder_path = r'C:\Users\gmb\Desktop\POWER_EMAIL_AUTOMATE'
sorted_folder_path = r'C:\Users\gmb\Desktop\MyCombos'
print(f'Working...')
def file_open(current_file_name):
    """

    :param current_file_name: main
    :return: handling file opening for each file
    """
    try:
        with open(unsorted_folder_path + '\\' + current_file_name ,errors='replace') as opened_file:
            r_file = opened_file.read()
            opened_file.close()
            return r_file

    except:
        print(Exception ,"""OOPS.. AN ERROR OCCURRED 
                        TRY THESE TO TROUBLESHOOT:
                        * Verify Your File or Folder PATH if its correct
                        * Verify your File or Folder name
                        * Verify your File Type (.txt)
                        * IF NOTHING WORKED THEN YOU ARE FUCKED
                        """)


def create_file(path, data):

    file = open(path , 'a' ,errors='replace')
    for combo in data:
        file.write(f'{combo}\n')
    file.close()




def filter_cat(combos_list):
    """

    :param combos_list:
    :return: Iterates over combo list to filter out all disierd combos mail
    """

    fr = '.fr'
    de = '.de'
    laposte = '@laposte.net'
    orange = '@orange.fr'
    wanadoo = '@wanadoo.fr'

    def all_fr_sorting(email):
        email_spl = email.split(':')
        if email_spl[0].endswith(fr) :
            return email
        else:
            return ""

    def all_de_sorting(email):
        email_spl = email.split(':')
        if email_spl[0].endswith(de) :
            return email
        else:
            return ""

    all_fr_set = set(list(map(all_fr_sorting, combos_list)))
    all_de_set = set(list(map(all_de_sorting, combos_list)))
    laposte_list = set(filter(lambda email: laposte in email, combos_list))
    orange_list = set(filter(lambda email: orange in email, all_fr_set))
    wanadoo_list = set(filter(lambda email: wanadoo in email, all_fr_set))

    laposte_list = list(laposte_list)
    orange_mail_list = list(wanadoo_list) + list(orange_list)
    all_de_list = list(all_de_set)
    all_fr_list = list(all_fr_set) + laposte_list

    return  all_fr_list ,orange_mail_list , laposte_list , all_de_list


files = os.listdir(unsorted_folder_path)
for file in files:
    result = file_open(file)
    combos_list = result.replace('\n', ',').split(',')

    all_list = filter_cat(combos_list)
    all_fr ,orange_mail , laposte , all_de = all_list

    all_fr_path = sorted_folder_path+ '\\all_fr.txt'
    all_de_path = sorted_folder_path+ '\\all_de.txt'
    laposte_path = sorted_folder_path+ '\\laposte.txt'
    orange_mail_path = sorted_folder_path+ '\\orange_mail.txt'

    try:
        create_file(all_fr_path, all_fr)
        create_file(all_de_path, all_de)
        create_file(orange_mail_path, orange_mail)
        create_file(laposte_path, laposte)
    except:
        print(Exception)


for file in files:
    file_path = os.path.join(unsorted_folder_path , file)
    os.remove(file_path)


print('Done')
