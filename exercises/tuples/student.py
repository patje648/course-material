def split_name(full_name):
    spatie= full_name.find(" ")
    lettervn= full_name[0:spatie]
    letteran=full_name[spatie+1:]
    return lettervn, letteran

