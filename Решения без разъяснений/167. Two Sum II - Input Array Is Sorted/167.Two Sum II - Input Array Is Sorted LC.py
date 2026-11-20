def my_solution1(numbers: list[int], target: int):
    unums = set(numbers)
    for n1 in unums:
        if target - n1 in numbers:
            ind = numbers.index(n1)
            ind2 = numbers.index(target-n1)
            if ind == ind2:
                ind2 += 1
            result = [ind+1, ind2+1]
            result.sort()
            return result