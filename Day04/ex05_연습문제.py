f = open("test2.txt","r")
# 파일의 내용을 body변수에 저장
body = f.read()
f.close()
# 문자열 변경
body = body.replace("java", "python")
# 파일을 쓰기 모드로 실행
f = open("test2.txt","w", encoding="utf-8")
f.write(body)
f.close()
