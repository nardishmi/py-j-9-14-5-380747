
studentcode=1808
while True:
    menu = input("1.register student 2.Show student information 3.add course 4. delete course 5.exit")
    while True:
        match menu:
            case "1":
                registration = input(" 1.Name 2.Surname 3.Age 4.national id 5.Major 6.exit")
                match registration:
                    case "1":
                        name=input("Enter name: ").capitalize()
                        if name.isalpha() == True:
                            print("Name saved .")
                        else:
                            print("Invalid name .")
                    case "2":
                        surname=input("Enter surname: ").capitalize()
                        if surname.isalpha() == True:
                            print("Surname saved .")
                        else:
                            print("Invalid surname .")
                    case "3":
                        age=int(input("Enter age: "))
                        if age.isdigit() == True:
                            print("Age saved .")
                        else:
                            print("Invalid age .")
                    case "4":
                        nationalid=input("Enter national id: ")
                        if nationalid.isdigit() == True:
                            print("national id saved.")
                        else:
                            print("invalid national id")
                    case "5":
                        major=input("Enter major: ").capitalize()
                        print("major saved.")
                    case "6":
                        break

            case "2":
                print(studentcode)
                print(name)
                print(surname)
                print(age)
                print(nationalid)
                print(major)
                print(course1)
                print(course2)

            case "3":
                course=input("1.Add first course 2.Add second course 3.exit")
                match course:
                    case "1":
                        course1=input("Enter course name: ").capitalize()
                        print("Course added")
                    case "2":
                        course2=input("Enter course name: ").capitalize()
                        print("Course added")
                    case "3":
                        break

            case "4":
                course=input("1.delete first course 2.delete second course 3.exit")
                match course:
                    case "1":
                        course1="course1"
                        print("First course deleted")

                    case "2":
                        course2 = "course2"
                        print("Second course deleted")

                    case "3":
                        break
            case "5":
                if menu.isdigit() == True:
                    print("Invalid menu number")
                else:
                    break 
