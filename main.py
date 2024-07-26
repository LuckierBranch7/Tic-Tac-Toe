canvas = {'7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '}

boardKeys = []

for key in canvas:
    boardKeys.append(key)

def printCanvas(canvas):
    print(canvas['7'] + '|' + canvas['8'] + '|' + canvas['9'])
    print('-+-+-')
    print(canvas['4'] + '|' + canvas['5'] + '|' + canvas['6'])
    print('-+-+-')
    print(canvas['1'] + '|' + canvas['2'] + '|' + canvas['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printCanvas(canvas)
        print("It's your turn, " + turn + ". Move to which place?")

        move = input()

        if canvas[move] == ' ':
            canvas[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        
        if count >= 5:
            if canvas['7'] == canvas['8'] == canvas['9'] != ' ':
                printCanvas(canvas)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif canvas['4'] == canvas['5'] == canvas['6'] != ' ':
                printCanvas(canvas)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif canvas['1'] == canvas['2'] == canvas['3'] != ' ':
                printCanvas(canvas)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif canvas['1'] == canvas['4'] == canvas['7'] != ' ':
                printCanvas(canvas)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif canvas['2'] == canvas['5'] == canvas['8'] != ' ':
                printCanvas(canvas)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    restart = input("\nDo want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in boardKeys:
            canvas[key] = " "

        game()

if __name__ == "__main__":
    game()