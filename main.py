import os
from extractzip import extract_to_zip_directory, extract_to_current_directory
from countfiles import countfilesAndCompareWithSignature


def resolve_zip_path():
    """
    Determines the correct ZIP path depending on whether the script
    is running locally (Windows) or inside Docker (/data).
    """

    docker_path = "/data/MockAssayInstaller.zip"
    local_path = r"C:\Users\anagh\OneDrive\Desktop\GetInterviewAtTheBig4\BuildingToolsForQAAutomation\AssayInstaller\MockAssayInstaller.zip"

    if os.path.exists(docker_path):
        print(f"Running inside Docker. Using ZIP at: {docker_path}")
        return docker_path

    if os.path.exists(local_path):
        print(f"Running locally. Using ZIP at: {local_path}")
        return local_path

    raise FileNotFoundError(
        f"Neither ZIP file exists:\n - {docker_path}\n - {local_path}"
    )


def main():
    try:
        zip_path = resolve_zip_path()

        # Extract only ONCE — into the ZIP's directory
        extract_to_zip_directory(zip_path)

        # Run your signature + file count validation
        countfilesAndCompareWithSignature()

        print("\nProcess completed successfully.")
        print("Editing this file to create a seperate pull request and testing GitHub actions")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")


if __name__ == "__main__":
    main()
