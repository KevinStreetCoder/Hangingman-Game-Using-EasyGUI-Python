import easygui, random,sys

title="Hanging game"
word_list= ['Python','pygame', 'artificial intelligence','machine learning', 'data science','numpy','pandas','matplotlib','tensorflow',
			'scipy','web scripting','web development','html','css','javascript','c','java','concatenation','string','networking','topology',
			'sql','skillitlearn','hacking','hashing','mapping','computers','hardware','software','algorithms','data structures','linked list',
			'stack','queues','binary tree','heaps','graphs','mesh','array','pointers','inheritance','polymorphism','encapsulation','abstaction',
			'data hiding','cybersecurity','ethical hacking','classes','object','constructors']
choices = ["Play again","Quit"]

def hanged_man(tries = 0): 
    random_word = random.choice(word_list)
    word = ['*' for x in range(len(random_word))] 
    while tries < 5: # number of tries
        guess = easygui.enterbox(f'The word to guess has the below architecure\n {word} \nEnter the word or letter below',title)
        if guess in random_word:
            for ind, item in enumerate(random_word):
                if item==guess:
                    word[ind]=guess
                    if '*' in word:
                        easygui.msgbox(f'Good one! There is letter "{guess}"! And now word looks like {word}',title)
                    else:
                        easygui.msgbox(f'Congratulations! The word is {"".join(word)}',title)
        else:
            easygui.msgbox(f'Try again!You have {5 - tries}',title)
            tries += 1
    if (tries==5 and "*" in word):
        c = easygui.buttonbox('You lose!',title,choices)
        if (c == "Play again"):
            hanged_man()
        else:
            sys.exit()

hanged_man()