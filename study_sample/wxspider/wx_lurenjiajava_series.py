import re

from study_sample.myutils.report_html2pdf import convert


def getLen(filePath):
    count = 0
    fp = open(filePath, "r", encoding='utf-8')
    while 1:
        buffer = fp.read(8 * 1024 * 1024)
        if not buffer:
            break
        count += buffer.count('\n')
    print(count)
    print('over')
    fp.close()
    return count

def loadText(filePath):
    # len = getLen(filePath)
    import fileinput
    text = ''
    for line in fileinput.input(filePath):
        print(line)
        text += line
    return text

fn = './temp.md'
source_code = loadText(fn)
print(source_code)
urls = re.findall(r'<a.*?href=.*?<\/a>', source_code, re.I)
for url in urls:
    print(url)
    regex = '<a.*?href="(.*?)">(.*?)</a>'
    tuple = re.match(regex, url, re.DOTALL).groups()
    # print(tuple)
    print(tuple[0].split('" target="_blank')[0],tuple[1])
    html_path = tuple[0].split('" target="_blank')[0]
    pdf_path = './.out/'+tuple[1] + '.pdf'
    convert(html_path,pdf_path)