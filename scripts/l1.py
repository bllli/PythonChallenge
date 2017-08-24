# coding=utf-8
def t(s):
    for ch in s:
        if ord('a') <= ord(ch) <= ord('z'):
            # 仅处理a-z字符 跳过空格、标点等
            if (ord(ch) + 2) <= ord('z'):
                # 字符加二后超出z，则从a开始算
                print("%c" % chr(ord(ch) + 2), end='')
            else:
                print("%c" % chr(ord(ch) + 1 + ord('a') - ord('z')), end='')
        else:
            # 直接输出
            print(ch, end='')


def translate(s):
    print('translating "%s" ...' % s)
    t(s)
    print('\n\n')  # 多换两行

translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr yl"
          "b rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

translate('map')
