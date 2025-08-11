# Django Bootstrapper

Questions asked in the steps:
- [x] Give your project a name. (No default)
- [x] Enter a slug for your project. (Slugify name of project)
- [x] Do you want me to install Django-Tailwind? (Yes)
## TODO
- [ ] Do you want me to setup auth? (Yes)
- [ ] Do you want me to setup celery? (No)
- [ ] Provide a Github repo name (optional) (E.g. KavyanshKhaitan2/django-bootstrapper) *Requires git in path to be connected to remote

# How to run while development
- 1. (optional) Go to `main.py` and set `DEV = True` for easier development.
- 2. Run `uv run main.py` to start testing.
- 3. Make changes to the code.
- 4. Run `rm -r project-slug/` to clean the slate and go to step 2 to continue dev or step 5 when completed dev.
- 5. Go to `main.py` and set `DEV = False` so you feel good about it.