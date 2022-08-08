import simplejson as json
import os


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class features:

    def __init__(self, name):
        self.name = name
        self.actions = ["View Tasks", "Add New Task", "Mark Completed", "Exit"]

    def get_user(self, name):
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'tasks.json')

        if os.path.isfile(filename) and os.stat(filename).st_size != 0:
            tskfile = open(filename, "r")
            data = json.loads(tskfile.read())

            for item in data["users"]:
                if item["name"] == name:
                    return True
        else:
            open(filename, "w")
            return False

    def menu(self):
        i = 1
        print(bcolors.BLUE + bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1
        print("-----------------------------")

    def do_actions(self, actionnumber):
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'tasks.json')
        tskfile = open(filename, "r")
        data = json.loads(tskfile.read())

        if (actionnumber == "1"):
            for item in data["users"]:
                if item["name"] == self.name:
                    i = 0
                    print("-----------------------------")
                    print(bcolors.GREEN+bcolors.BOLD + bcolors.UNDERLINE +
                          "\nYour Tasks: \n"+bcolors.ENDC)

                    if len(item["tasks"]) == 0:
                        print("    "+"You have no tasks.")
                    else:
                        for task in item["tasks"]:
                            print("    " + str(i+1)+".", task)
                            i += 1
            print("-----------------------------")

        elif (actionnumber == "2"):
            for item in data["users"]:
                if item["name"] == self.name:
                    print("---------------------------------------")
                    newtask = input(
                        bcolors.GREEN+"Enter a new task: "+bcolors.ENDC)
                    item["tasks"].append(newtask)
            with open(filename, "w") as file:
                json.dump(data, file)

            print(bcolors.GREEN+"\nTask Successfully Added!"+bcolors.ENDC)

            for item in data["users"]:
                if item["name"] == self.name:
                    i = 0
                    print("---------------------------------------")
                    print(bcolors.GREEN+bcolors.BOLD + bcolors.UNDERLINE +
                          "\nYour Tasks: \n"+bcolors.ENDC)
                    for task in item["tasks"]:
                        print("    " + str(i+1)+".", task)
                        i += 1
            print("-----------------------------")

        elif (actionnumber == "3"):
            for item in data["users"]:
                if item["name"] == self.name:
                    print("---------------------------------------")
                    completetask = input(
                        bcolors.GREEN+"Enter task number to mark complete: "+bcolors.ENDC)
                    item["tasks"].pop(int(completetask)-1)
            with open(filename, "w") as file:
                json.dump(data, file)

            print(bcolors.GREEN+"\nTask Mark Completed!"+bcolors.ENDC)

            for item in data["users"]:
                if item["name"] == self.name:
                    i = 0
                    print("---------------------------------------")
                    print(bcolors.GREEN+bcolors.BOLD + bcolors.UNDERLINE +
                          "\nYour Tasks: \n"+bcolors.ENDC)
                    for task in item["tasks"]:
                        print("    " + str(i+1)+".", task)
                        i += 1
            print("-----------------------------")

    def create_profile(self):
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'tasks.json')
        with open(filename, "r+") as file:
            data = json.load(file)

            newprofile_entry = {"name": self.name, "tasks": []}

            data["users"].append(newprofile_entry)

            file.seek(0)
            json.dump(data, file, indent=4)

        print(bcolors.GREEN+"\nProfile created Successfully!"+bcolors.ENDC)
