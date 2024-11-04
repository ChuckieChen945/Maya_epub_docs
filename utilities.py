# import requests

# # link = 'https://help.autodesk.com/cloudhelp/2025/CHS/Maya-CharEffEnvBuild/files/GUID-66822A1A-C6AD-47B4-8782-E058B5E6A528.htm'

# link = 'https://help.autodesk.com/cloudhelp/2024/CHS/Maya-WhatsNew/files/GUID-A7291217-7424-49C9-8CB3-3089E7F4909E.htm'

# html = requests.get(link).text

# print(html)

import os
from pyquery import PyQuery as pq

def delete_unlisted_files(folder_path, keep_filenames):
    """
    遍历指定文件夹中的文件，如文件名不在 keep_filenames 列表中，则删除该文件。
    
    :param folder_path: 要遍历的文件夹路径
    :param keep_filenames: 需要保留的文件名列表（含扩展名）
    """
    for filename in os.listdir(folder_path):
        # # 获取文件的基础名称（不含扩展名）
        # file_base, file_ext = os.path.splitext(filename)

        # print(file_base,file_ext,filename)
        
        # 如果文件名不在指定列表中，则删除文件
        if filename not in keep_filenames:
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"已删除文件: {file_path}")


def get_image_names_from_html(folder_path):
    """
    读取指定文件夹中的所有 HTML 文件，并获取其中所有 img 标签的 src 属性。
    
    :param folder_path: 包含 HTML 文件的文件夹路径
    :return: 包含所有图像路径的列表
    """
    image_names = []
    
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件扩展名是否为 .html
        if filename.endswith(".html") and not filename.endswith('_id.html'):
            file_path = os.path.join(folder_path, filename)
            
            # 读取 HTML 文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # 使用 PyQuery 解析 HTML 并提取所有 img 标签的 src 属性
            doc = pq(html_content)
            img_elements = doc("img")
            for img in img_elements.items():
                img_src = img.attr("src")
                if img_src:  # 如果 src 属性存在，则添加到列表
                    image_names.append(os.path.basename(img_src))

    return image_names



def match_image_names():
    """
    匹配图片名与html中的引用，输出缺失的文件名
    """
    html_image_names = get_image_names_from_html('./html')
    images = os.listdir('./images')
    for html_image_name in html_image_names:
        if html_image_name not in images:
            print(html_image_name)

# keep_filenames = get_image_names_from_html('./html')  # 需要保留的文件名（含扩展名）
# delete_unlisted_files('./images', keep_filenames)
match_image_names()