def findStringsByRecursion(integer_string, index, currentCombination, result):
    

    if index == len(integer_string):
        result.append(''.join(list(currentCombination)))
        return None

    if index == len(integer_string) - 1:
        new_combination = list(currentCombination)
        if int(integer_string[index]) >= 1 and int(integer_string[index]) <= 26:
            converted_char = chr(65 + int(integer_string[index]) - 1)
            new_combination.append(converted_char)

        result.append(''.join(new_combination))
        return None


    int_1 = int(integer_string[index])
    int_2 = int(integer_string[index: index + 2])
    
    
    if int_1 >= 1 and int_1 <= 26:
        converted_char_1 = chr(65 + int_1 - 1)
        new_combination = list(currentCombination)
        new_combination.append(converted_char_1)
        findStringsByRecursion(integer_string, index + 1, new_combination, result)

    new_combination = list(currentCombination)
    if int_2 >= 1 and int_2 <= 26:
        converted_char_2 = chr(65 + int_2 - 1)
        new_combination.append(converted_char_2)
    
    findStringsByRecursion(integer_string, index + 2, new_combination, result)







def findAllStrings(integer_string):
    result = []
    if integer_string is None or len(integer_string) == 0:
        return result
    
    currentCombination = []
    findStringsByRecursion(integer_string, 0, currentCombination, result)
    return result



# print(chr(65 + 1))
def main():
    integer_string = "122"
    result = findAllStrings(integer_string)
    print(result)
    integer_string = "10"
    result = findAllStrings(integer_string)
    print(result)
    integer_string = "256"
    result = findAllStrings(integer_string)
    print(result)
    integer_string = "25678"
    result = findAllStrings(integer_string)
    print(result)

main()