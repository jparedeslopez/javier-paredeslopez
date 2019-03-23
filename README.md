1. Create virtualenv with Python 3 and activate venv
2. Install Requirements from dependencies/requirements.txt
3. Modify configs/android.config with the right path for the .apk and device name.
4. Install the .apk and complete onboarding selecting Euro as currency and deafult accounts, dismiss the What's new dialogue.
5. Run 'python testsuite.py' in terminal



The two tests included in unitests.python verify the following:
- The number and name of the deafult Accounts are as expected. (Requirements can be found under /tests/testdata)
- The value of the accounts at fresh start of the app is "0"
