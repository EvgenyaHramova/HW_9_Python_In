# Создать декоратор для использования кэша. 
# Т.е. сохранять аргументы и результаты в словарь, 
# если вызывается функция с агрументами, 
# которые уже записаны в кэше - вернуть результат из кэша, 
# если нет - выполнить функцию. Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.


import json
from random import randint
from typing import Callable


def cash_json(func: Callable):
    try:
        with open(f'{func.__name__}.json', 'r') as data:
            dict_res = json.load(data)

    except FileNotFoundError:
        dict_res = {}


    def wrapper(*args):
        if dict_res.get('+'.join(map(str,args))):
            print(f"Return result with cash: {(dict_res.get('+'.join(map(str,args))))}")
            return dict_res.get('+'.join(map(str,args)))
        else:                                 
            dict_res['+'.join(map(str,args))] = func(*args)
            with open(f'{func.__name__}.json', 'w') as data:
                json.dump(dict_res, data, indent= 4)
            return func(*args)
    return wrapper

@cash_json
def sum_args(*args):
    sum_nums = 0
    for i in range(len(nums)):
        sum_nums = sum_nums + nums[i]
    print(sum_nums)    

    return sum_nums


if __name__ == "__main__":
    nums = [randint(0, 3) for _ in range(3)]
    print(nums)
    sum_args(nums)