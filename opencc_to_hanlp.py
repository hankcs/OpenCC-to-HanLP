# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-06-27 20:37
import argparse
import glob
import json
import os
import sys


def convert_single(json_path, output_path):
    print('转换 {} 为 {} 通过合并'.format(json_path, output_path), end=' ')
    opencc_data = os.path.dirname(os.path.dirname(json_path))
    with open(json_path) as json_fp, open(output_path, 'w') as out:
        dic = dict()
        config = json.load(json_fp)
        for chain in config['conversion_chain']:
            dicts = chain['dict'].get('dicts', None)
            if not dicts:
                dicts = [chain['dict']]
            for dic_item in dicts:
                dic_txt = dic_item['file'].replace('.ocd', '.txt')
                rev = False
                if not os.path.isfile(os.path.join(opencc_data, 'dictionary', dic_txt)) and 'Rev' in dic_txt:
                    rev = True  # 有些Rev文件不存在，需要动态逆转
                    dic_txt = dic_txt.replace('Rev', '')
                print(dic_txt, end=' ')
                dic_txt = os.path.join(opencc_data, 'dictionary', dic_txt)
                if os.path.isfile(dic_txt):
                    load_dic(dic, dic_txt, rev)
                else:  # 有些文件需要动态合并
                    for file in glob.glob(dic_txt.replace('.txt', '*.txt')):
                        load_dic(dic, file, rev)
        for first, second in sorted(dic.items()):
            out.write('{}={}\n'.format(first, second))
    print()


def load_dic(dic, dic_txt, rev):
    with open(dic_txt) as src:
        for line in src:
            cells = line.strip().split()
            if not cells:
                continue
            first, second = cells[0], cells[1]
            if rev:
                first, second = second, first
            dic[first] = second


def convert_all(opencc_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for json_file in glob.glob(os.path.join(opencc_path, 'data', 'config', '*.json')):
        convert_single(json_file, os.path.join(output_dir, os.path.basename(json_file).replace('.json', '.txt')))
    print('转换完毕，词典保存在目录 {}'.format(output_dir))


def main():
    arg_parser = argparse.ArgumentParser(description='Tool for converting dictionaries from OpenCC to HanLP')
    arg_parser.add_argument('--opencc_path', required=True, help='root path to OpenCC')
    arg_parser.add_argument('--output_dir', required=True,
                            help='the folder to store converted dictionaries in HanLP format')
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    args = arg_parser.parse_args()
    convert_all(args.opencc_path, args.output_dir)


if __name__ == '__main__':
    main()
