

while True:
    hospitalmeno=input("1.name 2.surname 3.national id 4.age 5.illness 6.medical history 7.phone 8.address 9.doctor name 01.exit :")
    match hospitalmeno:
        case "1":
            name=input("enter your name:").capitalize()
            if name.isalpha()==True :
                print("your name is correct.")
            else:
                print("your name is incorrect.")
        case "2":
            surname=input("enter your surname:").capitalize()
            if name.isalpha()==True :
                print("your surname is correct.")
            else:
                print("your surname is incorrect.")
        case "3":
            nationalid=int(input("enter your national id:"))
            if len(nationalid)==10 :
                print("your national id is valid.")
            else:
                print("your national id is invalid.")
        case "4":
            age=int(input("enter your age:"))
            if age<18 :
                print("you must be accompanied by one of your parents.")
            else:
                ("your age is acceptable.")
        case "5":
            illness=input("enter your illnes:").capitalize()
            if illness.isalpha()==True:
                print("your illnes is acceptable.")
            else:
                ("your illness isn't acceptable.")
        case "6":
            medicalhistory=input("enter your medicalhistory:").capitalize()
            if medicalhistory.isalpha()==True:
                print("your medical history is acceptable.")
            else:
                print("your medical history isn't acceptable.")
        case "7":
            phone=int(input("enter your phone number:"))
            if len(phone)==11 :
                print("your phone number is valid.")
            else:
                print("your phonr number is invalid.")
        case "8":
            address=input("enter your address:")
            if address.isalnum==True:
                print("your address is acceptable.")
            else:
                print("your address isn't acceptable.")
        case "9":
            doctorname=input("enter your doctor's name:").capitalize()
            if doctorname.isalpha()==True:
                print("your doctor's name is correct.")
            else:
                print("your doctor's name is incorrect.")
        case "11":
            break

                

