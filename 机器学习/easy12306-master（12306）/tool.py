# -*- coding: cp936 -*-
import os
import shutil
import sys

result_fn = sys.argv[1]
classify_fn = sys.argv[2]

# ����ͳ���ж��پ�����������������
s = set()
fp = open(result_fn)
for line in fp:
    (fn, classify) = line.strip().split(' ')
    s.add(int(classify))
fp.close()
print len(s)

# ���������������Ʋ�ʹ�þ���������
fp = open(result_fn)
for idx, line in enumerate(fp):
    (fn, classify) = line.strip().split(' ')
    shutil.copy(os.path.join('ocr', fn), '%s/%s(%d).jpg' % (classify_fn, classify, idx))
