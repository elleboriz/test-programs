from  string import punctuation
from random import randint,choice

def pass_gen(value=None):

    try:

        if not value:
            value = "Pass"
        """   
        :param value: 
        :return: a string of  random combination of ascii characters , numbers  and symbols 
        base on user preferred word
        """

        symbol = str(punctuation)
        symbol = [i for i in symbol]
        symbol = choice(symbol)


        value = value.capitalize()
        ran_value_index = randint(len(value)//2,len(value))
        value = [i for i in value]
        value[-1] = value[-1].upper()
        value.insert(ran_value_index,str(randint(10,101)))
        value = "".join(value)

        number = str(randint(0,100))

        return number + symbol + value

    except:
        return """An Error occurred:
< check input type should be string (str) >
         """






