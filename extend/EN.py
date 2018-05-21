import math
import hashlib
import base64

s = [[0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05, ],
     [0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99, ],
     [0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62, ],
     [0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6, ],
     [0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8, ],
     [0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35, ],
     [0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87, ],
     [0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e, ],
     [0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1, ],
     [0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3, ],
     [0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f, ],
     [0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51, ],
     [0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8, ],
     [0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0, ],
     [0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84, ],
     [0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48]]

FK = [0xa3b1bac6, 0x56aa3350, 0x677d9197, 0xb270022c]
CK = [0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269,
      0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
      0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249,
      0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
      0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229,
      0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
      0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209,
      0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279]


def str2uni(in_text, length):  # str转换为unicode
    out_text = []
    for i in range(length):
        out_text.append(ord(in_text[i]))
    return out_text


def str2bit(in_text):
    out_text = []
    for i in in_text:
        a = bin((ord(i)))
        b = a[2:]
        c = (8 - len(b)) * '0' + b
        out_text.extend(c)
    return out_text


def bit2asc(in_text, length):
    out = []
    temp = 0
    for i in range(length):
        temp = temp | (int(in_text[i]) << (i % 8))
        if i % 8 == 7:
            out.append(temp)
            temp = 0
    return out


def uni2bit(in_text, length):  # unicode转换为二进制
    out_text = []
    for i in range(length * 16):
        out_text.append((in_text[int(i / 16)] >> (i % 16)) & 1)
    if len(out_text) % 128 != 0:
        for j in range(128 - len(out_text) % 128):
            out_text.append(0)
    return out_text


def bit2uni(in_text, length):  # 二进制转换为unicode
    out_text = []
    temp = 0
    for i in range(length):
        temp = temp | (int(in_text[i]) << (i % 16))
        if i % 16 == 15:
            out_text.append(temp)
            temp = 0
    return out_text


def byte2bit(inchar,length):
    outbit=[]
    for i in range(length*8):
        outbit.append((inchar[int(i/8)]>>(i%8))&1)#一次左移一bit
    return outbit


def uni2str(in_text, length):  # unicode转换为字符串
    out_text = ""
    for i in range(length):
        out_text = out_text + chr(in_text[i])
    return out_text


def str28str(in_text):  # key转换为8字节
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUV'
    d = ''
    h = in_text.encode('utf-8')
    a = hashlib.md5(h).hexdigest()
    for f in range(8):
        g = ord(a[f])
        d += s[(g ^ ord(a[f + 8])) - g & 0x1F]

    return d;


def SChange(in_32):  # 输入32位bit list
    sout = []
    for i in range(4):
        s1_1 = in_32[4 * i:4 * i + 3]
        s1_2 = in_32[4 * i + 4:4 * i + 7]
        x = '0b'
        y = '0b'
        for j in s1_1:
            x += str(j)
        for j in s1_2:
            y += str(j)
        z = str(bin(s[int(x, 2)][int(y, 2)]))[2:]
        lent = len(z)
        if lent < 8:
            for j in range(8 - lent):
                z = '0' + z
        sout.append(z)
    sout_end = ''
    for i in sout:
        sout_end += i
    return sout_end


def leftMove(in_text, bit):  # 输入32位bit string 和 移的位数
    output = in_text[bit:] + in_text[:bit]
    return output


def LChange(in_32):  # 输入32位bit string
    c = int(in_32, 2) ^ int(leftMove(in_32, 2), 2) ^ int(leftMove(in_32, 10), 2) ^ int(leftMove(in_32, 18), 2) ^ int(
        leftMove(in_32, 24), 2)
    b = str(bin(c))[2:]
    lent = len(b)
    if lent < 32:
        for j in range(32 - lent):
            b = '0' + b
    return b


def _LChange(in_32):
    c = int(in_32, 2) ^ int(leftMove(in_32, 13), 2) ^ int(leftMove(in_32, 23), 2)
    b = str(bin(c))[2:]
    lent = len(b)
    if lent < 32:
        for j in range(32 - lent):
            b = '0' + b
    return b


def TChange(in_32):  # 输入数字,输出int
    bit = (32 - len(str(bin(in_32))[2:-1])) * '0' + str(bin(in_32))[2:-1]
    sout = SChange(bit)
    lout = LChange(sout)
    lout = int('0b' + lout, 2)
    return lout


def _TChange(in_32):  # 输入数字 输出int
    sout = SChange(in_32)
    lout = _LChange(sout)
    lout = int('0b' + lout, 2)
    return lout


