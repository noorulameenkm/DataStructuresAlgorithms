
"""
    Time Complexity - O(n)
    Space Complexity - O(1)
"""
def fare_in_words(fare):

    def ones(fare):
        switcher = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return switcher.get(fare)
    
    def teens(fare):
        switcher = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return switcher.get(fare)

    def tens(fare):
        switcher = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Fourty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }

        return switcher.get(fare)

    def two(fare):

        if not fare:
            return ''
        elif fare < 10:
            return ones(fare)
        elif fare < 20:
            return teens(fare)
        else:
            tenner = fare // 10
            rest = fare - tenner * 10
            return tens(tenner) + ' ' + ones(rest) if rest else tens(rest)

    def three(fare):
        hundred = fare // 100
        rest = fare - hundred * 100

        if hundred and rest:
            return ones(hundred) + ' Hundred ' + two(rest)
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return ones(hundred) + ' Hundred'


    if not fare:
        return 'Zero'
    

    billion = fare // 1000000000
    million = (fare - billion * 1000000000) // 1000000
    thousands = (fare - billion * 1000000000 - million * 1000000) // 1000
    rest = fare - billion * 1000000000 - million * 1000000 - thousands * 1000

    result = ''

    if billion:
        result = three(billion) + ' Billion'
    
    if million:
        result = result + ' ' if result else ''
        result += three(million) + ' Million'
    
    if thousands:
        result = result + ' ' if result else ''
        result += three(thousands) + ' Thousand'
    
    if rest:
        result = result + ' ' if result else ''
        result += three(rest)
    
    return result



fare = 5648
print("The fare is:", fare_in_words(fare), "dollars")
print("The fare is:", fare_in_words(15000), "dollars")