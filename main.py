import os
import sys
import time
import platform
import venv  
import subprocess


try:
    from termcolor import colored
except:
    os.system("pip install termcolor")
    from termcolor import colored
    
try:
    from tqdm import tqdm
except:
    os.system("pip install tqdm")
    from tqdm import tqdm



operationg_system = platform.system()

def start():
    os.system("cls || clear")
    print(colored(f"    {operationg_system}", "green"))
    print(colored(
    """
        /SSSSSS              /SS                  /SSSSSSS     /SSSSS
       /SS__  SS            | SS                 | SS__  SS   |__  SS
      | SS  \ SS /SS   /SS /SSSSSS    /SSSSSS    | SS  \ SS      | SS
      | SSSSSSSS| SS  | SS|_  SS_/   /SS__  SS   | SS  | SS      | SS
      | SS__  SS| SS  | SS  | SS    | SS  \ SS   | SS  | SS /SS  | SS
      | SS  | SS| SS  | SS  | SS /SS| SS  | SS   | SS  | SS| SS  | SS
      | SS  | SS|  SSSSSS/  |  SSSS/|  SSSSSS/   | SSSSSSS/|  SSSSSS/
      |__/  |__/ \______/    \___/   \______/    |_______/  \______/ 
    ""","red", attrs=["bold"]))



    print(
        colored("  BY --> ", "black", attrs=["bold"]), 
        colored("Suro299", "white", attrs=["bold", "underline"]),
        "    ",
        colored("  git --> ", "black", attrs=["bold"]), 
        colored("https://github.com/Suro299/AutoDJ", "white", attrs=["bold", "underline"]),
        "\n"
        ) 
    
    print(
        colored("  <----------------------------------------------->", "black", attrs=["bold"]),
        "\n"*2,
        colored("  -h", "white", attrs=["bold"]), 
        colored("--> for help", "white"),
        "\n"*3
        ) 


def djhelp(kw = False):
    print(colored("\n  < ------------------------------------------------- > ", "black", attrs=["bold"]), end = "\n\n",)
    
    
    print(colored("\n  you can also write commands via ':' Example` --v:--av ", "red", attrs=["bold"]), end = "\n\n",)
    
    print(colored("\n  <--- VENV ---> ", "white", attrs=["bold"]), end = "\n\n",)
    print(colored("  --v", "white", attrs=["bold"]), end = " --> ")
    print(colored(" (create venv)", "grey", attrs=["bold"]), end = "\n\n")
    
    print(colored("  --av", "white", attrs=["bold"]), end = " --> ")
    print(colored(" (activate venv)", "grey", attrs=["bold"]), end = "\n\n")
    
    print(colored("  --dv", "white", attrs=["bold"]), end = " --> ")
    print(colored(" (deactivate venv)", "grey", attrs=["bold"]), end = "\n\n")
    


def ls():
    print("\n-----------------------")
    os.system("ls || dir")

def is_venv_present():
    try:
        if os.path.exists("venv"):
            if input("Looks like venv already exists, recreate venv ? [y/n]: ").lower().strip() in ("yes", "y", "ya", "да", "д"):
                os.system("rm -rf venv")
                create_venv()
            else:
                print(colored("\n-------------------------------", "red"))
                print(colored("!! Creation of Venv Canceled !! ", "red"))
                print(colored("-------------------------------", "red"))
        else:
            create_venv()
                
    except Exception as ex:
        print(colored("\n----------------------------", "red"))
        print(colored(" !! Create Venv Failed !!", "red"))
        print(ex)
        print(colored("----------------------------", "red"))
    

def create_venv(): 
    print()
    # with tqdm(total=6, desc="Create venv ", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}") as pbar:
        # for _ in range(5):
            # time.sleep(0.1)
            # pbar.update(1)
        # venv.create("./venv")
        # pbar.update(1)
    venv.create("./venv")
    
    
            
    print((colored("\n-----------------------", "green")))
    print((colored("   Venv Created !!", "green")))
    print((colored("-----------------------", "green")))


