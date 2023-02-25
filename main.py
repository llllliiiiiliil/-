import papago

papago = papago.Papago()


while True:
    code = int(input("""파파고 월드에 오신걸 환영합니다.
1. 바꾸고 싶은 언어 설정
2. 번역하고 싶은 말 넣기
3. 번역 하기
4. 결과 보기
5. 파파고 월드 종료하기
"""))
    if (code == 1):
        papago.setting()
    if(code == 2):
        papago.translate()
    if(code == 3):
        papago.send()
    if(code == 4):
        papago.getResult()


    if(code == 5):
        break

print("파파고 월드를 사용해주셔서 감사합니다.")