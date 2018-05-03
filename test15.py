inFp, outFp = None, None 
inStr = ""

inFp = open("C:/Windows/win.ini", "r")
outFp = open(r"C:\Users\user\Desktop\개인작업폴터\교안개발\파이썬과데이터과학\01.강의교안\강의교안강의버전\Code\01.파이썬기초/data3.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사되었음 ---")
