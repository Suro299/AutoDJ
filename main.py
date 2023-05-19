import os
import sys
import time
import platform


        
try:
    from termcolor import colored
except:
    os.system("cls || clear")
    
    if input("\n\nThe program requires the termcolor package. Do you want to install it ? [y/n]: ").lower().strip() in ("yes", "y", "ya", "да", "д"):
        os.system("pip install termcolor")
        from termcolor import colored
        os.system("cls || clear")
        
        print(colored("\n------------------------------------------------------------", "green"))
        print(colored("!! termcolor has been successfully installed!! ", "green"))
        print(colored("------------------------------------------------------------", "green"))
    else:
        sys.exit()


try:
    from tqdm import tqdm
except:
    if input("\n\nThe program requires the tqdm package. Do you want to install it ? [y/n]: ").lower().strip() in ("yes", "y", "ya", "да", "д"):
        os.system("pip install tqdm")
        from tqdm import tqdm
    else:
        sys.exit()

try:
    import django
except:
    if input("\nThe program requires the django package. Do you want to install it ? [y/n]: ").lower().strip() in ("yes", "y", "ya", "да", "д"):
        os.system("pip install django")
        print(colored("\n------------------------------------------------------------", "green", attrs=["bold"]))
        print(colored("!! Django has been successfully installed !! ", "green", attrs=["bold"]))
        print(colored("------------------------------------------------------------", "green", attrs=["bold"]), end = "\n\n")
    else:
        sys.exit()




def start():
    os.system("cls || clear")
    print(colored(f"    {platform.system()}", "green"))
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
    
    print(colored("  <----------------------------------------------->", "black", attrs=["bold"]), end = "\n\n")
    
    if os.name == "nt":
        print(colored("   py main.py -hh", "white", attrs=["bold"]), end = " ")
    else:   
        print(colored("   python3 main.py -h", "white", attrs=["bold"]), end = " ")

    print(colored("--> for help", "white"), end = "\n\n")    
    

def djhelp(kw = False):
    print(colored("\n  < ------------------------------------------------- > ", "black", attrs=["bold"]), end = "\n\n",)
    
    
    print(colored("\n  you can also write commands via ':' Example` --v:--av ", "red", attrs=["bold"]), end = "\n\n",)
    
    print(colored("\n  <--- VENV ---> ", "grey", attrs=["bold"]), end = "\n",)
    print(colored("  --v", "white", attrs=["bold"]), end = " --> ")
    print(colored(" (create venv)", "grey", attrs=["bold"]), end = "\n\n\n")
    
    print(colored("\n  <--- DJANGO ---> ", "grey", attrs=["bold"]), end = "\n",)
    print(colored('  --sp project_name (default "core" ) ', "white", attrs=["bold"]), end = " --> ")
    print(colored(" ( Create Project )", "grey", attrs=["bold"]), end = "\n\n")
    print(colored('  --sa app_name -p project_name ', "white", attrs=["bold"]), end = " --> ")
    print(colored(" ( Create App )", "grey", attrs=["bold"]), end = "\n\n")
    

def ls():
    print("\n-----------------------")
    os.system("ls || dir")



def is_venv_present():
    try:
        if os.path.exists("venv"):
            if input("Looks like venv already exists, recreate venv ? [y/n]: ").lower().strip() in ("yes", "y", "ya", "да", "д"):
                create_venv()
            else:
                print(colored("\n-------------------------------", "red", attrs=["bold"]))
                print(colored("!! Creation of Venv Canceled !! ", "red", attrs=["bold"]))
                print(colored("-------------------------------", "red", attrs=["bold"]))
        else:
            create_venv()
                
    except Exception as ex:
        print(colored("\n----------------------------", "red", attrs=["bold"]))
        print(colored(" !! Create Venv Failed !!", "red", attrs=["bold"]))
        print(colored(f"\n Exception: {ex}", "red", attrs=["bold"]))
        print(colored("----------------------------", "red", attrs=["bold"]))
    

def create_venv(): 
    print()
    with tqdm(total=4, desc="Create venv ", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}") as pbar:
        for _ in range(3):
            time.sleep(0.1)
            pbar.update(1)
        if os.name == 'nt':
            os.system("py -m venv venv")
        else:
            os.system("python3 -m venv venv")
        pbar.update(1)
    
            
    print((colored("\n-----------------------", "green")))
    print((colored("   Venv Created !!", "green")))
    print((colored("-----------------------", "green")))



