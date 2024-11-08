def apply_all_func(int_list, *functions): #В функции создаем пустой словарь results
    results = {}
    for i in functions: #Перебераем все функции из *functions.
        result = i(int_list)
        results[i.__name__] = result #
    return results #Везвращаем словарь results.


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))