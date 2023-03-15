#Biddeer programm


some =[{}]

obj ={}
finish = True 
while   finish :
    actual_name = input('What is your name \n')
    bid_ques = int(input('How much you wanna make a bit in dollars \n'))
    run_again = input('Anyome else "yes" or "no"')
    obj["name"] = actual_name
    obj["price"] = bid_ques
    some.append(obj)
    if run_again == "yes":
        finish=True
    else:
        finish=False
        print('Game finished! ')
        for num in obj:
           print(f"{obj['price']}$")


