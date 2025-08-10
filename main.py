from slugify import slugify
import cutie
import colorama
from utils import text_input, BootstrapperPreferences
import steps

# Only enable it if you are trying to modify this project. This will enable
# almost all options and not let you configure your preferences.
DEV = False

def main():
    project_name = text_input("Give your project a name.")
    project_slug = text_input("Enter a slug for your project.", default=slugify(project_name))
    if project_slug != slugify(project_slug):
        old_slug = project_slug
        project_slug = slugify(project_slug)
        print(f"{old_slug} is not a valid slug. {project_slug} will be used instead.")
        if cutie.prompt_yes_or_no("Continue?", yes_text="Continue", no_text="Exit", default_is_yes=True, char_prompt=False):
            print(" └─ Yes")
            print("Sure.")
        else:
            print(" └─ No")
            print("Please re-start this script!")
            exit()
    install_django_tailwind = cutie.prompt_yes_or_no("Do you want me to install Django-Tailwind?", default_is_yes=True)
    print(" └─", "Yes" if install_django_tailwind else "No")
    print()
    setup_auth = cutie.prompt_yes_or_no("Do you want me to setup Django-Auth?")
    print(" └─", "Yes" if setup_auth else "No")
    print()
    github_remote = text_input("Provide a Github repo name (optional) (E.g. KavyanshKhaitan2/django-bootstrapper) *Requires git in path to be connected to remote", default="").strip()
    
    print("Preferences")
    print(f" ├─ Project Name:  {project_name}")
    print(f" ├─ Project Slug:  {project_slug}")
    print(f" ├─ Tailwind:      {"Yes" if install_django_tailwind else "No"}")
    print(f" ├─ Setup Auth:    {"Yes" if setup_auth else "No"}")
    print(f" ├─ Github Upload: {github_remote if github_remote else "[Disabled]"}")
    print( " ├────────────────────────────────────")
    cont = cutie.prompt_yes_or_no(" └─ Please confirm the preferences above.", yes_text="Continue", no_text="Exit", char_prompt=False)
    print()
    if not cont:
        print("Bye!")
        exit()
    steps.proceed(BootstrapperPreferences(
        project_name=project_name,
        project_slug=project_slug,
        tailwind=install_django_tailwind,
        auth=setup_auth,
        github_upload=github_remote
    ))




if __name__ == "__main__":
    print(" "+colorama.Back.GREEN, " ▄ ▘          ▄     ▗   ▗             ", colorama.Back.RESET)
    print(" "+colorama.Back.GREEN, " ▌▌▌▀▌▛▌▛▌▛▌▄▖▙▘▛▌▛▌▜▘▛▘▜▘▛▘▀▌▛▌▛▌█▌▛▘", colorama.Back.RESET)
    print(" "+colorama.Back.GREEN, " ▙▘▌█▌▌▌▙▌▙▌  ▙▘▙▌▙▌▐▖▄▌▐▖▌ █▌▙▌▙▌▙▖▌ ", colorama.Back.RESET)
    print(" "+colorama.Back.GREEN, "  ▙▌    ▄▌                    ▌ ▌     ", colorama.Back.RESET)
    print(                     "+------ With ❤️  by Kavyansh Khaitan -----+")
    print("Note: Run this in the parent dir of the project, not in the project dir itself.")
    print("UV also needs to be in path.")
    print()
    print()
    if not DEV:
        main()
    
    if DEV:
        pref = BootstrapperPreferences(
            project_name="Project Name",
            project_slug="project-slug",
            tailwind=True,
            auth=True,
            github_upload=""
        )
        print("Dev-mode enabled.")
        print(pref)
        print("Skipping to step: 'proceed'")
        steps.proceed(pref)