import random
import time

OPERATORS = ['+', '-', '*']
MIN = 3
MAX = 12
PROBLEMS = 8

def generate_problem ():
    left = random.randint(MIN, MAX)
    right = random.randint(MIN, MAX)
    operand = random.choice(OPERATORS)

    problem = str(left) + ' ' + operand + ' ' + str(right)
    answer = eval(problem)

    return problem, answer

wrong = 0
start_time = time.time()

input("Naciśnij ENTER żeby zacząć ")
print("____________________________")

for i in range(PROBLEMS):
    problem, answer = generate_problem()
    while True:
        guess = input("Działanie #" + str(i+1) + ": " + problem + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
accuracy = 100 - ((wrong / PROBLEMS) * 100)

print("Koniec! zadania rowiązano w", total_time, "sekund, z dokładnością", accuracy, "%")
print("____________________________")