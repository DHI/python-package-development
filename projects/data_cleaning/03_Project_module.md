---
title: "Module 3: Installable package and pytest"
---

In the last module, you introduced modules, classes and a new notebook in you repo. In this module, you will add tests to your code base. But first, you will make your package installable.

- Create new branch "package-test" (Make sure changes from last module have been merged, and that you start from the main branch)
- 3.1 Installable package
    - Organize the files into folders and add an empty `pyproject.toml`. Call your package `tscleaner`.
        - subfolders: `src/tscleaner`, `scripts`, `notebooks`, `tests`
        - make an init-file `__init__.py` in the src/tscleaner folder with the following content: 

    ```python
    from .cleaning import SpikeCleaner, FlatPeriodCleaner, OutOfRangeCleaner
    from .plotting import plot_timeseries
    ```

    *Project structure*:

    ```
    ├── notebooks/
    ├── scripts/
    ├── src/
    │   └── tscleaner/
    │       └── __init__.py
    ├── tests/
    └── pyproject.toml
    ```

    - edit the `pyproject.toml` in the root with the following content (change with your data):

    ```toml
    [project]
    name = "tscleaner"
    version = "0.1.0"
    description = "Add your description here"
    authors = [
        { name = "Mike Water", email = "xyz@dhigroup.com" }
    ]
    requires-python = ">=3.13"
    dependencies = [
        "matplotlib",
        "numpy",
    ]

    [dependency-groups]
    dev = ["pytest", "pytest-cov"]

    [tool.pytest.ini_options]
    pythonpath = ["src"]
    ```

    - Modify import statements in `notebook_A` and script `main.py` and make sure they run.
    - Modify the cleaner tools by raising exceptions for invalid inputs.
    - Move the csv file to `/tests/testdata` and update notebook with relative path to the file
- 3.2 Pytest
    - Write unit tests with pytest in the `/tests` folder. Create an empty `__init__.py` file in the folder. Create a file `test_cleaning.py` and create at least three tests that verify that the cleaning tools work as intended
    - If all your tests are failing, consider if you have given the right requirements in the `pyproject.toml`... 
    - [Optional] Consider to make a fixture that reads the csv file and you can read in all tests
    - Run the tests from the commandline by writting `> uv run pytest` in the project root (can you also run the tests from VSCode?)
    - Assess the test coverage with `> uv run pytest --cov=tscleaner tests`
    - [Optional] Get coverage as html with `> uv run pytest --cov=tscleaner --cov-report html` (check the index.html in the htmlcov subfolder afterwards)
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)

{{< include _footer.md >}}