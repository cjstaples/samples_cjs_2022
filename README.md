# samples_cjs_2022
A place for code samples / 2022

Setup:
    create / activate virtual environment and load dependencies from requirements.txt
    e.g.    python -m venv venv_sample
            venv_sample\Scripts\activate (Windows) or
            source ./venv_sample/bin/activate (Unix/MacOS)
            pip install -r requirements.txt

Execution:
    each script will run a sanity test out of main() and produce output to match the relevant question
    e.g.    python fn_anagrams.py
    or
    run the pytest included to check all scripts
    e.g.    pytest -collect-only                # list all tests
            pytest -v                           # run all tests, verbose output
