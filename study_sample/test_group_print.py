my_list = [54189, 54075, 9154, 36207, 19443, 64635, 73327, 48835, 60567, 77260, 60015, 60016, 60017,
						77261, 60568, 60569, 60570, 60571, 64297, 47595, 42756, 35925]  # 假设你已有一个包含14000个元素的列表

group_size = 2  # 每组的大小

with open("output.txt", "w") as f:  # 打开一个文件用于写入结果，如果文件不存在将会被创建
    for i in range(0, len(my_list), group_size):
        group = my_list[i:i+group_size]
        group_str = ', '.join(map(str, group))  # 将分组中的元素连接成一个字符串，使用逗号分隔
        group_str = 'delete from test_tbl where id in(' + group_str + ');'
        f.write(group_str + '\n\n')  # 将每个分组写入文件，每个分组占一行

print("结果已写入文件output.txt")
