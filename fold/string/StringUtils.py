
'''
内容是否包含中文字符
'''

def content_is_chinese(content):
    for i in range(len(content)):
        isChinese = is_chinese(content[i])
        if isChinese:
            return True
    return False


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False
