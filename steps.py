import os
import subprocess
import shutil
from pathlib import Path
from utils import BootstrapperPreferences
from utils import show_progress, show_step_complete, show_complete
from utils import HOURGLASS, GREEN_TICK
import colorama

# Run 'python manage.py tailwind dev' to start server for dev.

TOTAL_PROGRESS_ITEMS = 10

progress = 0


def proceed(preferences: BootstrapperPreferences):
    print("Proceeding with project initialisation...")
    create_directory(preferences)  # Step 1
    init_django_project(preferences)  # Step 2
    init_uv(preferences)  # Step 3
    setup_tailwind_css(preferences)  # Step 4


def create_directory(preferences: BootstrapperPreferences):
    global progress
    progress += 1
    show_progress("Creating project directory...", progress, TOTAL_PROGRESS_ITEMS)
    os.mkdir(Path(os.getcwd()) / preferences.project_slug)
    show_step_complete()


def init_django_project(preferences: BootstrapperPreferences):
    global progress
    progress += 1
    show_progress("Initialising Django project...", progress, TOTAL_PROGRESS_ITEMS)
    subprocess.run(
        ["django-admin", "startproject", "mysite", preferences.project_slug],
        capture_output=True,
        text=True,
    )
    os.chdir(Path(os.getcwd()) / preferences.project_slug)
    show_step_complete()


def init_uv(preferences: BootstrapperPreferences):
    global progress
    progress += 1
    show_progress("Initialising UV package manager...", progress, TOTAL_PROGRESS_ITEMS)
    subprocess.run(
        ["uv", "init"],
        capture_output=True,
        text=True,
    )
    subprocess.run(
        ["uv", "add", "django"],
        capture_output=True,
        text=True,
    )
    os.remove("main.py")
    show_step_complete()


def setup_tailwind_css(preferences: BootstrapperPreferences):
    global progress
    progress += 1
    show_progress(
        "Setting up Django-Tailwind (+ Browser Reload for DEBUG)...",
        progress,
        TOTAL_PROGRESS_ITEMS,
    )
    subprocess.run(
        ["uv", "add", "django-tailwind[reload]", "cookiecutter"],
        capture_output=True,
        text=True,
    )
    os.remove("mysite/settings.py")
    shutil.copy(
        Path(__file__).parent / "assets/step4_1_settings.py",
        Path(os.getcwd()) / "mysite/settings.py",
    )
    subprocess.run(
        ["uv", "run", "manage.py", "tailwind", "init", "--no-input", "--app-name=tailwindcsstheme"],
        capture_output=True,
        text=True,
    )
    os.remove("mysite/settings.py")
    shutil.copy(
        Path(__file__).parent / "assets/step4_2_settings.py",
        Path(os.getcwd()) / "mysite/settings.py",
    )
    os.remove("mysite/urls.py")
    shutil.copy(
        Path(__file__).parent / "assets/step4_3_urls.py",
        Path(os.getcwd()) / "mysite/urls.py",
    )
    show_progress(
        "SUBPART: Started TailwindCSS installation (requires js, so more patience)...",
        progress,
        TOTAL_PROGRESS_ITEMS,
    )
    subprocess.run(
        ["uv", "run", "manage.py", "tailwind", "install"],
        capture_output=True,
        text=True,
    )
    show_step_complete()
