#Driving_Test.py
#Creating a driving test program that stores past results.
#March.2020

from tkinter import*
from random import*
import random

root=Tk()
root.title("BATC's Driving Test")
root.geometry("567x200+850+0")

random10questions = []

class Question:
        def __init__(self, prompt, answer):
                self.prompt = prompt
                self.answer = answer
               
driving_questions = [
    "What is the safest way to drive up to intersections? \n(a) Look to the right \n(b) Look to the left \n(c) Look behind you \n(d) All of the above \nAnswer: ", '\n'
         
    "If you have to drive at a slow speed that may hold up other vehicles, what should you do? \n(a) Drive at night when there's less traffic \n(b) Keep to the left and let others pass where possible \n(c) Nothing - drive as normal as it's other drivers' responsibility to overtake you safely \n(d) Keep as close as you can to the centre of the road \nAnswer ", '\n'
         
    "Who is responsible for making a child under 14 years use a seat belt or a safety seat in a vehicle? \n(a) The child's parents \n(b) The driver of the vehicle \n(c) The owner of the vehicle \n(d) The child \nAnswer ", '\n'
         
    "What is the maximum distance a load may overhang your vehicle behind the rear axle? \n(a) 4 Metres \n(b) 5 Metres \n(c) 6 Metres \n(d) 7 Metres \nAnswer ", '\n'
         
    "You must NOT park on the right-hand side of the road, except when: \n(a) In the countryside \n(b) Deliviering packages \n(c) Picking up passengers \n(d) In a one way street \nAnswer ", '\n'
         
    "You are driving in a 100 km/h speed area and you see an Accident sign. What speed must you slow down to? \n(a) 50km/h \n(b) 30km/h \n(c) 40km/h \n(d) 20km/h \nAnswer ", '\n'
         
    "If you have a learner licence you can carry passengers if your supervisor is in the back seat?\n(a) True \n(b) False \nAnswer ", '\n'
           
    "A broken yellow line painted close to the edge of the road means you may stop or park your vehicle there at any time?\n(a) True \n(b) False \nAnswer ", '\n'
           
    "When you have a learner licence you do not have to have it with you when you drive if your supervisor has their licence with them?\n(a) True \n(b) False \nAnswer ", '\n'
         
    "What must you do before turning left into a driveway?\n(a) Check the driveway is clear and enter \n(b) Signal for 3 seconds or more and if the driveway is clear enter \n(c) Signal only if there is a vehicle behind you and enter \n(d) Signal only if another vehicle is coming towards you and enter \nAnswer ", '\n'
         
    "What is the minimum tread depth required for car tyres?\n(a) 0.5mm \n(b) 1.0mm \n(c) 1.5mm \n(d) 2.0mm \nAnswer ", '\n'
           
    "What is the recommended distance you should allow when driving past a cyclist? \n(a) 0.5 metres \n(b) 1.0 metres \n(c) 1.5 metres \n(d) 2.0 metres \nAnswer ", '\n'
           
    "If you can do so safely, you may pass on the left at an intersection if:\n(a) You have the headlights of your vehicle turned on \n(b) The vehicle in front is signalling a right turn \n(c) The vehicle in front is signalling a left turn \n(d) The vehicle in front is going faster than the speed limit \nAnswer ",'\n'
   
    "Can you stop on a bus stop in a private motor vehicle? \n(a) When dropping off passengers \n(b) Only if it is for less than 5 minutes \n(c) Only between midnight and 6am \n(d) No\nAnswer ", '\n'
         
    "You should check that there is space for your vehicle on the other side of the crossing before going over a railway level crossing.\n(a) True \n(b) False \nAnswer ", '\n'
         
    "To help you from being blinded by the headlights of an oncoming vehicle, what should you do?\n(a) Turn the headlights of your vehicle onto high beam \n(b) Look to the right-hand side of the road \n(c) Look at the centre of the road \n(d) Look to the left-hand side of the road \nAnswer ", '\n'
         
    "When must you turn your vehicle headlights on? \n(a) 15 minutes after sunset until 15 minutes before sunrise \n(b) 30 minutes after sunset until 30 minutes before sunrise \n(c) 45 minutes after sunset until 45 minutes before sunrise  \n(d) 1 hour after sunset until 1 hour before sunrise \nAnswer ", '\n'
         
    "What should you do if the vehicle behind you starts to pass you?\n(a)Move over to the right so that they cannot pass \n(b)Speed up so that they will not need to pass \n(c)Signal for them to stay behind you because you think they are going too fast \n(d) Move as far to the left side of the road as is safe and do not speed up \nAnswer ", '\n'
         
    "If anybody is hurt in a crash, the driver must tell a police officer as soon as possible but within:\n(a) 24 hours \n(b) 36 hours \n(c) 48 hours \n(d) 60 hours \nAnswer ", '\n'
   
    "A police officer can impound your car on the spot if you are caught driving while disqualified.\n(a) True \n(b) False \nAnswer ",    
]

