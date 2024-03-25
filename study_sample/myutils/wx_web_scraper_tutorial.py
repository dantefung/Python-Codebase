from study_sample.myutils.CSVTool import CSVTool
from study_sample.myutils.firefox_html2pdf import convertByJs

if __name__ == '__main__':
    # 数据来自 web scraper 爬取
    csv_tool = CSVTool('wx_web_scraper_tutorial.csv')
    # column_name = "WebScraper教程目录-href"
    colIdx = 3
    hrefs = csv_tool.get_column_data(colIdx)
    names = csv_tool.get_column_data(2)

    i = 0
    for href in hrefs:
        print(names[i] + '---' + href)
        pdf_path = 'D:/.out/'+names[i].replace(" ", "").replace("|", "") + '.pdf'
        convertByJs(href, pdf_path)
        i = i + 1






