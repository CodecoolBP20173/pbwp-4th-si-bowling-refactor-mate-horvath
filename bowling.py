STRIKE = 'X'
SPARE = '/'
MISS = '-'


def score(throws):
    """This function calculates the score of the bowling game from the given results(throws)
    and return the calculated score(result)"""

    throws = throws.upper()
    result = 0
    frame = 1
    max_frame = 10
    in_first_half = True

    for i in range(len(throws)):
        result += get_throwresult(i, SPARE, i, throws)
        if frame < max_frame:
            if throws[i] == SPARE:
                result += get_value(throws[i+1])
            if throws[i] == STRIKE:
                result += get_value(throws[i+1])
                result += get_throwresult(i+2, SPARE, i, throws)
                frame += 1
                continue
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
    return result


def get_value(char):
    """This function assignes and then returns the corresponding value of the given bowling sign(char)"""

    bowling_values = {STRIKE: 10, SPARE: 10, MISS: 0}
    bowling_values.update({str(i): i for i in range(1, 10)})

    if char in bowling_values:
        return bowling_values[char]
    else:
        raise ValueError()


def get_throwresult(NumberOfthrow, ValueToCheck, NumberOfCurrentthrow, ResultList):
    """This function calculates the result of the given roll, considering some all the resctrictions
    that come with bowling point calculation
    NumberOfthrow = the throw needed to check, ValueToCheck = the type of throw we need
    NumberOfCurrentthrow = the current number of throw, ResultList = the object that holds the throws"""

    if ResultList[NumberOfthrow] == ValueToCheck:
            return get_value(ResultList[NumberOfCurrentthrow]) - get_value(ResultList[NumberOfthrow-1])
    else:
        return get_value(ResultList[NumberOfthrow])
