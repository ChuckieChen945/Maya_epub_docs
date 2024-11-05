# Maya_epub_docs

将[Maya 2025 文档](https://help.autodesk.com/view/MAYAUL/2025/CHS/)制成epub电子书


## 参考链接

<https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/6hGHDwrHzKBq8zd65p4LpK.html>

## 其它

利用Calibre从epub转mobi时，为了能自动生成目录，需在`结构检测>检测章节的XPath表达式`处填入：

```
//*[((name()='h1' or name()='h2') and re:test(., '\s*((chapter|book|section|part)\s+)|((prolog|prologue|epilogue)(\s+|$))', 'i')) or @class = 'chapter' or @class = 'head-block' or @class ='head-text']
```