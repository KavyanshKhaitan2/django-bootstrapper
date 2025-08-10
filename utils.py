from dataclasses import dataclass
import colorama

HOURGLASS = "[⏳]"
GREEN_TICK = "["+colorama.Fore.GREEN+"✔✔"+colorama.Fore.RESET+"]"

def text_input(text_for, prompt=" └─ ", default=None):
    print(text_for)
    inp = input(f"{prompt}{f"({default}) " if default else ""}")
    print()
    
    if inp.strip() == "":
        return default
    else:
        return inp

@dataclass
class BootstrapperPreferences:
    project_name: str
    project_slug: str
    tailwind: bool
    auth: bool
    github_upload: str

def show_progress(text:str, current_progress:int, total_progress:int):
    print(f"├─ {HOURGLASS} ({current_progress}/{total_progress}) {text}")

def show_step_complete():
    print(f"├─ {GREEN_TICK} Step Complete")
    

def show_complete(text:str):
    print(f"└─ {text}")