driving_answers = [
    Question(driving_questions[0], "d"),
    Question(driving_questions[1], "b"),
    Question(driving_questions[2], "b"),
    Question(driving_questions[3], "a"),
    Question(driving_questions[4], "d"),
    Question(driving_questions[5], "d"),
    Question(driving_questions[6], "b"),
    Question(driving_questions[7], "b"),
    Question(driving_questions[8], "b"),
    Question(driving_questions[9], "b"),
    Question(driving_questions[10], "c"),
    Question(driving_questions[11], "c"),
    Question(driving_questions[12], "b"),
    Question(driving_questions[13], "d"),
    Question(driving_questions[14], "a"),
    Question(driving_questions[15], "d"),
    Question(driving_questions[16], "b"),
    Question(driving_questions[17], "d"),
    Question(driving_questions[18], "a"),
    Question(driving_questions[19], "a")
]    

random.shuffle(driving_questions)
driving_questions[0:11] = random10questions
print (random10questions)

def MainPage():
    global MainPageFrame
    global QuestionsPageFrame
   
    MainPageFrame = LabelFrame(root, height = "500", width = "600", bg ="#fcdd12", text = "")
    MainPageFrame.grid (row=0, column=0)
   
    TitleLabel=Label (MainPageFrame, bg="black", fg="white", width=25, padx=30, pady=1, text="Welcome to BATC's Driving Test", font=("Verdana","22","bold"))
    TitleLabel.grid (columnspan = 50)
   
    DescLabel=Label (MainPageFrame, bg="#fcdd12", fg="black", width=50, height = 3, padx=30, pady=1, text="Please enter your name and age then press next! Good Luck!")
    DescLabel.grid (row = 1, column = 1)    
   
    text2=Label(MainPageFrame, width=11, height=1, bg="black", fg="white", text="Enter name:", relief=RIDGE)
    text2.grid(row=2,column=1)    
   
    text3=Label(MainPageFrame, width=10, height=1, bg="black", fg="white", text="Enter age:", relief=RIDGE)
    text3.grid(row=4,column=1)  
   
    entry2=Entry(MainPageFrame)
    entry2.grid(row=5,column=1)    
   
    entry=Entry(MainPageFrame)
    entry.grid(row=3,column=1)    
   
    button1=Button(MainPageFrame, text="Next Page", anchor = W, command = QuestionsPage)
    button1.grid(row=6,column=0)
   
def QuestionsPage():
    global MainPageFrame
    global QuestionsPageFrame
   
    MainPageFrame.grid_remove()
    QuestionsPageFrame = LabelFrame(root,height="500",width="600", bg="#fcdd12")
    QuestionsPageFrame.grid(row=0, column=0)
   
    QuestionsLabel=Label(QuestionsPageFrame,bg="black",fg="white",width=25,padx=30,pady=1, text="Questions", font=("Verdana","22","bold"))
    QuestionsLabel.grid(columnspan=50)    
   
    Desc2Label=Label (QuestionsPageFrame, bg="#fcdd12", fg="black", width=61, height = 3, text="Click next to start the driving test. Enter your answer (a, b, c or d) in the entry box.")
    Desc2Label.grid (row = 1, columnspan=4, sticky = E)    
   
    questions = Label(QuestionsPageFrame, text = "", width = 18, height = 3, bg="#fcdd12")
    questions.grid (row = 2, column = 0, sticky = E)

    answer_entry = Entry (QuestionsPageFrame, width = 7)
    answer_entry.grid (row = 2, column = 1, sticky = W)
   
    nextquestion = Button (QuestionsPageFrame, text = "Next", width = 5, relief = RIDGE)
    nextquestion.grid (row = 4,column = 1)    
   
    homescreen=Button(QuestionsPageFrame,text="Home Page",anchor=W,command=MainPage , relief = RIDGE)
    homescreen.grid(row=2 , column=0)

MainPage()
root.mainloop()