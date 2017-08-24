# coding=utf-8
# see: http://www.runoob.com/python3/python3-string-maketrans.html
instr = 'abcdefghijklmnopqrstuvwxyz'
outstr = 'cdefghijklmnopqrstuvwxyzab'
t = str.maketrans(instr, outstr)


def translate(s):
    print('translating "%s" ...' % s)
    print(s.translate(t))
    print('\n\n')  # 多换两行

translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr yl"
          "b rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

translate('map')
