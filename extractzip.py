import os
import zipfile


def extract_to_zip_directory(zip_path):
    try:
        extract_path = os.path.dirname(zip_path)

        with zipfile.ZipFile(zip_path) as zip_ref:
            zip_ref.extractall(extract_path)

            print("Extracted to zip file directory:")
            print(extract_path)

            print("Extracted files:")
            for file in zip_ref.namelist():
                print(file)

    except Exception as e:
        print(f"An error occurred: {e}")


def extract_to_current_directory(zip_path):
    try:
        with zipfile.ZipFile(zip_path) as zip_ref:
            zip_ref.extractall()

            print("Extracted to current working directory:")
            print(os.getcwd())

            print("Extracted files:")
            for file in zip_ref.namelist():
                print(file)

    except Exception as e:
        print(f"An error occurred: {e}")


zip_path = r"C:\Users\anagh\OneDrive\Desktop\GetInterviewAtTheBig4\BuildingToolsForQAAutomation\AssayInstaller\MockAssayInstaller.zip"