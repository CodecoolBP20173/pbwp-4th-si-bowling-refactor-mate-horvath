def score(throws):
    throws = throws.upper()
    result = 0
    frame = 1
    strike = 'X'
    spare = '/'
    max_frame = 10
    in_first_half = True
    for i in range(len(throws)):
        result += get_throwresult(i, spare, i, throws)
        if frame < max_frame:
            if throws[i] == spare:
                result += get_value(throws[i+1])
            if throws[i] == strike:
                result += get_value(throws[i+1])
                result += get_throwresult(i+2, spare, i, throws)
                frame += 1
                continue
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
    return result


def get_value(char):
    bowling_values = {'X': 10, '/': 10, '-': 0}
    bowling_values.update({str(i): i for i in range(1, 10)})
    if char in bowling_values:
        return bowling_values[char]
    else:
        raise ValueError()


def get_throwresult(NumberOfthrows, ValueToCheck, NumberOfCurrentthrows, ResultList):
    if ResultList[NumberOfthrows] == ValueToCheck:
            return get_value(ResultList[NumberOfCurrentthrows]) - get_value(ResultList[NumberOfthrows-1])
    else:
        return get_value(ResultList[NumberOfthrows])