def create_project(project_name):
    if os.getenv('VIRTUAL_ENV'):
        if os.path.exists(project_name):
            print(colored("\n---------------------------------------", "red", attrs=["bold"]))
            print(colored(f"  !! {project_name} already exists !! ", "red", attrs=["bold"]))
            print(colored("---------------------------------------", "red", attrs=["bold"]))
        else:
            os.system(f"django-admin startproject {project_name}")
            print(colored("\n------------------------------------------------------------", "green", attrs=["bold"]))
            print(colored(f'!! Django project "{project_name}" has been successfully created !! ', "green", attrs=["bold"]))
            print(colored("------------------------------------------------------------", "green", attrs=["bold"]), end = "\n\n")
     
    else:
        os.system("cls || clear ")
        print(colored("\n-----------------------------------------------------", "red"))
        print(colored("  !! Please activate venv !!", "red", attrs=["bold"]), end = "\n\n")

        if os.name == 'nt':
            print(colored("  venv\Scripts\activate.bat", "white", attrs=["bold"]))
        else:
            print(colored("  source venv/bin/activate", "white", attrs=["bold"]))
        print(colored("-----------------------------------------------------", "red"), end = "\n\n") 
        
        if not(os.path.exists("venv")):
            if input("Looks like you don't have venv, would you like to create venv? [y/n]: ").lower().strip() in ("yes", "y", "ya", "да", "д"):
                create_venv()
            else:
                sys.exit()

def template_creating(project_name, app_name):
    if not(os.path.exists(f"{project_name}/{app_name}/templates")):
        os.mkdir(f"{project_name}/{app_name}/templates")
        os.mkdir(f"{project_name}/{app_name}/templates/{app_name}")
        print(colored(f"{app_name} --> templates/{app_name} Creating", "green"))
    
        with open(f"{project_name}/{app_name}/templates/{app_name}/index.html", "w") as file:
            print(colored(f"{app_name} --> {app_name}.html Creating", "green"))
            
            file.write("")
            file.write('{% load static %}\n\n' + '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + """    <link rel="stylesheet" href="{% static """ + f""" '{app_name}/css/style.css' %""" + '}">' + f'\n    <title> {app_name} - index </title>\n</head>\n<body>\n  <h1> Barev </h1>  \n</body>\n</html>')
            print(colored(f"{app_name} --> {app_name}.html Changed", "green"))
        
        print(colored(f"{app_name} --> {project_name}/{app_name}/templates Creating", "green"))
        
        
        
    if not(os.path.exists(f"{project_name}/{app_name}/static")):
        os.mkdir(f"{project_name}/{app_name}/static")
        os.mkdir(f"{project_name}/{app_name}/static/{app_name}")

        os.mkdir(f"{project_name}/{app_name}/static/{app_name}/css")
            
        with open(f"{project_name}/{app_name}/static/{app_name}/css/style.css", "w") as file:
            file.write("")
            file.write("/* Karoche css a */\n\n")
            print(colored(f"{app_name} --> {project_name}/{app_name} CSS Creating", "green"))

        print(colored(f"{app_name} --> {project_name}/{app_name}/static Creating", "green"))


def app_urls(project_name, app_name):
    with open(f"{project_name}/{app_name}/urls.py", "w") as file:
        file.write("")
        print(colored(f"{app_name} --> {project_name}/{app_name}/urls.py Creating", "green"))
        file.write(f'from django.urls import path\nfrom . import views\n\nurlpatterns = [\n   path("", views.index, name = "index")\n]')
        print(colored(f"{app_name} --> {project_name}/{app_name}/urls.py Changed", "green"))
        

def app_views(project_name, app_name):
    with open(f"{project_name}/{app_name}/views.py", "r") as text:
        text = text.read()

    with open(f"{project_name}/{app_name}/views.py", "a") as file:
        print(colored(f"{app_name} --> {project_name}/{app_name}/views.py Creating", "green"))
        if "def index(" not in text:
            
            file.write(f'\n\ndef index(request):\n    return render(request, "{app_name}/index.html")')
        
            print(colored(f"{app_name} --> {project_name}/{app_name}/views.py Changed", "green"))
            
            
