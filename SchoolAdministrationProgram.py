#School Administration Program
import csv

def write_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if(csv_file.tell()==0):#checks if the file is empty
            writer.writerow(["Name", "Age", "Contact No.", "Email ID"])
        writer.writerow(info_list)#takes list value only

if __name__=="__main__":
    student_no=1
    condition=True
    while(condition):
        student_info=input("Enter information for student#{} in format Name, Age, Contact No, Email ID ".format(student_no))
        #store the data in a list using split()
        list=student_info.split(" ")
        print("\nEntered information is\nStudent Name: {}\nAge: {}\nContact No: {}\nEmail id: {}"
              .format(list[0],list[1],list[2],list[3]))
        valid=input("Is the information correct?(yes/no) ")

        if(valid=="yes"):
            student_no+=1
            write_csv(list)
        else:
            print("Please re-enter values")
            continue

        con_check=input("Do you want to enter information for another student :(yes/no) ")
        if(con_check=="yes"):
             condition=True
        elif(con_check=="no"):
                condition = False
        
