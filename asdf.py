import random
def main():
	win = 0
	lose = 0 
	draw = 0
	counter = 0
	while counter <10 :
		print("무엇을 낼 것인지 정하십시오.(1~3,1번:가위,2번:바위,3번:보)")
		computer = random.randint(1,3)
		player = input()
		if int(player) == 1:
			if computer == 1:
				draw += 1
				counter += 1
				print("비겼습니다")
			if computer == 2:
				lose += 1
				counter += 1
				print("졌습니다")
			if computer ==3:
				win += 1
				counter += 1
				print("이겼습니다")
		if int(player) == 2:
			if computer == 1:
				win += 1
				counter += 1
				print("이겼습니다")
			if computer == 2:
				draw += 1
				counter += 1
				print("비겼습니다")
			if computer ==3:
				lose += 1
				counter += 1
				print("졌습니다")
		if int(player) == 3 :
			if computer == 1:
				lose += 1
				counter += 1
				print("졌습니다")
			if computer == 2:
				win += 1
				counter += 1
				print("이겼습니다")
			if computer == 3 :
				draw += 1
				counter += 1
				print("비겼습니다")
		if int(player)> 3 : 
			print("제대로 된 숫자를 입력해 주세요")
		if int(player) < 1 :
			print("제대로 된 숫자를 입력해 주세요")
	print("플레이어는 ",win,"번 승리하셨습니다.")
	print("플레이어는 ",lose,"번 패배하셨습니다.")
	print("플레이어는 ",draw,"번 비기셨습니다.")

main()

