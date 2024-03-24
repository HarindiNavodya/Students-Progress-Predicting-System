# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20220541 
# Date: 14/12/2022 

progress_count = 0
trailer_count = 0
exclude_count = 0
retriever_count = 0
progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []
cre_p = 0
cre_d = 0
cre_f = 0




def Total(cre_p, cre_d, cre_f):
    if (cre_p + cre_d + cre_f) != 120:
        print("total incorrect")

def Range(cre_p, cre_d, cer_f):
    if (cre_p or cre_d or cre_f) not in range (0,121,20):
        print ("out of range")

while True:
    while True:
        try:
            cre_p = int(input("Please enter your credits at pass:"))
            if Range (cre_p, cre_d, cre_f):
                continue
            cre_d = int(input("Please enter your credits at defer:"))
            if Range (cre_p, cre_d, cre_f):
                continue
            cre_f = int(input("Please enter your credits at fail:"))
            if Range (cre_p, cre_d, cre_f):
                continue
            
        except ValueError:
            print("Integer required")
            break
        if Total (cre_p, cre_d, cre_f):
            continue
        else:
            break
    if cre_p == 120 and cre_d == 0 and cre_f == 0:
        print('Progress')
        progress_count += 1
        progress_list.append([str(cre_p),str(cre_d),str(cre_f)])
        
    elif cre_p == 100 and (cre_d == 20 or cre_d == 0) and (cre_f == 0 or cre_f == 20):
        print('Progress(module trailer)')
        trailer_count += 1
        trailer_list.append([str(cre_p),str(cre_d),str(cre_f)])
    elif cre_p == 80  and (cre_d == 40 or cre_d == 20 or cre_d == 0) and (cre_f == 0 or cre_f == 20 or cre_f == 40):
        print('Do not Progress-module retriever')
        retriever_count += 1
        retriever_list.append([str(cre_p),str(cre_d),str(cre_f)])
    elif cre_p == 60 and (cre_d == 60 or cre_d == 40 or cre_d == 20 or cre_d == 0) and (cre_f == 0 or cre_f == 20 or cre_f == 40 or cre_f == 60):
        print('Do not Progress-module retriever')
        retriever_count += 1
        retriever_list.append([str(cre_p),str(cre_d),str(cre_f)])
    elif cre_p == 40 and (cre_d == 80 or cre_d == 60 or cre_d == 40 or cre_d == 20) and (cre_f == 0 or cre_f == 20 or cre_f == 40 or cre_f == 60):
        print('Do not Progress-module retriever')
        retriever_count += 1
        retriever_list.append([str(cre_p),str(cre_d),str(cre_f)])
    elif cre_p == 40 and cre_d == 0 and cre_f == 80:
        print('Exclude')
        exclude_count += 1
        exclude_list.append([str(cre_p),str(cre_d),str(cre_f)])
    elif cre_p == 20 and (cre_d == 100 or cre_d == 80 or cre_d == 60 or cre_d == 40) and (cre_f == 0 or cre_f == 20 or cre_f == 40 or cre_f == 60):
        print('Do not Progress-module retriever')
        retriever_count += 1
        retriever_list.append([str(cre_p),str(cre_d),str(cre_f)])
    elif cre_p == 20 and (cre_d == 20 or cre_d == 0) and (cre_f == 80 or cre_f == 100):
        print('Exclude')
        exclude_count += 1
        exclude_list.append([str(cre_p),str(cre_d),str(cre_f)])
    elif cre_p == 0 and (cre_d == 120 or cre_d == 100 or cre_d == 80 or cre_d == 60) and (cre_f == 0 or cre_f == 20 or cre_f == 40 or cre_f == 60):
        print('Do not Progress-module retriever')
        retriever_count += 1
        retriever.append([str(cre_p),str(cre_d),str(cre_f)])
    elif cre_p == 0 and (cre_d == 40 or cre_d == 20 or cre_d == 0) and (cre_f == 80 or cre_f == 100 or cre_f == 120):
        print('Exclude')
        exclude_count += 1
        exclude_list.append([str(cre_p),str(cre_d),str(cre_f)])
    
    
    print()
    program = str(input("Would you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: "))
    print()
    if program == 'y':
        input()
        
    elif program == 'q':
        
            
        print('---------------------------------------------------------------------------------------------------------------------------------------------')
        print("Histogram")
        print('Progress',progress_count, ':' , '*' * progress_count)
        print('Trailer',trailer_count, ':' , '*' * trailer_count)
        print('Retriever', retriever_count, ':' , '*' * retriever_count)
        print('Exclude', exclude_count, ':' , '*' * exclude_count)
        print(progress_count + trailer_count + retriever_count + exclude_count,"outcomes in total.")
        print('--------------------------------------------------------------------------------------------------------------------------------------------------')
        break
    else:
        print('Invalid Options')
        program = str(input("Enter 'q' to quit or 'y' to add another student:"))
        print()
    
with open('programming.txt', 'w') as file:
    for progress in progress_list:
        print("Progress - ", ",".join(progress) )
        file.write("Progress - " + ",".join(progress))#www.w3schools.com. (n.d.). Python String join() Method. [online] Available at: https://www.w3schools.com/python/ref_string_join.asp.
        file.write("\n")
    for trailer in trailer_list:
        print("Progress(module trailer)- ", ",".join(trailer) )
        file.write("Progress(module trailer)- " + ",".join(trailer))
        file.write("\n")
    for retriever in retriever_list:
        print("Do not Progress-module retriever - ", ",".join(retriever) )
        file.write("Do not Progress-module retriever - " + ",".join(retriever))
        file.write("\n")
    for exclude in exclude_list:
        print("Exclude - ", ",".join(exclude))
        file.write("Exclude - " + ",".join(exclude))
        file.write("\n")
        




        
    
    
