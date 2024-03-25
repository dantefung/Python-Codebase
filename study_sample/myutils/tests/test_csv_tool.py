from study_sample.myutils.CSVTool import CSVTool

if __name__ == '__main__':
    # 使用示例：
    tool = CSVTool('test_data.csv')
    data = tool.read_csv()
    print(data)

    # 处理数据...
    csvtool = CSVTool('temp_test.csv')
    test_data = [
        ["1708866898-1", "url1", "1.web scraper 提问须知", "url2"],
        ["1708866898-2", "url3", "2.🧭 Web Scraper 学习导航", "url4"]
    ]
    csvtool.write_csv(test_data,["web-scraper-order", "web-scraper-start-url", "WebScraper教程目录", "WebScraper教程目录-href"])

    # 或者，如果你想追加数据：
    new_rows_to_append = [["3", "ben", "45"]]
    tool.append_to_csv(new_rows_to_append)

    print(data)