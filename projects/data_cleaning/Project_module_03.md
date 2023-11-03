## Module 3: Installable package and pytest

In the last module, you introduced modules, classes and a new notebook in you repo. In this module, you will add tests to your code base. But first, you will make your package installable.

- Create new branch "package-test" (Make sure changes from last module have been merged, and that you start from the main branch)
- Make sure pytest and pytest-cov are installed
- 3.1 Installable package
    - Organize the files into folders and add `setup.py`. Call your package `tscleaner`.
        - subfolders: tscleaner, scripts, notebooks, tests
        - make an init-file `__init__.py` in the tscleaner folder with the following content: 
            ```python
            from .cleaning import SpikeCleaner, FlatPeriodCleaner, OutOfRangeCleaner
            from .plotting import plot_timeseries
            ```
        - create a `setup.py` in the root with the following content (change with your data):
            ```python
            from setuptools import setup, find_packages
            setup(
                name='MyPackageName',  
                version='0.0.1',  
                url='https://github.com/mypackage.git',  
                author='Author Name',  
                author_email='author@gmail.com',  
                description='Description of my package',  
                packages=find_packages(),  
                install_requires=['numpy', 'matplotlib'],  
            )  
            ```
    - Install the package in editable mode, by running the below command from the project root.
        - `> pip install -e .`
    - Modify import statements in `notebook_A` and script `main.py` and make sure they run.
    - Modify the cleaner tools by raising exceptions for invalid inputs.
    - Move the csv file to `/tests/testdata` and update notebook with relative path to the file
- 3.2 Pytest
    - Write unit tests with pytest in the `/tests` folder. Create an empty `__init__.py` file in the folder. Create a file `test_cleaning.py` and create at least three tests that verify that the cleaning tools work as intended
    - [Optional] Consider to make a fixture that reads the csv file and you can read in all tests
    - Run the tests from the commandline by writting `>pytest` in the project root (can you also run the tests from VSCode?)
    - Assess the test coverage with `>pytest --cov=tscleaner tests`
    - [Optional] Get coverage as html with `>pytest --cov=tscleaner --cov-report html` (check the index.html in the htmlcov subfolder afterwards)
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)

{{< include _footer.md >}}