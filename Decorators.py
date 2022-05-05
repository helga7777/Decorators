# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
import time
import datetime


def make_trace(old_function):
    def new_function(*args, **kwargs):
        today = datetime.datetime.today()
        result = old_function(*args, **kwargs)
        result_book = f'вызвана функция {old_function.__name__} {today.strftime("%Y-%m-%d-%H.%M.%S")} с аргументами {args} и {kwargs} .Получили {result} \n'
        with open("decoratorsbook.txt", "a+") as f:
            f.write(result_book)
        return result
    return new_function

def summator(a,b):
    time.sleep(1)
    return a + b

summator = make_trace(summator)
summator(4,6)
summator(44,66)
summator(404,606)






# Написать декоратор из п.1, но с параметром – путь к логам.
import time
import datetime

def multiply(multiplier):
    url = multiplier
    def make_trace(old_function):
        def new_function(*args, **kwargs):
            today = datetime.datetime.today()
            result = old_function(*args, **kwargs)
            result_book = f'вызвана функция {old_function.__name__} {today.strftime("%Y-%m-%d-%H.%M.%S")} с аргументами {args} и {kwargs} .Получили {result} \n'
            url_next = f'{url}/decoratorsbook.txt'
            with open(url_next, "a+") as f:
                f.write(result_book)
            return result
        return new_function
    return make_trace

url = 'D:\саша\работа\нетология\профессиональная работа с питон'
@multiply(url)
def summator(a,b):
    time.sleep(1)
    return a + b

summator(4,6)
summator(44,66)
summator(404,606)




# Применить написанный логгер к приложению из любого предыдущего д/з.


# Написать генератор, который принимает список списков, и возвращает их плоское представление.

nested_list = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]]

@multiply(url)
def flat_generator(nested_list):
    cursor_start = 0
    cursor_start_2 = 0
    while cursor_start < len(nested_list):
        while cursor_start_2 < len(nested_list[cursor_start]):
            v = nested_list[cursor_start][cursor_start_2]
            cursor_start_2 += 1
            yield v
        cursor_start += 1
        cursor_start_2 = 0

for item in  flat_generator(nested_list):
    print(item)
