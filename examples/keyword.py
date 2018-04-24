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

    # Command line: keyword.py [-d] keyword filename
    mode = ceaser.ENCRYPT
    fn = ""
    argc = len(sys.argv)-1   ## Not including script argument
    isPlainText = True


    # Check if minimum number of arguments
    if (argc<2):
        print('%s [-d] keyword filename' % sys.argv[0])
        exit()


    # Check for decrypt mode which decodes
    s = sys.argv[1].lower()
    if (len(s)==2 and s=="-d"):
        isPlainText = False
        mode = ceaser.DECRYPT


    # Grab arguments
    keyword = sys.argv[1+int(isPlainText==False)].strip().upper()
    keyword = ceaser.ciphertable()[0] if len(keyword)==0 else keyword
    fn = sys.argv[2+int(isPlainText==False)]



    fnText = open(fn,'r')
    text = fnText.read()
    print(str.format('%-6s:%s:%s'%(ceaser.modeTbl[mode], keyword, text)))
    newText = ceaser.keyword(mode, keyword, text)
    mode = ceaser.toggleTbl[mode]
    print(str.format('%-6s:%s:%s'%(ceaser.modeTbl[mode], keyword, newText)))

    
