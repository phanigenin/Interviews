import re

def betterCompression(s):
    res = {}
    sr = set([ c for c in s if c.isalpha()])
    for c in sr:
        numbers = re.findall(c+'\d+', s)
        for ch in numbers:
            actualchar = ch[0]
            res[actualchar] = res.get(actualchar,0)+int(ch[1:])

    strres=""
    for key in sorted(res.keys()):
      strres += "%s%d" % (key, res[key])
    return strres


def betterCompression2(s):
    #res = {}
    sr = set([ c for c in s if c.isalpha()])

    res = {}.fromkeys(sr,0)
    for c in sr:
        numbers = re.findall(c+'\d+', s)
        for ch in numbers:
            actualchar = ch[0]
            res[actualchar] = res.get(actualchar,0)+int(ch[1:])


    strres=""
    for key in sorted(res.keys()):
      strres += "%s%d" % (key, res[key])
    return strres

def betterCompression3(s):
    res = {}
    sr = set([ c for c in s if c.isalpha()])
    for c in sr:
        numbers = re.findall(c+'\d+', s)
        res[c] = sum([int(ch[1:])for ch in numbers])

        '''
                for ch in numbers:
            actualchar = ch[0]
            res[actualchar] = res.get(actualchar,0)+int(ch[1:])
        '''


    strres=""
    for key in sorted(res.keys()):
      strres += "%s%d" % (key, res[key])
    return strres


input='a12c20b56c1'
print(betterCompression(input))
print(betterCompression2(input))
print(betterCompression3(input))

