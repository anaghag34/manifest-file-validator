**QA Automation Tools: Assay Installer Validator**

A Python-based utility tool built for QA automation pipelines. This tool automates the process of extracting assay deployment packages, parsing XML installation manifests, counting target deployment files (.dll, .zip), and verifying their cryptographic signatures (sha256) to ensure package integrity.

It is designed to run seamlessly both locally (Windows) and containerized within Docker environments.

**Features**

Smart Path Resolution: Automatically detects whether it is running inside a Linux Docker container (/data) or a local Windows environment.

Safe Extraction: Safely extracts .zip packages dynamically using standard libraries.

Integrity Validation: Parses manifest.xml and performs automated file-to-signature counting across specific localization and deployment subdirectories (Assay Packages, de).

**Project structure**

├── data/
│   ├── MockAssayInstaller.zip   # Sample deployment package
├── extractzip.py                # Zip extraction logic
├── countfiles.py                # File counting and signature validation logic
├── main.py                      # Application entry point & environment detection
├── Dockerfile                   # Docker container configuration
└── requirements.txt             # Project dependencies 

**Prerequisites**
Python 3.11+

Docker (Optional, for containerized execution)

**What is covered:**
Environment Detection: Assures the script correctly chooses Docker paths over local paths when both or either exist.

Zip Extraction: Uses transient virtual folders to verify real zip files unzip correctly.

Signature Alignment: Simulates both matching and mismatching validation counts between mocked directories and manifest configurations.
