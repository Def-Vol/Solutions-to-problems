'''
Требуется решение с временной сложностью О(log n), а значит задача решается тем же бинарным 
поиском. Однако теперь в сортированном массиве могут содержаться дублированные target, поэтому 
необходимо найти индексы их начального и конечного значений в списке. Поэтому стоит прописать 
два бинарных поиска: первый ищет начальный индекс, а второй - последний индекс. 

Бинарный поиск необходимо дополнить ещё условием, который даст сигнал, что значение является 
начальным или конечным. Соответственно, чтобы определить необходимое условие стоит ответить
на вопрос: что означает начальное или конечное значение? Они означают, что сразу перед 
начальным стоит иное число, так же как и после конечного. Поэтому достаточно взять наш mid
(в моём решении ind), когда он равен target и проверить является ли mid-1 или mid+1 уже иным 
числом. И если да, то left = mid или right = mid соответственно и прервать цикл, так как
значение найдено.
'''
def my_solution1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:    #Если массив (список) пустой, то и икать ничего не надо
        return [-1,-1]
    left, right = 0, len(nums) - 1
    if nums[0] == target and nums[right] == target:    #Если весь список это target, то и начало, и конец всего этого списка и есть искомое
        return [0, right]
    while left <= right:
        ind = (left + right)//2
        if nums[ind] == target:
            if ind == 0 or nums[ind-1] < target:
                left = ind
                break 
            right = ind - 1
        elif nums[ind] < target:
            left = ind + 1
        else:
            right = ind - 1 
    result = [left]
    if left > len(nums)-1 or nums[left] != target:    #Если left не найден, то и target в списке отсутствует
        return[-1,-1]
    left, right = 0, len(nums) - 1
    while left <= right:
        ind = (left + right)//2
        if nums[ind] == target:
            if ind == len(nums)-1 or nums[ind+1] > target:
                right = ind 
                break
            left = ind + 1
        elif nums[ind] < target:
            left = ind + 1
        else:
            right = ind - 1
    result.append(right)
    return result