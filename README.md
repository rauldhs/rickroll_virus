# RickRoll GIF Virus

A script that spams multiple windows with Rickroll GIFs.

![rickroll virus running](https://github.com/rauldhs/rickroll_virus/blob/master/rickroll_virus_running.png)

## Installation

### Executable
1. Go to [releases](https://github.com/rauldhs/rickroll_virus/releases).
2. Download `rickroll.exe`.
3. Run it and enjoy the chaos! 🎉

### Python Script
1. Clone the repository and navigate to the script location.
2. Create a Python virtual environment:
    ```bash
    python -m venv rickroll_env
    ```
3. Activate the virtual environment:
    - **Windows:**
      ```bash
      .\rickroll_env\Scripts\activate
      ```
    - **macOS/Linux:**
      ```bash
      source rickroll_env/bin/activate
      ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the script:
    ```bash
    python rickroll.py
    ```
6. Enjoy the chaos! 🎉

### Building
1. Clone the repository as described in the **Python Script** section.
2. Navigate to the script location.
3. Install PyInstaller:
    ```bash
    pip install pyinstaller
    ```
4. Build the executable:
    ```bash
    pyinstaller --onefile --noconsole --icon="rickroll_icon.ico" --add-data "rickroll.gif;." --hidden-import=pillow --hidden-import=requests rickroll.py
    ```
