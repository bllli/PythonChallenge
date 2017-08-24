Python 挑战
-----------------

解决 http://www.pythonchallenge.com/ 上的33道题

Level 0
`````````

2的38次方... 这没啥难度吧?

Level 1
`````````

读题:

K -> M
O -> Q
E -> G

貌似是凯撒密码(每个字母被往后位移三格字母所取代)， 所以移回去试一下。

Python3代码::

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

执行结果::

    translating "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj." ...
    i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.


    translating "map" ...
    ocr

可知下一关在 http://www.pythonchallenge.com/pc/def/ocr.html

使用推荐的string.maketrans()，结果不变::

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

Level 2
``````````
recognize the characters. maybe they are in the book,
but MAYBE they are in the page source.

给的图这么模糊，字符肯定在源码里面。 源码中有提示"find rare characters in the mess below"。所以找到一千多行乱码里面的字符就行了.

Python3代码::

    raw = """太长不写 详见scripts/l2.py"""
    for c in raw:
    if ord('a') <= ord(c) <= ord('z'):
        print(c, end='')

输出::

    equality

可知下一关为 http://www.pythonchallenge.com/pc/def/equality.html

Level3
````````

One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

说是要找到被**确切的**三个大写字母环绕的小写字母。网页的标题是re，就是说要用正则表达式来处理。

看网页源码 果然有一大堆。

我的第一个想法是找出*前后***环绕着**三个大写字母的小写字母，有三个就行了，所以我的匹配式为 `[A-Z]{3}([a-z])[A-Z]{3}`

答案不对。

随后我的思路是*上下左右*环绕着三个大写字母的小写字母。每行有80个字符和一个换行符，所以所以我的匹配式为

`[A-Z].{81}[A-Z].{81}[A-Z].{78}[A-Z]{3}([a-z])[A-Z]{3}.{78}[A-Z].{81}[A-Z].{81}[A-Z]`

还是不对。

随后 小写字母前后**有且仅有**三个大写字母。

`[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]`

Python3代码::

    raw = """太多了 详见scripts/l3.py"""
    r = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', raw)

    if r:
        print(r)
        print(''.join(r))

