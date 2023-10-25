# Course project: Time Series Data Cleaning

## Module 1: GitHub and basic functions

- 1.1 GitHub repo
    - 1.1.1 Create a new GitHub repository "timeseriescleaner"
        - private, no template, add readme, gitignore python, no license
    - 1.1.2 Go to repo settings/Collaborators add your instructors and your "buddy"
    - 1.1.3 Clone repo to local machine
    - [Optional] Create virtual environment for this course project (use venv or mamba/conda environment)
    - 1.1.4 Download the provided Python script and add it to the repo
    - 1.1.5 Commit the file and push the changes (Check that the file can be found on GitHub)
    - 1.1.6 Open the project in vscode and make a single character change to the file (add a comment)
    - 1.1.7 Commit the changes (Check that it works on GitHub)
- 1.2 Functions
    - 1.2.1 Create a local branch "refactor-functions"
    - 1.2.2 Refactor the code to use functions (`clean_spikes`, `clean_outofrange`, `clean_flat`, `plot_timeseries`)        
        - for data in [data1, data2, data3]:
            - data_original = data.copy()
            - data = clean_spikes(data, max_jump=10)
            - data = clean_outofrange(data, min_val=0, max_val=50)
            - data = clean_flat(data, flat_period=5)
            - plot_timeseries(data_original, data)
    - 1.2.3 Check that your code and produce the same results as before (you should not change the functionality!)
    - 1.2.4 Commit your code in 1 or more commits (in the end your code should be approximately 75 lines long)
- Create a pull request in GitHub and "request review" from your reviewers
- Wait for feedback, Adjust code until approval, then merge (and delete branch)


## Module 2: Modules and classes

- Create new branch "modules-classes" (Make sure changes from last module have been merged, and that you start from the main branch)
- 2.1 Function arguments
    - Add default arguments to the functions. Commit.
    - Make sure that you only use positional arguments where there is only one argument. Use keyword arguments everywhere else. Commit.
- 2.2 Modules
    - Move cleaner functions into a separate module "cleaning.py". Commit.
    - Move the plotting function into a separate module "plotting.py". Commit.
    - Rename the script `main.py` and execute the cleaning and plotting.
        - from cleaning import ...
        - from plotting import ...
        - Check that it runs!
- 2.3 Classes
    - Organize the cleaning functions into classes that all have the same structure (an init method and a clean method)
        - SpikeCleaner
            - init(max_jump)
            - clean(data)
        - modify `main.py` and check that it runs
            - cleaners = [
            -   SpikeCleaner(max_jump=10),
            -   OutOfRangeCleaner(min_val=0, max_val=50),
            -   FlatPeriodCleaner(flat_period=5),
            - ]
            - for cleaner in cleaners:
            - data = cleaner.clean(data)
    - Download notebook_A and csv file and make sure it runs. (remove any remaining print statements)
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)



## Module 3: Installable package and pytest

- Create new branch "package-test" (Make sure changes from last module have been merged, and that you start from the main branch)
- Make sure pytest and pytest-cov are installed
- 3.1 Installable package
    - 4.1 Organize the files into folders and add setup.py. Call your package tscleaner.
        - subfolders: tscleaner, scripts, notebooks, tests
        - make init-file in tscleaner with
            - `from .cleaning import SpikeCleaner, FlatPeriodCleaner, OutOfRangeCleaner`
            - `from .plotting import plot_timeseries`
        - create a setup.py in the root with the following content (change with your data):
            - from setuptools import setup, find_packages
            - setup(
                name='MyPackageName',  
                version='0.0.1',  
                url='https://github.com/mypackage.git',  
                author='Author Name',  
                author_email='author@gmail.com',  
                description='Description of my package',  
                packages=find_packages(),  
                install_requires=['numpy', 'matplotlib'],  
                )  
    - 4.2 Install the package in editable mode.
        - `>pip install -e .`
    - 4.3 Modify import statements in notebook_A and script main.py and make sure they run.
    - 4.4 Modify cleaner tools by raising exceptions for invalid inputs.
    - 4.5 Move the csv file to `/tests/testdata` and update notebook with relative path to the file
