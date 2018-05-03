inFp = None	# 입력 파일
inStr = ""		# 읽어온 문자열
lineNum = 1

inFp = open(r"C:\Users\user\Desktop\개인작업폴터\교안개발\파이썬과데이터과학\01.강의교안\강의교안강의버전\Code\01.파이썬기초\data1.txt", "r")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print("%d : %s" %(lineNum, inStr), end = "")
    lineNum += 1

inFp.close()
