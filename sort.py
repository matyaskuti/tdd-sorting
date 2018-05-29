def sort(list_):
    index = 0
    while len(list_) > index+1:
        if list_[index+1] < list_[index]:
            list_[index], list_[index+1] = list_[index+1], list_[index]
        index += 1
    return list_
