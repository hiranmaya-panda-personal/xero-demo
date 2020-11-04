# xero-demo
## Section 1 - Environment setup - macOS using zsh
1. Download & install binary from python.org
2. Installed path is by default /usr/local/bin
3. Open the terminal & execute the virtual environment creation command - ```python3.9 -m venv ~/venvs/<INSERT FOLDER NAME>```.
4. Activate virtual environment via: ```cd ~/venvs/<FOLDER NAME>/bin``` and then execute ```source activate```.
5. Install selenium package while the venev is active by executing ```pip3 install selenium``` in the terminal.
6. To check packages/dependencies installed, execute ```pip list``` while the virtual environment is active.
7. Download ChromeDriver(chromedriver) from chromium.org and place it under ```~/Projects/drivers``` (you can use any name - this is just an example)
8. Add the drivers to the PATH in macOS by adding the folder path in .zshrc file: ```nano ~/.zshrc```,add this line ```PATH=$PATH:/Users/<INSERT USERNAME>/Projects/drivers```, control + O, control + Z, ```source ~/.zshrc```.
9. Ensure that the drivers and browsers are compatible with each other.

## Section 2 - Running the tests 
1. Ensure that the venv is up & running.
2. Download the files in this repo in a single folder(do not scatter the files across different folder hierachies).
3. Using the terminal - navigate to the folder containing these .py files.
4. Execute - ```python runtests.py``` in terminal.

## Important note - some limitations
* Ensure that the default organisation(i.e, the organisation that you located in after a successful log in, is **Trial Run**) before running the tests.
* If you want to rerun the test cases multiple times, you'll need to specify a unique value of the the ```self.dummy_account_name``` variable under the *bankpage.py* file.
