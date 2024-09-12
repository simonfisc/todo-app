import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index, "-", alternative)
    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer
    if question["user_answer"] == question["correct_answer"]:
        score = score + 1

for question in data:
    

print(data)
print(score, "/", len(data))