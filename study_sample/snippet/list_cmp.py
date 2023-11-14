

# 预期
list1 = [202,380,299,210,219,662,1522,683,2354,1302,2355,242,2378,409,2204,1867]
# 实际
#list2 = [202,242,299,380,409,662,683,1302,1522,1867,2204,2354,2378]
list2 = [202,242,299,380,409,662,683,1302,1522,1867,2204,2354,2378]



diff_elements = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]

print("列表1中不在列表2: ", [x for x in list1 if x not in list2]);
print("列表2中不在列表1: ", [x for x in list2 if x not in list1]);
print("差异元素:  ", diff_elements);