def handle_argument(keyword):
    if keyword == "-h":
        djhelp()
    elif keyword == "ls":
        ls()  
    elif keyword in ("clear", "cls"):
        start()
    elif keyword == "--v":
        is_venv_present()
    elif keyword == "--av":
        print(colored("\n---------------------------------------------------", "red"))
        print(colored("  !! to use --av write", "red", attrs=["bold"]), end = " ")
        if os.name == "nt":
            print(colored("py main.py --av", "white", attrs=["bold"]), end = " ")
        else:
            print(colored("python3 main.py --av", "white", attrs=["bold"]), end = " ")
        print(colored("!!", "red", attrs=["bold"]))
        print(colored("---------------------------------------------------", "red"), end = "\n\n")
    
    elif keyword == "--dv":
        print(colored("\n---------------------------------------------------", "red"))
        print(colored("  !! to use --dv write", "red", attrs=["bold"]), end = " ")
        if os.name == "nt":
            print(colored("py main.py --dv", "white", attrs=["bold"]), end = " ")
        else:
            print(colored("python3 main.py --dv", "white", attrs=["bold"]), end = " ")
        print(colored("!!", "red", attrs=["bold"]))
        print(colored("---------------------------------------------------", "red"), end = "\n\n")
    else:
        print(colored("\n-----------------------------------------------------", "red"))
        print(colored("  !! to use --dv write", "red", attrs=["bold"]), end = " ")
        print(colored("Command not found -h for help", "red", attrs=["bold"]), end = "\n\n  ")
        print(colored("-h for help ", "white", attrs=["bold"]))
        print(colored("-----------------------------------------------------", "red"), end = "\n\n")
    
def one_line_handle_argument(keyword):
    if keyword == "-h":
        djhelp()
    elif keyword == "ls":
        ls()  
    elif keyword in ("clear", "cls"):
        start()
    elif keyword == "--v":
        is_venv_present()
    elif keyword == "--av":
        pass
        
        # print((colored("\n-----------------------", "green")))
        # print((colored("   Venv Activated !!", "green")))
        # print((colored("-----------------------", "green")))
    

    elif keyword == "--dv":
            print(colored("\n---------------------------------------------------", "red"))
            print(colored("  !! to use --dv write", "red", attrs=["bold"]), end = " ")
            if os.name == "nt":
                print(colored("py main.py --dv", "white", attrs=["bold"]), end = " ")
            else:
                print(colored("python3 main.py --dv", "white", attrs=["bold"]), end = " ")
            print(colored("!!", "red", attrs=["bold"]))
            print(colored("---------------------------------------------------", "red"), end = "\n\n")
    else:
        print(colored("\n-----------------------------------------------------", "red"))
        print(colored("  !! to use --dv write", "red", attrs=["bold"]), end = " ")
        print(colored("Command not found -h for help", "red", attrs=["bold"]), end = "\n\n  ")
        print(colored("-h for help ", "white", attrs=["bold"]))
        print(colored("-----------------------------------------------------", "red"), end = "\n\n")
           



def main():
    args = sys.argv 
    
    if len(args) == 1:
        start()
        while True:
            keyword = input("\n--> ")
            
            if ":" in keyword:
                keyword = keyword.split(":")
                
                for i in keyword:
                    while " " in i:
                        i.replace(" ", "")
                        
                    handle_argument(i.strip().lower())
            else:
                handle_argument(keyword.strip().lower())    
            
                    
    else:
        for i in args[1:]:
            one_line_handle_argument(i.strip().lower())
        
        
        # print(colored("-----------------------------------------------", "red"))
        # print(colored("  !! Hly vor menak Miacnelov a ashxatum !! ", "red"))
        # print(colored("-----------------------------------------------", "red"))
        
    
    # args = sys.argv 
    # if len(args) != 1:
    #     if args[1]  == "sp" and (len(args) == 3 or len(args) == 5):
    #         print("Project created")
    #         if len(args) == 5:
    #             print(f"Add App {args[-1]}")
    #     else:
    #         print("-h for help")




if __name__ == "__main__":
    main()