- 3.2 Pytest
    - 4.2.1 Write unit tests with pytest in the `/tests` folder. Create an empty init-py file in the folder. Create a file `test_cleaning.py` and create at least five tests that verify that the cleaning tools work as intended
    - [Optional] Consider to make a fixture that reads the csv file and you can read in all tests
    - 4.2.2 Run the tests from the commandline by writting `>pytest` in the project root (can you also run the tests from VSCode?)
    - 4.2.3 Assess the test coverage with `>pytest --cov=tscleaner tests`
    - Optional: Get coverage as html with `>pytest --cov=tscleaner --cov-report html` (check the index.html in the htmlcov subfolder afterwards)
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)


## Module 4: GitHub actions and auto-formatting

- Create new branch "action-formatting" (Make sure changes from last module have been merged, and that you start from the main branch)
- 4.1 Github Action
    - 5.1.1 Copy the GitHub action "python-app.yml" from the python template https://github.com/DHI/template-python-library to your own library (make sure it sits in the same folder).
    - 5.1.2 Change all occurrences of "my_library" in the yml file to your package name "tscleaner"
    - 5.1.3 Comment out the line with "ruff-action" with "#"
    - 5.1.4 Commit, push and create a pull request; the tests should now run, verify that they all run before you move on
- 4.2 Ruff
    - 5.2.1 Enable the "ruff-action" be removing the "#" you added above
    - 5.2.2 Commit and push, your actions will probably fail now - inspect the problems by clicking the red cross (did you also get an email?)
    - 5.2.3 Install "ruff" on your local machine with mamba/conda/pip
    - 5.2.4 Navigate to your project root folder and run ruff with "ruff ."
    - 5.2.5 Add `__all__ = ["SpikeCleaner", "FlatPeriodCleaner", "OutOfRangeCleaner", "plot_timeseries"]` to your `__init__.py` file and fix remaining issues until ruff passes
    - 5.2.6 Commit, push and verify that you action now succeeds
- 4.3 Black
    - 5.3.1 Install "black" on your local machine with mamba/conda/pip
    - 5.3.2 Run black from your project root folder; inspect the differences; commit
- 4.4 pyproject.toml
    - Copy the pyproject.toml from the python template https://github.com/DHI/template-python-library (this file will replace your setup.py)
    - Modify to fit your package
    - Remove the setup.py
    - Commit, push and verify that the GitHub action runs
    - If it fails, you probably forgot some dependencies - go back and fix
    - [Optional] You should also re-install your local package with ">pip install --upgrade -e ."
- 4.5 [Optional] Enable black and ruff extensions in VSCode; set black to run on save
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)


## Module 5: Object-oriented design

- Create new branch "oop-dataclasses" (Make sure changes from last module have been merged, and that you start from the main branch)
- 5.1 Type Hints
    - Add type hints to all functions and methods. Commit
- 5.2 Data class
    - Make all the cleaner classes dataclasses.    
    - remove the init method (not needed anymore)
    - Check that the notebook still runs and that the classes indeed work as data classes (e.g. have a string representation and support equality testing etc)
    - Commit
- 5.3 Module level function
    - Make a private module function _print_stats() that prints the number of cleaned values
    - call from each of the clean methods
- 5.4 Composition or inheritance
    - Create a new cleaner class called CleanerWorkflow that takes a list of cleaners when constructed and has a clean method that run all the cleaners' clean methods. 
    - Modify the notebook to use the CleanerWorkflow instead of looping over the cleaners
    - Consider what type of validation you would want CleanerWorkflow
    - Consider whether it would be better to create a base class BaseCleaner - write down your considerations as a comment in the pull request, refer to specific lines of code
        - e.g. how would you handle e.g. common plotting functionality in the cleaner classes? 
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)



## Module 6: Documentation

- Create new branch "docs" (Make sure changes from last module have been merged, and that you start from the main branch)
- 6.1 README
    - Write a README file with basic information about the project.
- 6.2 Docstrings
    - Write NumPy style docstrings for all functions and classes.
    - [Optional] Install the autodocstrings extension in VSCode (set the style to NumPy)
- 6.3 mkdocs
    - Install mkdocs, mkdocstrings and material design `mamba/pip install mkdocstrings-python mkdocs-material`
    - Create a `mkdocs.yml` file (copy from https://github.com/DHI/template-python-library and adapt).
    - Create a docs folder and create a markdown file `index.md` inside.
    - Create API documentation locally using `>mkdocs serve`.
    - Check the generated HTML documentation.
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)


##  Module 7: Publishing
- Add a license
- Change version number to 0.1.0
- Build the package with hatchling.
- Publish the package to the PyPI Test Server.
