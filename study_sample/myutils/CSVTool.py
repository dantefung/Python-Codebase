import csv
import os


class CSVTool:
    def __init__(self, filepath):
        """ 初始化CSVTool类，设置文件路径 """
        self.filepath = filepath

    def read_csv(self, delimiter=','):
        """ 读取CSV文件并返回内容为二维列表 """
        rows = []
        try:
            with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=delimiter)
                # 跳过表头（如果有的话）
                headers = next(reader, None)
                for row in reader:
                    rows.append(row)
            return rows
        except FileNotFoundError:
            print(f"文件 {self.filepath} 不存在")
            return []
        except Exception as e:
            print(f"读取CSV文件时发生错误: {str(e)}")
            return []

    def write_csv(self, data, headers=None, delimiter=',', mode='w'):
        """ 将二维列表写入CSV文件，可选地添加表头 """
        try:
            with open(self.filepath, mode, newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=delimiter)
                if headers is not None:
                    writer.writerow(headers)
                writer.writerows(data)
        except Exception as e:
            print(f"写入CSV文件时发生错误: {str(e)}")

    def append_to_csv(self, data, headers=None, delimiter=','):
        """ 向CSV文件追加数据，可选地添加表头（仅当文件为空时） """
        if not self.is_file_empty():
            headers = None  # 如果文件不为空，则不写入表头
        self.write_csv(data, headers=headers, delimiter=delimiter, mode='a')

    def is_file_empty(self):
        """ 检查文件是否为空 """
        return os.path.getsize(self.filepath) == 0

    def get_column_data(self, colIdx):
        """ 从CSV文件中获取指定列的数据 """
        rows = self.read_csv()
        if not rows:
            return []

        column_data = [row[colIdx] for row in rows[1:]]  # 跳过表头
        return column_data



