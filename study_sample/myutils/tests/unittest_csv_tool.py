import csv
import os
from unittest.mock import mock_open, patch

from study_sample.myutils.CSVTool import CSVTool

# 测试数据
test_data = [
    ["web-scraper-order", "web-scraper-start-url", "WebScraper教程目录", "WebScraper教程目录-href"],
    ["1708866898-1", "url1", "1.web scraper 提问须知", "url2"],
    ["1708866898-2", "url3", "2.🧭 Web Scraper 学习导航", "url4"]
]

# 用于模拟文件操作的mock对象
mock_file_content = '\n'.join([','.join(row) for row in test_data])

def test_read_csv():
    # 使用patch装饰器模拟打开文件的操作
    with patch('builtins.open', mock_open(read_data=mock_file_content)) as mock_file:
        csv_tool = CSVTool('temp_test.csv')
        result = csv_tool.read_csv()

        assert result == test_data[1:]

def test_write_csv():
    # 创建临时文件路径，用于测试写入CSV
    temp_file_path = 'temp_test.csv'

    # 创建CSVTool实例并写入数据
    csv_tool = CSVTool(temp_file_path)
    csv_tool.write_csv(test_data)

    # 检查文件是否存在以及内容是否正确
    assert os.path.exists(temp_file_path)
    with open(temp_file_path, 'r', newline='', encoding='utf-8') as f:
        written_data = list(csv.reader(f))
        assert written_data == test_data

    # 清理临时文件
    os.remove(temp_file_path)

def test_append_to_csv():
    # 创建临时文件路径，用于测试追加写入CSV
    temp_file_path = 'temp_test.csv'
    # 先创建一个空文件
    open(temp_file_path, 'a').close()

    # 创建CSVTool实例并追加写入数据
    csv_tool = CSVTool(temp_file_path)
    csv_tool.write_csv(test_data)
    csv_tool.append_to_csv(test_data[1:])  # 不包含表头

    # 检查文件是否存在以及内容是否正确
    assert os.path.exists(temp_file_path)
    with open(temp_file_path, 'r', newline='', encoding='utf-8') as f:
        written_data = list(csv.reader(f))
        assert written_data == test_data[0:] + test_data[1:]

    # 清理临时文件
    os.remove(temp_file_path)

if __name__ == "__main__":
    print(test_data[1:])
    test_write_csv()
    test_read_csv()
    test_append_to_csv()
    print("All tests passed.")