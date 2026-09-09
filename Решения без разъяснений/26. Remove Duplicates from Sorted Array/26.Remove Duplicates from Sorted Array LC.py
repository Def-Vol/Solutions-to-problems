#"remove the duplicates in-place", то есть суть задачи: удалять повторяющиеся значения необходимо именно в переданном списке, не создавая новый,
#поэтому решить задачу через множество в одно действие (nums = list(set(nums)).sort()) - невозможно, ибо это удаление старого и создание нового списка.

#Решение с использованием метода .remove() выдаёт непростительно большое время исполнения (см. 26.Runtime№1.png). 
#Однако количество используемой памяти наименьшее среди решений сообщества.
def my_solution1(nums): 
    """
    :type nums: List[int]
    :rtype: int
    """
    ind = 0
    while ind < len(nums):
        rcount = nums.count(nums[ind])
        if rcount > 1:
            for n1 in range(rcount-1):
                nums.remove(nums[ind])
        ind += 1


#Решение с использованием ключевого слова del позволяет ускорить выполнение в 4 раза (см. 26.Runtime№2.png),
#почти не увеличивая при этом объём памяти.
def my_solution2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ind = 0 
    while ind < len(nums):
        del nums[ind+1:ind+nums.count(nums[ind])]
        ind += 1
