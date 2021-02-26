import json

Questions = json.load(open('questions.json'))
results = json.load(open('results.json'))

total = 0

print("歡迎來到菲爾人格測試！")
input("(請按Enter鍵以繼續)")

for question in Questions:
	print(question["question"])
	for option in question["options"]:
		print(option)
	user_input = None
	while (user_input not in range(len(question["options"]))):
		try:
			user_input = int(input("請輸入選項並按下Enter鍵：")) - 1
		except:
			pass
	total += question["scores"][user_input]

print("\n\n")
print("你作答完畢囉！")
print("你總共得到" + str(total) + "分")

def section(score):
	if score <= 20:
		return 0
	elif score > 60:
		return 5
	else:
		return int(score / 10)

result = results[section(total)]
print("\n\n")
print("因為你的分數在" + result["range"])
print("你的人格是 " + result["title"])

print("\n\n")
print("關於這個人格，詳細地來說是這樣：\n" + result["description"])