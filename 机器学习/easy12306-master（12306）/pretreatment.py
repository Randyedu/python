# -*- coding: cp936 -*-
# ���ܣ���ͼ�����Ԥ���������ֲ��ֵ�����ȡ����
# ����ŵ�ocrĿ¼��
# �ļ���Ϊԭ��֤���ļ����ļ���
import cv2
import os


def read_img(fn):
    '''
    �õ���֤������ͼ��
    :param fn:ͼ���ļ�·��
    :return:ͼ�����
    '''
    return cv2.imread(fn)


def write_img(im, fn):
    cv2.imwrite(fn, im)


def get_text_img(im):
    '''
    �õ�ͼ���е��ı�����
    '''
    return im[3:22, 127:184]


def binarize(im):
    '''
    ��ֵ��ͼ��
    '''
    gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    (retval, dst) = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    return dst


def show_img(im):
    print im.ndim, im.dtype
    cv2.imshow("image", im)
    cv2.waitKey(0)


if __name__ == '__main__':
    img_names = os.listdir('img')
    for img_name in img_names:
        im = read_img(os.path.join('img', img_name))
        im = get_text_img(im)
        im = binarize(im)
#        show_img(im)
        write_img(im, os.path.join('ocr', img_name))
