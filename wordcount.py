def wordcount(msg):
    space=0
    i=0
    while i<len(msg):
        if msg[i]== " ":
            space=space+1
        i = i+1
    print("In the message we found", space+1, "words")

wordcount("How are you doing")
wordcount("What is going on today")