def app_views(project_name, app_name):
    with open(f"{project_name}/{app_name}/views.py", "r") as text:
        text = text.read()

    with open(f"{project_name}/{app_name}/views.py", "a") as file:
        if "def index(" not in text:
            file.write(f'\n\ndef index(request):\n    return render(request, "{app_name}/index.html")')
        
        print(f"{app_name} --> {app_name}/views.py Changed")

def static_media_apps(app_name, project_name):
    with open(f"{project_name}/{project_name}/settings.py", "r") as file:
        file = file.read()
        
    installed_apps = file[file.index("INSTALLED_APPS") : file.index("MIDDLEWARE")-2]
    skzb_installed_apps = installed_apps
    installed_apps = installed_apps.replace("INSTALLED_APPS = [", "").replace("]", "").strip().split(",\n")
    
    installed_apps = [i.strip().replace(",", "") for i in installed_apps]
    
    new_istalled_apps = "INSTALLED_APPS = [\n"
    for i in installed_apps:
        new_istalled_apps += f"    {i},\n"
    
    
    if f"'{app_name}'" not in installed_apps:
        new_istalled_apps += f"    '{app_name}',\n"
    
    new_istalled_apps += "]"
    file = file.replace(skzb_installed_apps, new_istalled_apps)
    
    
    file = file.replace("'DIRS': [],", """'DIRS': [
            BASE_DIR/"templates"
            ],""")


    if "MEDIA_URL = 'media/'" not in file and "STATIC_ROOT = BASE_DIR/'static'" not in file and "MEDIA_ROOT = BASE_DIR/'media'" not in file:  
        file = file.replace("STATIC_URL = 'static/'", "STATIC_URL = 'static/'\nSTATIC_ROOT = BASE_DIR/'static'\n\nMEDIA_URL = 'media/'\nMEDIA_ROOT = BASE_DIR/'media'")


    with open(f"{project_name}/{project_name}/settings.py", "w") as new_text:
        new_text.write(file)
    
    print(colored(f"\n{app_name} --> {project_name}/{project_name}/settings.py Changed", "green"))
    

def urls_ch(project_name, app_name):
    with open(f"{project_name}/{project_name}/urls.py", "r") as file:
        file = file.read()
    
    urlpatterns = file[file.index("urlpatterns = "):file.index("]")+1:]
    
    if f'path("", include("{app_name}.urls"))' not in urlpatterns:
        urlpatterns = urlpatterns.replace("path('admin/', admin.site.urls),", f"""path('admin/', admin.site.urls),\n    path("", include("{app_name}.urls")),""")

    if " + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)" not in urlpatterns:
        urlpatterns += " + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)"

    with open(f"{project_name}/{project_name}/urls.py", "w") as new_file:
        new_file.write("from django.contrib import admin\nfrom django.urls import path, include\nfrom django.conf import settings\nfrom django.conf.urls.static import static\n\n")
        new_file.write(urlpatterns)
        new_file.write("")
    
    print(colored(f"{app_name} --> {project_name}/{project_name}/urls.py Changed", "green"))

                
