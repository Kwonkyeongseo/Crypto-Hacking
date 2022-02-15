ENC = 0
DEC = 1

def makeDisk(key):
    keytable = map(lambda x: (chr(x+65), x), range(26))
    # keytable = map(lambda x: (x, chr(x+65)), range(26))

    key2index = {}  

    for t in keytable:
        alphabet, index = t[0], t[1]    
        key2index[alphabet] = index

    if key in key2index:        #k는 입력한 키에 해당하는 인덱스
        k = key2index[key]
    else:
        return None, None

    enc_disk = {}
    dec_disk = {}

    for i in range(26): 
        enc_i = (i+k)%26    #enc_i
        enc_ascii = enc_i + 65  #0~25부터 enc_i에 해당하는 아스키 코드
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i+65)    

    return enc_disk, dec_disk

def caesar(msg, key, mode):
    ret = ''
    key = key.upper()
    msg = msg.upper()
    enc_disk, dec_disk = makeDisk(key)

    if enc_disk is None:
        return ret

    if mode is ENC:
        disk = enc_disk 
    if mode is DEC:
        disk = dec_disk

    for c in msg:
        if c in disk:
            ret += disk[c]
        else:
            ret += c
    
    return ret

def main():
    plaintext = 'hollyweekend'
    key = 't'
    print('Original:\t%s' %plaintext.upper())
    ciphertext = caesar(plaintext, key, ENC)
    print('Caesar Cipher:\t%s' %ciphertext)
    deciphertext = caesar(ciphertext, key, DEC)
    print('Deciphered:\t%s' %deciphertext)

if __name__ == '__main__':
    main()
 