def score(roll):
    roll = [item.upper() for item in roll]
    result = 0
    frame = 1
    strike = 'X'
    spare = '/'
    max_frame = 10
    in_first_half = True
    for i in range(len(roll)):
        result += get_rollresult(i, spare, i, roll)
        if frame < max_frame:
            if roll[i] == spare:
                result += get_value(roll[i+1])
            if roll[i] == strike:
                result += get_value(roll[i+1])
                result += get_rollresult(i+2, spare, i, roll)
        if in_first_half:
            in_first_half = False
        else:
            frame += 1
            in_first_half = True
        if roll[i] == strike:
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    bowling_values = {'X': 10, '/': 10, '-': 0}
    bowling_values.update({str(i): i for i in range(1, 10)})
    if char in bowling_values:
        return bowling_values[char]
    else:
        raise ValueError()


def get_rollresult(NumberOfRoll, ValueToCheck, NumberOfCurrentRoll, ResultList):
    if ResultList[NumberOfRoll] == ValueToCheck:
            return get_value(ResultList[NumberOfCurrentRoll]) - get_value(ResultList[NumberOfRoll-1])
    else:
        return get_value(ResultList[NumberOfRoll])
