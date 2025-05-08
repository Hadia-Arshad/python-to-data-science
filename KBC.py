print("welcome to KBC")
questions=[
    ("independence day of pakistan is?", ["A 14 Aug", "B 15 sep", "C 16 oct",], "A", 1000),
    ("what is the capital of pakistan?",["A karachi", "B lahore","C islamabad"], "C", 2000),
    ("Historical city of pakistan is?", ["A Karachi", "B lahore", "C Sialkot"], "B", 3000),
    ("how is Allama iqbal?", ["A poet", "B politicion", "c Worker"], "A",4000)
]
total_money=0
for question, option, correct_option, prize in questions:
    print("\n"+question)
    for opt in option:
        print(opt)
    player_answer=input(f"enter your answer A B C for money Rs {prize}, or 0 to quit  ?")
    if player_answer==correct_option:
            total_money+=prize
            print("Move to the next question your total money is:", total_money)
    elif player_answer=="0":
            print(f"Ok you can quit, your total momey is: {total_money}")
            break
    else:
        print("wronge anWser, Game over! your total money is", total_money)
        break
print("Thank you for playing the KBC") 
print(f"money you take to your home is {total_money}")