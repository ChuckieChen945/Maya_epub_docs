# -*- coding: utf-8 -*-
'''
爬取Maya 2025手册，生成pdf
'''

import datetime
import json
import ssl
import time
import warnings

import pdfkit
import requests
import os, re
from urllib.parse import urljoin
from pyquery import PyQuery as pq



ssl._create_default_https_context = ssl._create_unverified_context
warnings.filterwarnings("ignore")



def write_log(log_file, content, with_time=True, mode='a+', print_line=True):
    # 输出日志
    if print_line:
        print(content)
    file_path = get_file_path(log_file)
    if not os.path.exists(os.path.join(os.getcwd(), file_path)):
        os.makedirs(file_path)
    with open(log_file, mode, encoding='utf-8') as f:
        if with_time:
            f.write(f'输出时间：{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {content}')
        else:
            f.write(content)

        f.close()


def get_file_path(full_path):
    # 根据文件路径，获取所在目录
    """
    根据文件名称获取目录
    :param full_path:
    :return:
    """
    return full_path[0:full_path.rfind(os.path.sep) + 1]



def clean_filename(filename):
    # 定义无效字符的正则表达式
    invalid_chars = r'[\\/:*?"<>|]'
    # 使用正则表达式替换无效字符为空字符
    cleaned_filename = re.sub(invalid_chars, '', filename)
    return cleaned_filename



def download_file(file_path, download_url, headers={}, check_exists=True):
    # 下载文件
    print('*' * 100)
    if os.path.exists(file_path) and check_exists:
        print(file_path, '文件已存在')
        return False
    print(f"保存路径：{file_path}")
    rindex1 = file_path.rfind(os.path.sep)
    rindex2 = file_path.rfind('/')
    rindex = rindex1 if rindex1 > rindex2 else rindex2
    file_folder = file_path[0:rindex + 1]
    # print(file_folder)
    if not os.path.exists(file_folder) and file_folder != '':
        os.makedirs(file_folder)
    # print(f'下载URL：{download_url}')
    try:
        response = requests.get(url=download_url, headers=headers, stream=True, timeout=600, verify=False)
        response.encoding = 'utf-8'
    except Exception as e:
        print(str(e))
        return False
    else:
        try:
            if not response.status_code == 200:
                print(download_url, f'响应码为{response.status_code}')
                return None
            # print(response.headers)
            if not "content-length" in response.headers.keys():
                # print(download_url, '下载失败')
                # return None
                content_size = len(response.content)
            else:
                content_size = int(response.headers["content-length"])
            size = 0
            with open(file_path, "ab+") as file:
                for data in response.iter_content(chunk_size=1024):
                    file.write(data)
                    file.flush()
                    size += len(data)
                    print("\r文件下载进度:%d%%(%0.2fMB/%0.2fMB)" % (
                        float(size / content_size * 100), (size / 1024 / 1024),
                        (content_size / 1024 / 1024)),
                          end=" ")
            print()
            return True
        except:
            return False



