"""Ceaser Cipher

This is a fun little module that implements encryption/decryption using
the Ceaser cipher.  The purpose of which is to 

Example:
    First import the ceasercipher module, then...

        ceaser = CeaserCipher()

        cipher = ceaser.ceaser(>0, plain)
        plain  = ceaser.ceaser(<0, cipher)

        cipher = ceaser.keyword(ENCRYPT, keyword, plain)
        plain  = ceaser.keyword(DECRYPT, keyword, cipher)

        cipher = ceaser.keywordsum(ENCRYPT, initvalue, keyword, plain)
        plain  = ceaser.keywordsum(DECRYPT, initvalue, keyword, cipher)

Todo:
    * Customize cipher table with a list because A-Z doesn't have to be in order ;)

"""
class CeaserCipher:
    """ Collection of various ceaser substitution methods """
    ENCRYPT = False
    DECRYPT = True
    _cipherTable = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    modeTbl = {ENCRYPT:'Plain',DECRYPT:'Cipher'}
    toggleTbl = {ENCRYPT:DECRYPT, DECRYPT:ENCRYPT}


    def ciphertable(self):
        return self._cipherTable

    def ceaser(self, sub, text):
        cipher = ""
        table = self.ciphertable()
        start = ord(table[0])

        for s in text:
            if s.isalpha()==False:
                cipher += s
                continue
            c = ord(s.upper()) + sub - start
            cipher += chr(start + (c % len(self.ciphertable())))

        return cipher


    def keyword(self, mode, keyword, text):
        cipher = ""
        table = self.ciphertable()
        start = ord(table[0])
        ikeyword = 0
        sub = 1 if mode==self.ENCRYPT else -1

        for s in text:
            if s.isalpha()==False:
                cipher += s
                continue
            c = ord(s.upper())-start + sub*(ord(keyword[ikeyword])-start)
            cipher += chr(start + (c % len(table)))
            ikeyword = (ikeyword+1) % len(keyword)

        return cipher


    def keywordsum(self, mode, salt, keyword, text):
        ret = ""
        table = self.ciphertable()
        start = ord(table[0])
        ikeyword = 0
        accum = salt

        if (mode==self.ENCRYPT):
            cipher = ""
            for s in text:
                if s.isalpha()==False:
                    cipher += s
                    continue
                c = ord(s.upper())-start + (ord(keyword[ikeyword])-start) + accum
                accum += c
                accum %= len(table)
                cipher += chr(start + (c % len(table)))
                ikeyword = (ikeyword+1) % len(keyword)

            ret = cipher
        else:
            plain = ""
            for s in text:
                if s.isalpha()==False:
                    plain += s
                    continue
                p = ord(s.upper())-start - ((ord(keyword[ikeyword])-start) + accum)
                if (p<0):
                    p += len(table)
                c = p + (ord(keyword[ikeyword])-start) + accum
                accum += c
                accum %= len(table)
                plain += chr(start + (p % len(table)))
                ikeyword = (ikeyword+1) % len(keyword)
            ret = plain

        return ret

