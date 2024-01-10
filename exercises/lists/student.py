def double_items(ns):
     for i in range(len(ns)):
        ns[i] *= 2
    

def pad_right(xs, length, padding):
    while len(xs) < length:
        xs.append(padding)

def remove_all(xs, item_to_remove):
    for i in range(len(xs) - 1, -1, -1):
        if xs[i] == item_to_remove:
            del xs[i]    

