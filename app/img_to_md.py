import os
import re
import time
import hashlib
from PIL import ImageGrab


menu_text = \
    '''
a：将剪贴板中的图片转换成markdown引用
q：退出程序
'''


def md5(string):
    return hashlib.md5(string.encode()).hexdigest()


def get_now_time():
    nowtime = time.time()
    nowtime_string = str(nowtime)
    return nowtime_string


def get_img_name():
    nowtime_string = get_now_time()
    img_name = md5(nowtime_string) + '.png'
    return img_name


def get_md_path():
    md_path = input('请输入markdown文件所在目录：')
    return md_path


def mkdir(md_path):
    img_path = md_path + '\\markdown_img\\'
    if False == os.path.exists(img_path):
        os.mkdir(img_path)
    return img_path


def img_to_md(img_path):
    # 根据当前时间生成图片名称
    img_name = get_img_name()
    # 从剪贴板获取图片
    img = ImageGrab.grabclipboard()
    # 将图片保存到指定路径
    img.save(img_path + img_name)
    # 返回图片的markdown引用
    img_markdown1 = '![img]({name})'.format(name=img_name)
    img_markdown2 = '![img]({path}/{name})'.format(
        path=img_path.split('\\')[-2], name=img_name)
    return [img_markdown1, img_markdown2]


def main():
    md_path = get_md_path()
    #img_path = mkdir(md_path)
    img_path = md_path + '\\'
    while True:
        print(menu_text)
        arg = input('请输入要执行的操作参数：')
        if 'q' == arg:
            exit()
        elif 'a' == arg:
            pass
        else:
            continue
        try:
            md = img_to_md(img_path)
        except:
            md = [False, 'Error：剪贴板中没有截图']
        os.system('cls')
        if False == md[0]:
            print(md[1])
        else:
            print(md[0])
            print(md[1])


if __name__ == "__main__":
    main()
