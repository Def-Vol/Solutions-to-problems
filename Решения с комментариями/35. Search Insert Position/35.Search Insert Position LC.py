'''
LeetCode почему-то принимает даже решение my_solution1() и при этом условие задачи не 
устанавливает никаких ограничений. Но я знаю, что когда говорят о поиске значения в 
отсортированном массиве и тем более указывают на временную сложность О(log n), то имеют
ввиду написание алгоритма "Бинарного поиска" (Binary Search), что и представлен во втором решении.
'''
def my_solution1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    try:
        return nums.index(target)
    except:
        nums.append(target)
        nums.sort()
        return nums.index(target)


'''
Согласно условию задачи, если целевое значение отсутствует в списке, то вернуть позицию, в
которой оно могло бы находиться. Поэтому возращаем значение left, потому что эта переменная
содержит индекс элемента, идущего сразу после последнего меньшего по отношению к target числа.
'''
def my_solution2(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return left