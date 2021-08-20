def getNonRepeatList1(data):
    return list(set(data))


def getNonRepeatList2(data):
    new_data = []
    for i in range(len(data)):
        if data[i] not in new_data:
            new_data.append(data[i])
    return new_data

def getNonRepeatList3(data):
    return [i for n, i in enumerate(data) if i not in data[:n]]

def getNonRepeatList4(data):
    print(dict.fromkeys(data))
    return list(dict.fromkeys(data))

def getNonRepeatList5(data):
    import pandas as pd
    return pd.unique(data).tolist()

input_list = [1,1,2,4,6,7,4,2]
print(getNonRepeatList1(input_list))
print(getNonRepeatList2(input_list))
print(getNonRepeatList3(input_list))
print(getNonRepeatList4(input_list))
print(getNonRepeatList5(input_list))