def dealKey(in_key):  # 输入128位list 输出 32*32 list
    RoundKey = []
    SK0b = '0b'
    SK1b = '0b'
    SK2b = '0b'
    SK3b = '0b'
    for i in range(32):
        SK0b += str(in_key[i])
        SK1b += str(in_key[32 + i])
        SK2b += str(in_key[64 + i])
        SK3b += str(in_key[96 + i])
    SK0 = int(SK0b, 2)
    SK1 = int(SK1b, 2)
    SK2 = int(SK2b, 2)
    SK3 = int(SK3b, 2)

    K0 = SK0 ^ FK[0]
    K1 = SK1 ^ FK[1]
    K2 = SK2 ^ FK[2]
    K3 = SK3 ^ FK[3]

    K = [K0, K1, K2, K3]

    for i in range(32):
        a = K[i + 1] ^ K[i + 2] ^ K[i + 3] ^ CK[i]
        b = str(bin(a))[2:]

        lent = len(b)
        if lent < 32:
            for j in range(32 - lent):
                b = '0' + b
        c = []
        for j in b:
            c.append(j)

        K.append(K[i] ^ _TChange(c))
    for j in range(4, 36):
        RoundKey.append(K[j])

    return RoundKey  # int list


def Encode(in_text, inkey, ifen):  # 输入128位二进制list和string key,分组数量
    X1b = '0b'
    X2b = '0b'
    X3b = '0b'
    X4b = '0b'

    termNum = len(in_text)

    key = ''
    for i in inkey:
        key += i

    dKey = str28str(key)
    key = str2uni(dKey, len(dKey))
    dKey = uni2bit(key, len(key))

    if ifen:
        roundKey = dealKey(dKey)
    else:
        roundKey = dealKey(dKey)
        roundKey.reverse()

    C = []

    for k in range(termNum):
        c = []
        X = []
        X1b = ''
        X2b = ''
        X3b = ''
        X4b = ''
        for i in range(32):
            X1b += str(in_text[k][i])
            X2b += str(in_text[k][32 + i])
            X3b += str(in_text[k][64 + i])
            X4b += str(in_text[k][96 + i])

        X = [int(X1b, 2), int(X2b, 2), int(X3b, 2), int(X4b, 2)]
        for i in range(0, 32):
            X.append(X[i] ^ TChange(roundKey[i] ^ X[i + 1] ^ X[i + 2] ^ X[i + 3]))
        for i in range(32, 36):
            a = '0' * (32 - len(str(bin(X[i]))[2:])) + str(bin(X[i]))[2:]

            c.append(a)

        c.reverse()

        for i in c:
            for j in i:
                C.append(j)
    return C  # 输出二进制list


def NMDealIn(in_text):
    str = str2uni(in_text, len(in_text))
    bit = uni2bit(str, len(str))
    termNum = len(bit) // 128
    out = []
    for i in range(termNum):
        a = bit[i * 128:128 * (i + 1)]
        out.append(a)

    return out


def NMDealOut(in_text):
    uni = bit2uni(in_text, len(in_text))
    str = uni2str(uni, len(uni))

    return str


def FLEnDealIn(fileName):
    fl = open(fileName, 'rb')
    byte = fl.read()

    b64 = base64.b64encode(byte)
    string = b64.decode('utf-8')
    print(string)
    uni = str2uni(string, len(string))
    bit = uni2bit(uni, len(uni))
    print(bit)
    termNum = len(bit) // 128
    out = []
    for i in range(termNum):
        a = bit[i * 128:128 * (i + 1)]
        out.append(a)
    return out


def FLEnDealOut(saveName, Cypher):
    fl = open(saveName, 'wb')
    text = bit2asc(Cypher, len(Cypher))
    out = ''
    for i in text:
        out += chr(i)
    cout = bytes(out, encoding="utf8")
    fl.write(cout)

    fl.close()
    return 0


def FLDeDealIn(fileName):
    fl = open(fileName, 'rb')
    byte = fl.read()
    string = bytes.decode(byte)
    tup = []
    for i in string:
        a = ord(i)
        tup.append(a)
    # print(tup)
    bit = byte2bit(tup, len(tup))
    termNum = len(bit) // 128
    out = []
    for i in range(termNum):
        a = bit[i * 128:128 * (i + 1)]
        out.append(a)

    return out


def FLDeDealOut(saveName, Cypher):
    uni = bit2uni(Cypher, len(Cypher))
    stri = uni2str(uni, len(uni))
    byte = base64.b64decode(stri)
    fl = open(saveName, 'wb')
    fl.write(byte)
    fl.close()
    return 0


def NMEN(in_text, key):
    message = NMDealIn(in_text)
    cypher = Encode(message, key, 1)

    out = NMDealOut(cypher)
    return out


def NMDE(in_text, key):
    message = NMDealIn(in_text)

    cypher = Encode(message, key, 0)

    out = NMDealOut(cypher)
    return out


def FLEN(fileName, saveName, key):
    bit = FLEnDealIn(fileName)
    cypher = Encode(bit, key, 1)
    FLEnDealOut(saveName, cypher)
    return 0


def FLDE(fileName, saveName, key):
    print(fileName)
    bit = FLDeDealIn(fileName)
    cypher = Encode(bit, key, 0)
    print(cypher)
    FLDeDealOut(saveName, cypher)
    return 0
