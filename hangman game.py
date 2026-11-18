import random
words = ['spider', 'oxygen', 'mouse', 'click', 'maggie']

def game(count=0, guessed='', wrong='', matched=0):
    secret_word = random.choice(words)
    print("the total letters in secret word is: ", len(secret_word))
    while count<6:
        for j in secret_word:
            print(j if j in guessed else "_", end=" ")
        print()

        guess = input("Enter the letter: ")
        if guess in guessed:
            print('already guessed')
        else:
            if guess in secret_word:
                print('correct guess')
                guessed+=guess
                matched+=secret_word.count(guess)
                if matched==len(secret_word):
                    print("You got the right word: ", secret_word)
                    break
            else:
                if guess in wrong:
                    print("Repeated wrong mistake")
                else:
                    count+=1
                    wrong+=guess
                    print("wrong guess! Tries left:", 6 - count)
                    if count==6:
                        print("the correct word was: ", secret_word)
                        break
while True:
    game(count=0, guessed='', wrong='', matched=0)
    ans = input("Want to play again (yes/no): ")
    if ans not in ['Yes', 'yes', 'y']:
        break
