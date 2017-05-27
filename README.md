文本分类算法实验


使用方法:

    usage: start.py [-h] -a [{classify,extract}] [-c {raw,scikit}] [-als {gnb}]
                [-cd [{train,classify,regression} [{train,classify,regression} ...]]]
                [-e {jieba}] [-ed [{tags,summary} [{tags,summary} ...]]]

    机器学习小工具

    optional arguments:
      -h, --help            show this help message and exit
      -a [{classify,extract}], --actions [{classify,extract}]
                        需要执行的操作, classifier:分类. extracter:提取关键词和简述
      -c {raw,scikit}, --classifier {raw,scikit}
                        分类器选择
      -als {gnb}, --algorithms {gnb}
                        分类算法选择
      -cd [{train,classify,regression} [{train,classify,regression} ...]], --class_do [{train,classify,regression} [{train,classify,regression} ...]]
                        机器分类的具体操作
      -e {jieba}, --extracter {jieba}
                        提取工具选择
      -ed [{tags,summary} [{tags,summary} ...]], --extract_do [{tags,summary} [{tags,summary} ...]]
                        提取具体操作

    机器学习小工具
