import sys
import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == '__main__':
    extract_archive("/Users/simoncarrier/Documents/python/todo/bonus/files/compressed.zip",
                    "/Users/simoncarrier/Documents/python/todo/bonus/files")