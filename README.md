# OpenCC-to-HanLP
转换[OpenCC](https://github.com/BYVoid/OpenCC/tree/master/data)词典为[HanLP](https://github.com/hankcs/HanLP)格式。

## 用法

```bash
$ python3 opencc_to_hanlp.py
usage: opencc_to_hanlp.py [-h] --opencc_path OPENCC_PATH --output_dir
                          OUTPUT_DIR

Tool for converting dictionaries from OpenCC to HanLP

optional arguments:
  -h, --help            show this help message and exit
  --opencc_path OPENCC_PATH
                        root path to OpenCC
  --output_dir OUTPUT_DIR
                        the folder to store converted dictionaries in HanLP
                        format
```

- `opencc_path` 指向OpenCC的根目录，即`git clone https://github.com/BYVoid/OpenCC.git`后获取到的`OpenCC`目录。
- `output_dir`指向输出目录。

典型用法如下：

```bash
git https://github.com/hankcs/OpenCC-to-HanLP.git
git clone https://github.com/BYVoid/OpenCC.git
cp OpenCC-to-HanLP/extra-config/* /Users/hankcs/CppProjects/OpenCC/data/config/
python3 --opencc_path ./OpenCC --output_dir ./hanlp-tc
tree hanlp-tc
hanlp-tc
├── hk2s.txt
├── s2hk.txt
├── s2t.txt
├── s2tw.txt
├── s2twp.txt
├── t2hk.txt
├── t2hkp.txt
├── t2s.txt
├── t2tw.txt
├── t2twp.txt
├── tw2s.txt
└── tw2sp.txt

0 directories, 12 files
```

这些`txt`词典即为转换后的HanLP格式，用户只需用`s2t.txt`、`t2s.txt`、`t2hk.txt`和`t2tw.txt`替换HanLP项目的`data/dictionary/tc`中相应的`4`个文件，并删除所有`.bin`缓存文件即可。

`t2hkp.txt`和`t2twp.txt`是合并了短语的“短语版”词典，比“精简版”`t2hk.txt`和`t2tw.txt`提供更多分歧词。OpenCC官方不提供相应的配置文件，默认不会生成这两个文件。通过拷贝本项目提供的[extra-config](https://github.com/hankcs/OpenCC-to-HanLP/tree/master/extra-config)到OpenCC的[config](https://github.com/BYVoid/OpenCC/tree/master/data/config)目录，才能生成这两个新文件。导入HanLP时，将这两个文件名中的`p`去掉重复上面的操作即可。

用户可根据自己的需求自由选择，HanLP默认采用了“短语版”词典。

## 转换后的词库下载

方便起见，特提供转换后的词库下载：https://github.com/hankcs/OpenCC-to-HanLP/releases