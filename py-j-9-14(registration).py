

while True:
    username="nardis12"
    password="nardis12"

    regmenu=input("1.log in 2.registration 3.exit ")
    while True:
        match regmenu :
            case "1":
                username=input("enter your username:")
                password=input("enter your password:")
                if username =="nardis12" and password =="nardis12":
                    print("log in .")
                if username != "nardis12" and password == "nardis12" :
                    print("your username isn't valid .")
                if username == "nardis12" and password != "nardis12" :
                    print("your password isn't valid .")
                else:
                    print("error .")
            case "2" :
                registration_=input("1.name 2.surname 3.age 4.email 5.address 6.phone 7.postcode 8.gender 9.education:")
                match registration_ :
                    case "1":
                        name=input("enter your name:").capitalize()
                        if name.isalpha()==True :
                            print("your name is correcet .")
                        else:
                            print("your name is incorrect .")
                    case "2":
                        surname=input("enter your surname:").capitalize()
                        if surname.isalpha()==True :
                            print("your surname is correct .")
                        else:
                            print("your surname is incorrect .")
                    case "3":
                        age=int(input("enter your age:"))
                        if age>=18:
                            print("your age is acceptable .")
                        else:
                            print("your age isn't acceptable .")

                    case "4":
                        email=input("enter your email:")
                        if email.endswith(email.com)==True :
                            print("your email is valid .")
                        else:
                            print("your email isn't valid .")
                    case "5":
                        address=input("enter your address:")
                        if address.isalnum()==True :
                            print("your address is correct .")
                        else:
                            print("your address is incorrect .")
                    case "6":
                        phone=int(input("enter your phone:"))
                        if len(phone)==1 :
                            print("your phonenumber is valid .")
                        else:
                            print("your phonenumber isn't valid .")
                    case "7":
                        postcode=int(input("enter your postcode:"))
                        if len(postcode)>=10 :
                            print("your postcode is valid .")
                        else:
                            print("your postcode isn't valid .")
                    case "8":
                        gender=input("enter your gender:").isalpha()
                        if gender == "male" or gender == "female" or gender == "other" :
                            print("your gender is acceptable .")
                        else:
                            print("your gender isn't acceptable .")
                    case "9":
                        edumenu=input("1.high school 2.bachelor 3.master 4.phd :")
                        match edumenu:
                            case "1":
                                score=float(input("enter your score:"))
                                if score<0 or score>20 :
                                    print("your score is incorrect .")
                                if 15<score<=20 :
                                    print("score A .")
                                if 10<score<=15 :
                                    print("score B .")
                                if 5<score<=10 :
                                    print("score C .")
                                if 0<score<=5 :
                                    print("score D .")
                                else:
                                    print("error .")
                            case "2":
                                score=float(input("enter your score:"))
                                if score<0 or score>20 :
                                    print("your score is incorrect .")
                                if 15<score<=20 :
                                    print("score A .")
                                if 10<score<=15 :
                                    print("score B .")
                                if 5<score<=10 :
                                    print("score C .")  
                                if 0<score<=5 :
                                    print("score D .")
                                else:
                                    print("error .")
                            case "3":
                                score=float(input("enter your score:"))
                                if score<0 or score>20 :
                                    print("your score is incorrect .")
                                if 15<score<=20 :
                                    print("score A .")
                                if 10<score<=15 :
                                    print("score B .")
                                if 5<score<=10 :
                                    print("score C .")
                                if 0<score<=5 :
                                    print("score D .")
                                else:
                                    print("error .")
                            case "4":
                                score=float(input("enter your score:"))
                                if score<0 or score>20 :
                                    print("your score is incorrect .")
                                if 15<score<=20 :
                                    print("score A .")
                                if 10<score<=15 :
                                    print("score B .")
                                if 5<score<=10 :
                                    print("score C .")
                                if 0<score<=5 :
                                    print("score D .")
                                else:
                                    print("error .")
                    case "3":
                        break

                        



                     
        
