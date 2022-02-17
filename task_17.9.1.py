
def sort(array):

    for i in range(len(array)):#проходим по всему массиву
        idx_min = i # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(array)): #
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min: # если индекс не совпадает с минимальным, меняем
            array[i], array[idx_min] = array[idx_min], array[i]
    return array

def binary_search(array, element, left, right):
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует

    middle = (right+left) // 2 # находимо середину
    if array[middle] == element: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)


arr = input("Введите список  целых чисел через пробел: ")
num = int(input("Введите целое число: "))
arr_list = list(map(int, arr.split(sep=" ")))
sort_list = sort(arr_list)

print("Сортировка списка по возрастанию: ", sort_list)
num_index = binary_search(sort_list, num, 0, len(sort_list))
print("Индекс элемента, ввeдeнного пользователем: ", num_index)


