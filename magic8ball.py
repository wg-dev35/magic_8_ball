"""
gui- 8ball.py
author - will - 07/18/23
chpt 8 gui program for a simple magic 8 ball interface
"""
#imports
####MUST HAVE BREEZYPYTHONGUI IN SAME WORKING DIRECTORY#####
from breezypythongui import EasyFrame
import random
from tkinter.font import Font


#Magic 8 ball class
class EightBall(EasyFrame):
    #class constructor method
    def __init__(self):
        EasyFrame.__init__(self, title="Magic 8 Ball", height=200, width=400, background="black", resizable=False)
        #UI elements 
        #colors 
        #text - #cee5f2
        #bg - #23395B
        #fonts
        self.titleFont = Font (family="Monospace", size = 14)
        self.resultFont = Font(family= "Impact", size = 12)
        self.splashFont = Font(family= "Impact", size = 20)

        self.addLabel(text="Magic Eight Ball", row=0, column=0, columnspan=2, sticky="news", font=self.titleFont)
        self.addLabel(text="8", row=2, column=0, columnspan=2, sticky="ns", font=self.splashFont)
       
       
        #input from user
        self.question = self.addTextField(row=1, column=1, text="", sticky="ne", width=30)
        self.addLabel(text="What is your Question?", row=1, column=0, sticky="nw", font=Font(family="Arial", size=12))

        #button
        self.addButton(text="Ask Away...", row=3, column=0, columnspan=2, command= self.shake)

        #response
        self.addLabel(text="You asked: ", row=4, column=0, sticky="nw")
        self.addLabel(text="Magic 8 Ball Says: ", row=5, column=0, sticky="nw")
        #response boxes
        self.inquiry = self.addLabel(text="", row=4, column=1, sticky="ne",background="black", foreground="white")
        self.magicAnswer = self.addLabel(text="", row=5, column=1, sticky="ne",background="black", foreground="white")
        
        
    def shake(self):        
        self.NegAns = ["Don’t count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
        self.PosAns = ["As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes"]
        self.MehAns = ["Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again",]
        self.answers = self.NegAns + self.PosAns+ self.MehAns
        
        inq = self.question.getValue()
        choice = random.choice(self.answers)
       
        self.inquiry["text"] = inq
        self.magicAnswer["text"] = choice
              
        































def main():
    #main run funcition
    EightBall().mainloop()

if __name__ == "__main__":
    main()
