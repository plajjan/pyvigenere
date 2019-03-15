# port of https://github.com/plajjan/java-CiscoVigenere

__ikey = 'dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87'

def encrypt(m, init):
    key = __ikey[init:len(__ikey)] + __ikey[0:init]
    res = '{:02d}'.format(init)
    return res +\
           ''.join(['{:02X}'.format(ord(m[i]) ^ ord(key[i % len(key)])) for i in range(0, len(m))])

def decrypt(s):
    init = int(s[0:2])
    key = __ikey[init-1:len(__ikey)] + __ikey[0:init-1]
    return ''.join([chr(int(s[2*i:2*i+2], base=16) ^ ord(key[i % len(key)])) for i in range(1, int(len(s)/2))])

if __name__ == '__main__':
    e = encrypt('letmein', 9)
    print(e)
    print(decrypt(e))
