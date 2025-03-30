#Quiz Game
#10 questions and answers 
def main():
    print("Quiz Game - Capitals\n")
    questions={1: "What is the capital of France?", 2: "What is the capital of Canada?", 3: "What is the capital of Spain?", 4: "What is the capital of Brazil?", 5: "What is the capital of Argentina?", 6: "What is the capital of Japan?", 7: "What is the capital of Russia?", 8: "What is the capital of Australia?", 9: "What is the capital of Poland?", 10: "What is the capital of Germany?"}
    answers={1: "Paris", 2: "Ottowa", 3: "Madrid", 4: "Brasilia", 5: "Buenos Aires", 6: "Tokyo", 7: "Moscow", 8: "Canberra", 9: "Warsaw", 10: "Berlin"}
    num=10
    quiz(questions, answers, num)

def quiz(q, a, n):
    k=0
    correct=0
    while k < n:
        k+=1
        player=input(q[k]+": ").lower()
        if player == a[k].lower():
            print("Correct answer!\n")
            correct+=1
        else:
            print(f"Incorrect Answer!\nThe correct answer would be: {a[k]}\n") 
    print(f"\nThanks for taking the quiz!\nYour score: {correct}/{n}")
main()                                       