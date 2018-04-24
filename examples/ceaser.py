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

    # Command line: ceaser.py [-d] sub filename
    mode = ceaser.ENCRYPT
    fn = ""
    argc = len(sys.argv)-1   ## Not including script argument
    isPlainText = True


    # Check if minimum number of arguments
    if (argc<2):
        print('%s -d sub filename' % sys.argv[0])
        exit()


    # Check for decrypt mode which decodes
    s = sys.argv[1].lower()
    if (len(s)==2 and s=="-d"):
        isPlainText = False
        mode = ceaser.DECRYPT


    # Grab arguments
    sub = toint(sys.argv[1+int(isPlainText==False)],0)
    fn = sys.argv[2+int(isPlainText==False)]


    if (mode==ceaser.DECRYPT):
        sub = -sub


    fnText = open(fn,'r')
    text = fnText.read()
    print(str.format('%-6s:%i:%s'%(ceaser.modeTbl[mode], sub, text)))
    newText = ceaser.ceaser(sub,text)
    mode = ceaser.toggleTbl[mode]
    print(str.format('%-6s:%i:%s'%(ceaser.modeTbl[mode], sub, newText)))
    
