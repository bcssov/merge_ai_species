import shutil
import os
from templates import get_modules
from templates.utils import locales

copy_directories = ["common", "events", "gfx", "interface", "localisation"]
copy_files = ["Readme.txt", "descriptor.mod",
              "thumbnail.png", "1.jpg", "2.jpg", "3.jpg"]

mode_name = "merge_ai_species"
destination = "publish/" + mode_name


def copy():
    for directory in copy_directories:
        if os.path.exists(directory):
            shutil.copytree(directory, destination + "/" + directory)

    for file in copy_files:
        if os.path.exists(file):
            shutil.copy(file, destination + "/" + file)


def clean_up():
    if os.path.exists(destination):
        shutil.rmtree(destination)


def process_templates():
    for module in get_modules():
        module.process(destination)


if __name__ == "__main__":
    clean_up()
    copy()
    process_templates()
    locales.process_locales(destination)
