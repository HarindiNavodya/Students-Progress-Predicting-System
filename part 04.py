#K.A.Harindi Navodya
#student_id - 20220541
#date - 14/12/2022

cre_p = 0
cre_d = 0
cre_f= 0
dictionary = {}

def validateid ():
    global student_id
    while True:
        student_id = input("Enter your UOW number:").lower()
        if len(student_id) == 8 and student_id[0] == 'w' and student_id[1:8].isdigit():#www.w3schools.com. (n.d.). Python String isdigit() Method. [online] Available at: https://www.w3schools.com/python/ref_string_isdigit.asp.
            if student_id not in dictionary:
                dictionary[student_id] = {}
            else:
                print("student id already exist")
                break
        else:
            print("Invalid student id,please try again")
            continue
        return student_id


def validate_credits() :
    while True:
        global cre_p, cre_d, cre_f

        while True:
            try :
                cre_p = int(input("Please enter your credits at pass: "))
                
            except :
                print("Enter an integer")
                continue
            if cre_p not in (0,20,40,60,80,100,120) :
                print("This value is Out of range. Please re-enter below ")
            else :
                break
                   

        while True:
            try :
                cre_d = int(input("Please enter your credits at Defer: "))
            except :
                print("Enter an integer")
                continue
            if cre_d not in (0,20,40,60,80,100,120) :
                print("This value is Out of range. Please re-enter below ")
            else :
                break
                
            
            
        while True:
            try :
                cre_f = int(input("Please enter your credits at Fail: "))
                
            except :
                print("Enter an integer")
                continue
            if cre_f not in (0,20,40,60,80,100,120) :
                print("This value is Out of range. Please re-enter below ")
            else :
                break
             
            
        ProgressionOutcomes()
        break

def ProgressionOutcomes() :
        
        
    if cre_p == 120 and cre_d == 0 and cre_f == 0:
            dictionary[student_id] = {}
            dictionary[student_id] = "Progress :", cre_p, cre_d, cre_f
                            
    elif cre_p == 100 and (cre_d == 20 or cre_d == 0) and (cre_f == 0 or cre_f == 20):
            dictionary[student_id] = {}
            dictionary[student_id] = "Progress (Module Trailer):", cre_p, cre_d, cre_f
    elif cre_p == 80  and (cre_d == 40 or cre_d == 20 or cre_d == 0) and (cre_f == 0 or cre_f == 20 or cre_f == 40):
            dictionary[student_id] = {}
            dictionary[student_id] = "Do not Progress- Module retriever :", cre_p, cre_d, cre_f
    elif cre_p == 60 and (cre_d == 60 or cre_d == 40 or cre_d == 20 or cre_d == 0) and (cre_f == 0 or cre_f == 20 or cre_f == 40 or cre_f == 60):
            dictionary[student_id] = {}
            dictionary[student_id] = "Do not Progress- Module retriever :", cre_p, cre_d, cre_f
    elif cre_p == 40 and (cre_d == 80 or cre_d == 60 or cre_d == 40 or cre_d == 20) and (cre_f == 0 or cre_f == 20 or cre_f == 40 or cre_f == 60):
            dictionary[student_id] = {}
            dictionary[student_id] = "Do not Progress- Module retriever :", cre_p, cre_d, cre_f
    elif cre_p == 40 and cre_d == 0 and cre_f == 80:
            dictionary[student_id] = {}
            dictionary[student_id] = "Exclude :", cre_p, cre_d, cre_f
    elif cre_p == 20 and (cre_d == 100 or cre_d == 80 or cre_d == 60 or cre_d == 40) and (cre_f == 0 or cre_f == 20 or cre_f == 40 or cre_f == 60):
            dictionary[student_id] = {}
            dictionary[student_id] = "Do not Progress- Module retriever :", cre_p, cre_d, cre_f
    elif cre_p == 20 and (cre_d == 20 or cre_d == 0) and (cre_f == 80 or cre_f == 100):
            dictionary[student_id] = {}
            dictionary[student_id] = "Exclude :", cre_p, cre_d, cre_f
    elif cre_p == 0 and (cre_d == 120 or cre_d == 100 or cre_d == 80 or cre_d == 60) and (cre_f == 0 or cre_f == 20 or cre_f == 40 or cre_f == 60):
            dictionary[student_id] = {}
            dictionary[student_id] = "Do not Progress- Module retriever :", cre_p, cre_d, cre_f
    elif cre_p == 0 and (cre_d == 40 or cre_d == 20 or cre_d == 0) and (cre_f == 80 or cre_f == 100 or cre_f == 120):
            dictionary[student_id] = {}
            dictionary[student_id] = "Exclude :", cre_p,cre_d,cre_f

        
            
def Main() :
    while True :
        Question = input("Would you like to enter an another set of data?\n Enter 'y' for yes and 'q' for quit:")
        print()
        if Question == "y" :
            while True :
                validateid()
                validate_credits()
                Main()
                break
        elif Question == "q" :
            
            while True :
                ProgressionOutcomes()
                print(dictionary)
                raise SystemExit



validateid()
validate_credits()
Main()






    
