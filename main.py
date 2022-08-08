from classes.functions import features, bcolors

running = True
while running:
    print(bcolors.BOLD+bcolors.HEADER +
          "\nWelcome to your TODO app\n------------------------"+bcolors.ENDC)
    name = input("Please enter your name: ")

    # Bringing features class
    todo = features(name)

    if(todo.get_user(name)):
        print("-----------------------------")
        print(bcolors.GREEN+bcolors.BOLD+bcolors.UNDERLINE +
              "\nWelcome, "+name+"!"+"\n"+bcolors.ENDC)

        while running:
            todo.menu()
            menuchoice = input(
                bcolors.BLUE+"Enter action number: "+bcolors.ENDC)

            if(menuchoice == "4"):
                print(bcolors.RED+"\n\nExiting App now!!!"+bcolors.ENDC)
                running = False
            else:
                todo.do_actions(menuchoice)

    else:
        print(bcolors.RED+"\nYou don't have a profile.\n"+bcolors.ENDC)
        createprofile = input(
            bcolors.BLUE+"\nWould you like to create one (y/n)? : "+bcolors.ENDC)
        if createprofile == "y":
            todo.create_profile()
        if createprofile == "n":
            print(bcolors.RED+"\n\nExiting App now!!!"+bcolors.ENDC)
            running = False
