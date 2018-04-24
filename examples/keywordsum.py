import sys
import ceasercipher as cc


#######################################


def toint(_str, _def):
    ret = 0
    try: 
        ret = int(_str)
    except ValueError:
        ret = _def        
    return ret


if __name__=='__main__':
    ceaser = cc.CeaserCipher()

    # Command line: keywordsum.py [-d] [salt] keyword filename
    mode = ceaser.ENCRYPT
    fn = ""
    argc = len(sys.argv)-1   ## Not including script argument
    isPlainText = True
    hasSalt = False


    # Check if minimum number of arguments
    if (argc<2):
        print('%s [-d] [salt] keyword filename' % sys.argv[0])
        exit()


    # Check for decrypt mode which decodes
    s = sys.argv[1].lower()
    if (len(s)==2 and s=="-d"):
        isPlainText = False
        mode = ceaser.DECRYPT
        argc -= 1


    # Grab arguments
    salt = toint(sys.argv[1+int(isPlainText==False)],0)
    keyword = sys.argv[1+int(isPlainText==False)+int(argc==3)].strip().upper()
    keyword = ciphertable()[0] if len(keyword)==0 else keyword
    fn = sys.argv[2+int(isPlainText==False)+int(argc==3)]



    fnText = open(fn,'r')
    text = fnText.read()
    print(str.format('%-6s:%s,%i:%s'%(ceaser.modeTbl[mode], keyword, salt, text)))
    newText = ceaser.keywordsum(mode, salt, keyword, text)
    mode = ceaser.toggleTbl[mode]
    print(str.format('%-6s:%s,%i:%s'%(ceaser.modeTbl[mode], keyword, salt, newText)))

    
