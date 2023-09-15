def checkvalue(valuetockeck):
    assert (type(valuetockeck) is int), "You must enter a number"
    assert (valuetockeck > 0), "Value entered must be greater than 0"
    if valuetockeck > 4:
        print("Value is greater than 4")