

while True:
    username="nardis12"
    password="nardis12"
    repairshopmenu=input("1.registration 2.log in 3.option 4.exit :")
    while True:
        match repairshopmenu :
            case "1":
              username=input("enter your username:")
              password=input("enter your password:")
              print("registration completed .")
            case "2":
                username=input("enter your username:").capitalize()
                password=input("enter your password:").capitalize()
                if username == "nardis12" and password=="nardis12":
                    print("log in .")
                if username != "nardis12" and password == "nardis12":
                    print("your username is incorrect .")
                if username == "nardis12" and password != "nardis12" :
                    print("your password is incorrect .")
                else:
                    print("error .")
            case "3":
                optionmenu=input("1.name 2.surname 3.phone 4.car model 5.car color 6.plate number 7.car service 8.exit :")
                match optionmenu :
                    case "1":
                        name=input("enter your name:").capitalize()
                        if name.isalpha() == True :
                            print("name entered .")
                        else:
                            print("name is invalid .")
                    case "2":
                        surname=input("enter your surname:").capitalize()
                        if surname.isalpha() == True :
                            print("surname entered .")
                        else:
                            print("surname is invalid .")
                    case "3":
                        phone=int(input("enter your phone:"))
                        if phone == 11 :
                            print("phone is valid .")
                        else:
                            print("phone is invalid .")
                    case "4":
                        model=input("enter your car model :").capitalize()
                        print("car model entered .")
                    case "5":
                        color=input("enter your car color :").capitalize()
                        print("car color entered .")
                    case "6":
                        plate=input("enter your plate number :")
                        if plate.isalnum() == True :
                            print("your plate number entered .")
                        else:
                            print("your plate number is invalid .")
                    case "7":
                        servicemenu=input("1.oilchange 2.brakepad 3.engine 4.carwash 5.exit : ")
                        match servicemenu :
                            case "1":
                                oilchangemenu=("1.persian 2000 2.imported 4000 3.exit:")
                                match oilchangemenu :
                                    case "1":
                                        numoilpersian=int(input("enter number:"))
                                        persianoilprice=int(input("oil price :"))
                                        persianolichangeprice=1.1*persianoilprice*numoilpersian
                                        print(persianolichangeprice)
                                        break
                                    case "2":
                                        numoilimported=int(input("enter number:"))
                                        importedoilprice=int(input("oil price :"))
                                        importedoilchangeprice=1.1*importedoilprice*numoilimported
                                        print(importedoilchangeprice)
                                        break
                                    case "3":
                                        break
                            case "2":
                                brakepadmenu=input("1.persian 4000 2.imported 8000 3.exit : ")
                                match brakepadmenu :
                                    case "1":
                                        numbrakepadpersian=int(input("enter number:"))
                                        persianbrakepadprice=int(input("oil price :"))
                                        persianbrakepadchangeprice=1.1*persianoilprice*numbrakepadpersian
                                        print(persianbrakepadchangeprice)
                                        break
                                    case "2":
                                        numbrakepadimported=int(input("enter number:"))
                                        importedbrakepadprice=int(input("oil price :"))
                                        importedbrakepadchangeprice=1.1*importedbrakepadprice*numbrakepadimported
                                        print(importedbrakepadchangeprice)
                                        break
                                    case "3":
                                        break
                            case "3":
                                enginemenu=input("1.persian 10000 2.imported 20000 3.exit :")
                                match enginemenu :
                                    case "1":
                                        numenginepersian=int(input("enter number:"))
                                        persianengineprice=int(input("engine price :"))
                                        persianenginechangeprice=1.1*persianengineprice*numenginepersian
                                        print(persianenginechangeprice)
                                        break
                                    case "2":
                                        numengineimported=int(input("enter number:"))
                                        importedengineprice=int(input("engine price :"))
                                        importedenginechangeprice=1.1*importedengineprice*numengineimported
                                        print(importedenginechangeprice)
                                    case "3":
                                        break  
                            case "4":
                                carwash=input("1.economy 500 2.vip 1000 3.exit :")
                                match carwash :
                                    case "1":
                                        economynum=int(input("enter number:"))
                                        economyprice=int(input("enter price:"))
                                        economyprice_=1.1*economynum*economyprice
                                        print(economyprice_)
                                    case "2":
                                        vipnum=int(input("enter number:"))
                                        vipprice=int(input("enter price:"))
                                        vipprice_=1.1*vipnum*vipprice
                                        print(vipprice_)
                                    case "3":
                                        break
                            case "5":
                                break
            case "4":
                break













