

while True:
    gymmenu=input("1.name 2.surname 3.national id 4.age 5.phone 6.address 7.sport's major 8.membership duration 9.exit :")
    match gymmenu:
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
                print("your age is acceptable.")
        
        case "5":
            phone=int(input("enter your phone number:"))
            if len(phone)==11 :
                print("your phone number is valid.")
            else:
                print("your phonr number is invalid.")
        case "6":
            address=input("enter your address:")
            if address.isalnum==True:
                print("your address is acceptable.")
            else:
                print("your address isn't acceptable.")
        case "7":
            sportsmenu=("1.bodybuilding 2.yoga 3.pilates 4.functional 5.swimming 6.exit :")
            match sportsmenu:
                case "1":
                    sport=input("enter sport:").capitalize()
                    if sport.isalpha==True and sport == bodybuilding :
                        print("bodybuilding.")
                case "2":
                    sport=input("enter sport:").capitalize()
                    if sport.isalpha==True and sport == yoga :
                        print("yoga.")
                case "3":
                    sport=input("enter sport:").capitalize()
                    if sport.isalpha==True and sport == pilates :
                        print("pilates.")
                case "4":
                    sport=input("enter sport:").capitalize()
                    if sport.isalpha==True and sport == functional :
                        print("functional.")
                case "5":
                    sport=input("enter sport:").capitalize()
                    if sport.isalpha==True and sport == swimming :
                        print("swimming.")
                case "6":
                    break 
        case "8":
            durationmenu=input("1.one month 2.three month 3.six month 4.one year 5.exit :")
            match durationmenu:
                case "1":
                    duration=input("enter your membership duration:")
                    if duration.isalnum()==True and duration=="1month" :
                        print("1 month membership.")
                case "2":
                     duration=input("enter your membership duration:")
                     if duration.isalnum()==True and duration=="3month" :
                        print("3 month membership.")
                case "3":
                    duration=input("enter your membership duration:")
                    if duration.isalnum()==True and duration=="6month" :
                        print("6 month membership.")
                case "4":
                     duration=input("enter your membership duration:")
                     if duration.isalnum()==True and duration=="12month" :
                        print("1 year membership.")
                case "5":
                    break 
        case "9":
            break