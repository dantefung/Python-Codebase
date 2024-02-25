import json


json1 = '[{"codeName":"yyy","id":301,"typeCode":"301"}]'
json2 = '[{"id":"8","type_code":"8","code_name":"xxx","is_hot":"1","short_code_name":"","is_del":"0","is_system":"0"}]'

data1 = json.loads(json1)
data2 = json.loads(json2)

# 按照ID升序排列
data1_sorted = sorted(data1, key=lambda x: x['id'])
data2_sorted = sorted(data2, key=lambda x: int(x['id']))

data2_map = {int(item['id']): item['code_name'] for item in data2_sorted}


for item1 in data1_sorted:
    id_value = item1['id']
    codeName_value = item1['codeName']

    if id_value in data2_map:
        code_name_value_from_map = data2_map[id_value]

        if codeName_value == code_name_value_from_map:
            print(f"For id {id_value}, codeName and code_name match.")
        else:
            print(f"For id {id_value}, codeName and code_name do not match.")
    else:
        print(f"Id {id_value} not found in data2_map.")