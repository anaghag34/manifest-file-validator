import glob
import os

def countfilesAndCompareWithSignature():
    count_signatures = 0

    # Detect Docker vs Local
    base_path = "/data/MockAssayInstaller"
    local_base = r"C:\Users\anagh\OneDrive\Desktop\GetInterviewAtTheBig4\BuildingToolsForQAAutomation\AssayInstaller\MockAssayInstaller"

    if os.path.exists(base_path):
        root = base_path
    else:
        root = local_base

    folder1 = os.path.join(root)
    folder2 = os.path.join(root, "Assay Packages")
    folder3 = os.path.join(root, "de")

    Counter1 = len(glob.glob(os.path.join(folder1, "*.dll")))
    Counter2 = len(glob.glob(os.path.join(folder2, "*.zip")))
    Counter3 = len(glob.glob(os.path.join(folder3, "*.dll")))

    total = Counter1 + Counter2 + Counter3
    print(total)

    manifest_path_docker = "/data/manifest.xml"
    manifest_path_local = r"C:\Users\anagh\OneDrive\Desktop\GetInterviewAtTheBig4\BuildingToolsForQAAutomation\pythonscripts\MockAssayInstaller\manifest.xml"

    manifest_path = manifest_path_docker if os.path.exists(manifest_path_docker) else manifest_path_local

    with open(manifest_path, "r") as manifest:
        for line in manifest:
            if "sha256" in line:
                count_signatures += 1

    if count_signatures == total:
        print("Every single file has a signature present in manifest")
    else:
        print("Not all files are encrypted")