class DzSpider(object):
    def __init__(self):
        self.folder = fr'{os.getcwd()}'
        self.spider_num = 1
        self.req_url = 'https://help.autodesk.com/view/MAYAUL/2025/CHS/data/toctree.json'
        self.headers_str = '''
        accept: application/json, text/javascript, */*; q=0.01
		accept-language: zh-CN,zh;q=0.9
		cache-control: no-cache
		cookie: excntry=CN; inst-id=UKGBmLemvTnpM8VnUYNi_C9LgrE.14z-pXK99SECroqW0xSzYBeCY4J9lzgD_U0w1bubEAs; ak_bmsc=61A5FDF2B9A0E7E40621DBC86BA2699D~000000000000000000000000000000~YAAQq8HJF5oRAcOSAQAAQTuMxxmKdAEv4AnYdZaPhYIJboYNgTB3ZFYTuYJdbkXpV2pmDo2NDHAE8q7i+sgkyTd735raEwP1MX/YNxfQTTXoTOs5H3XLfpUCflULyp1ZenVeC7YuSbug52bOwCLfLE/Z3OS6hRkIj6DjoUJ/zZq9Hvm4B6F93d3WJpkX71O4waQpTqKOJo3nWwQyVfCBjk5nBRMMy/PNhsl/zdeGpsqjf3yWNPUjzzXO+JhAXlDqY5ODtEMa1f8AI8BBC284h7OfvLwd6wykMHbTFewYiAjngAEU3w3hyVSgzP+Z6756f+SfTkI+4lMI0UgWEaLuvIbe5WnyuTfsE3KgYs6nm1tSEyqlWBl8m9pEpHv1x8U5jsxqSsImtRoVOoRlgbVc+VRuYf8oTWzNFwk1R1BKH3A+aYrl93XnwtTuf3Apgy4vj+SqHlScmNwxUydQvd4=; bm_sv=F162BBC6C334ABCC7AD576F16D738C2F~YAAQq8HJF2pnAcOSAQAAqROWxxkM4Nnm0oPEx5jLE8YjUGPtuITRl6Bxm3NfBbB556/QQoxmXEzz93pu8GiEKVi/+N/hYaCL5UF+C9PfU6UzoLGqJHjoWMhWbwG/Q8LwnFNXarIC9WyFd8H+NmXWITQzE+4XVum8Hp0Kjxsse2j94uSNrh0aL14BFwTgwZzI3Hor2WPD2JN1KyGXV9Ojo7eqYtIVJty6cjVrxqZNtbXouwdlFu+AP1EADeAmY3PHmcRc~1; ack-prod=oBfPYbNcqON1rUqrbpOEGL0qrbRVgZkl; auth-request-id=2ffe1282-5e7a-4b93-947c-6b6cc83fcc82
		pragma: no-cache
		priority: u=1, i
		referer: https://help.autodesk.com/view/MAYAUL/2025/CHS/?guid=GUID-057B91A1-B1E4-49BC-890B-F35A981C4442
		sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"
		sec-ch-ua-mobile: ?0
		sec-ch-ua-platform: "Windows"
		sec-fetch-dest: empty
		sec-fetch-mode: cors
		sec-fetch-site: same-origin
		user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
            '''
        self.headers = dict(
            [[y.strip() for y in x.strip().split(':', 1)] for x in self.headers_str.strip().split('\n') if x.strip()])

    def run_task(self):
        params = {}
        html = requests.get(self.req_url, headers=self.headers, params=params, verify=False).json()
        for item in html.get('books'):
            self.get_content(item)

    def get_content(self, item):
        title = item.get('ttl')
        item_link = item.get('ln')
        # 如果链接不为空，说明有内容，则下载html
        if item_link != '':
            item_link = urljoin(self.req_url, item_link)
            print(f'========================================\n'
                  f'第{self.spider_num}条\n'
                  f'{title}\n'
                  f'{item_link}\n'
                  f'========================================\n')
            self.download_pdf(title, item_link)
            self.spider_num += 1
        # 如果有子节点，继续获取内容
        if item.get('children'):
            for c in item.get('children'):
                self.get_content(c)

    def download_pdf(self, title, link):
        title = clean_filename(title)
        output = fr'{self.folder}{os.path.sep}pdf{os.path.sep}{title}.pdf'
        if os.path.exists(output):
            print('已存在')
            return
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://help.autodesk.com/view/MAYAUL/2025/CHS/?guid=GUID-057B91A1-B1E4-49BC-890B-F35A981C4442",
            "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        }
        cookies = {
            "excntry": "CN",
            "inst-id": "UKGBmLemvTnpM8VnUYNi_C9LgrE.14z-pXK99SECroqW0xSzYBeCY4J9lzgD_U0w1bubEAs",
            "auth-request-id": "d0788d25-e6a3-4e84-9403-40a2e69f1f25",
            "ak_bmsc": "61A5FDF2B9A0E7E40621DBC86BA2699D~000000000000000000000000000000~YAAQq8HJF5oRAcOSAQAAQTuMxxmKdAEv4AnYdZaPhYIJboYNgTB3ZFYTuYJdbkXpV2pmDo2NDHAE8q7i+sgkyTd735raEwP1MX/YNxfQTTXoTOs5H3XLfpUCflULyp1ZenVeC7YuSbug52bOwCLfLE/Z3OS6hRkIj6DjoUJ/zZq9Hvm4B6F93d3WJpkX71O4waQpTqKOJo3nWwQyVfCBjk5nBRMMy/PNhsl/zdeGpsqjf3yWNPUjzzXO+JhAXlDqY5ODtEMa1f8AI8BBC284h7OfvLwd6wykMHbTFewYiAjngAEU3w3hyVSgzP+Z6756f+SfTkI+4lMI0UgWEaLuvIbe5WnyuTfsE3KgYs6nm1tSEyqlWBl8m9pEpHv1x8U5jsxqSsImtRoVOoRlgbVc+VRuYf8oTWzNFwk1R1BKH3A+aYrl93XnwtTuf3Apgy4vj+SqHlScmNwxUydQvd4="
        }
        try:
            html = requests.get(link, headers=headers, cookies=cookies,timeout=10).text
        except:
            time.sleep(2)
            self.download_pdf(title,link)
            return
        # 处理转换过程中的特殊字符
        html = html.replace('<?xml version="1.0" encoding="UTF-8"?>', '<!DOCTYPE html>')
        html = self.make_urls_absolute(html, link)
        html = html.replace('<html xml:lang="zh-cn" lang="zh-cn">', '<html lang="en">')
        html = '<!DOCTYPE html>' + html

        html_folder = fr'{self.folder}{os.path.sep}html'
        pdf_folder = fr'{self.folder}{os.path.sep}pdf'
        if not os.path.exists(html_folder):
            os.makedirs(html_folder)
        if not os.path.exists(pdf_folder):
            os.makedirs(pdf_folder)

        if not os.path.exists(fr'{html_folder}{os.path.sep}{title}.html'):
            write_log(fr'{html_folder}{os.path.sep}{title}.html', html, with_time=False, print_line=False)
        if not os.path.exists(output):
            # html转换成pdf
            # configuration = pdfkit.configuration(wkhtmltopdf=r'D:\Programs\wkhtmltopdf\bin\wkhtmltopdf.exe')
            configuration = pdfkit.configuration(wkhtmltopdf=r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            try:
                pdfkit.from_file(fr'{html_folder}{os.path.sep}{title}.html', output_path=output, configuration=configuration,
                                 options={'encoding': 'utf-8', "enable-local-file-access": True,
                                          'disable-smart-shrinking': ''})
            except Exception as e:
                # print('--->',e)
                write_log(fr'{self.folder}{os.path.sep}log.log', f'{output}\n', with_time=False, print_line=False)

    def make_urls_absolute(self, html, base_url):
        # 处理html页面中的链接及图片信息
        doc = pq(html)
        doc('meta[name="helpsystempath"]').remove()
        for a in doc('a').items():
            href = a.attr('href')
            if href and not href.startswith('http'):
                a.attr('href', urljoin(base_url, href))
        for a in doc('img').items():
            href = a.attr('src')
            if href and not href.startswith('http'):
                img_url = urljoin(base_url, href)
                img_name = img_url[img_url.rfind('/') + 1:]
                save_name = fr'{self.folder}{os.path.sep}images{os.path.sep}{img_name}'
                download_file(save_name, img_url)
                local_path = f'{self.folder}/images'.replace('\\', '/')
                a.attr('src', f'file://{local_path}/{img_name}')
            if href and href.startswith('http'):
                img_url = urljoin(base_url, href)
                img_name = img_url[img_url.rfind('/') + 1:]
                save_name = fr'{self.folder}{os.path.sep}images{os.path.sep}{img_name}'
                download_file(save_name, img_url)
                local_path = f'{self.folder}/images'.replace('\\', '/')
                a.attr('src', f'file://{local_path}/{img_name}')

        for a in doc('link').items():
            href = a.attr('href')
            if href and not href.startswith('http'):
                a.attr('href', urljoin(base_url, href))
        for a in doc('script').items():
            href = a.attr('src')
            if href and not href.startswith('http'):
                a.attr('src', urljoin(base_url, href))

        return doc.outer_html()


if __name__ == '__main__':
    spider = DzSpider()
    spider.run_task()


'''
安装python以下模块：
pdfkit
requests
pyquery
从https://wkhtmltopdf.org/ 网站下载最新版本的，安装到本机，然后替换上面代码中的wkhtmltopdf.exe绝对路径
'''

