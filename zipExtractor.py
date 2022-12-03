import pathlib
import zipfile


def archive_extractor(file, folder):
    with zipfile.ZipFile(file, "r") as archive:
        archive.extractall(folder)
