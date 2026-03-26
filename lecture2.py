days=["일", "월", "화", "수", "목", "금", "토"]
start=input("시작 요일 입력:")
idx=days.index(start)
result=(idx + 100)% 7
print("100000000일 후 요일:", days[result])