def create_app(project_name, app_name):
    try:
        if os.path.exists(project_name):
            
            if not(os.path.exists(f"{project_name}/{app_name}")):
                os.system(f"cd {project_name} ; python manage.py startapp {app_name}")

                print(colored("\n------------------------------------------------------------", "green", attrs=["bold"]))
                print(colored(f'!! Application {app_name} was successfully created in {project_name} !! ', "green", attrs=["bold"]))
                print(colored("------------------------------------------------------------", "green", attrs=["bold"]), end = "\n\n")

                print(colored("\n----------------------------------------------------------------------------------------", "red", attrs=["bold"]))
                print(colored(f'  !! Remember every time you create an application, it is added to the {project_name}/urls.py !! ', "red", attrs=["bold"]))
                print(colored("----------------------------------------------------------------------------------------", "red", attrs=["bold"]), end = "\n\n")


                if input(f"\nYou have created {app_name} in {project_name}, do you want to automatically configure settings.py, urls.py, connect statics and media? [y/n]: ").lower().strip() in ("yes", "y", "ya", "да", "д"):



                    try:
                        static_media_apps(app_name, project_name)
                        template_creating(project_name, app_name)
                        app_urls(project_name, app_name)
                        app_views(project_name, app_name)
                        urls_ch(project_name, app_name)
                    except:
                        print(colored("\n---------------------------------------", "red", attrs=["bold"]))
                        print(colored("  !! Something went wrong !! ", "red", attrs=["bold"]), end = "\n\n")
                        print(colored("  Exception: ", "white", attrs=["bold"]), end = "")
                        print(colored(f"{ex} ", "white"))
                        print(colored("---------------------------------------\n", "red", attrs=["bold"]))

                else:
                    sys.exit()
            else:
                print(colored("\n---------------------------------------", "red", attrs=["bold"]))
                print(colored(f"  !! {project_name}/{app_name} Already exists  !! ", "red", attrs=["bold"]))
                print(colored("---------------------------------------\n", "red", attrs=["bold"]))
        
        else:
            print(colored("\n-----------------------------------------", "red", attrs=["bold"]))
            print(colored(f"  !! Project {project_name} not found !! ", "red", attrs=["bold"]), end = "\n")
            print(colored("---------------------------------------\n", "red", attrs=["bold"]))
            if input(f"\nDo you want to create a project {project_name} ? [y/n]: ").lower().strip() in ("yes", "y", "ya", "да", "д"):
                create_project(project_name)
            
        
    except Exception as ex:
        print(colored("\n---------------------------------------", "red", attrs=["bold"]))
        print(colored("  !! App creation canceled !! ", "red", attrs=["bold"]), end = "\n\n")
        print(colored("  Exception: ", "white", attrs=["bold"]), end = "")
        print(colored(f"{ex} ", "white"))
        print(colored("---------------------------------------\n", "red", attrs=["bold"]))
        

def keyword_handler(args):
    if args[1].lower() == "--v":
        is_venv_present()
    elif args[1].lower() == "-h":
        djhelp()
        
    elif args[1].lower() == "--sp":
        if len(args) < 4:
            if len(args) > 2:
                create_project(args[2])
            else:
                create_project("core")
        else:
            print(colored("\n---------------------------------------", "red", attrs=["bold"]))
            print(colored("  !! Too many arguments !! ", "red", attrs=["bold"]), end = "\n\n")
            print(colored('  try ` --sa app_name -p project_name ', "white", attrs=["bold"]), end = "\n")
            print(colored("---------------------------------------", "red", attrs=["bold"]))
    elif args[1].lower() == "--sa":
        if "-p" in args:
            if len(args) == 5:
                create_app(args[4], args[2])               
        else:
            print(colored("\n-----------------------------------------------------", "red"))
            print(colored("  !! Please enter project name !!", "red", attrs=["bold"]), end = "\n\n")
            print(colored("  For example` ", "white", attrs=["bold"]), end = " ")
            if os.name == 'nt':
                print(colored("py main.py --sa main in core", "white"))
            else:
                print(colored("python3 main.py --sa app_name -p project_name", "white"))
            print(colored("-----------------------------------------------------", "red"), end = "\n\n") 
  
    
    else:
        print(colored("\n---------------------------------------", "red", attrs=["bold"]))
        print(colored("  !! Command not found !! ", "red", attrs=["bold"]), end = "\n\n")
        print(colored('  try ` -h ', "white", attrs=["bold"]), end = "\n")
        print(colored("---------------------------------------", "red", attrs=["bold"]))
            
            
            
            
            
            
            
            
def main():
    args = sys.argv 
    if len(args) == 1:
        start()
    else:
        try:
            keyword_handler(args)
            
        except Exception as ex:
            print(colored("\n---------------------------------------", "red", attrs=["bold"]))
            print(colored("  !! Something went wrong !! ", "red", attrs=["bold"]), end = "\n\n")
            print(colored("  Exception: ", "white", attrs=["bold"]), end = "")
            print(colored(f"{ex} ", "white"))
            print(colored("---------------------------------------\n", "red", attrs=["bold"]))
                

                
                
if __name__ == "__main__":
    main()


