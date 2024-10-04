## Module 4: GitHub actions and auto-formatting

Your package is now installable and testable. In this module, you will make the tests automatic in GitHub and make sure that your code style adhere to the standards in PEP-8. 

In this module, we will use some files from the python library template. When you, after this course, need to create a new package, you can simply start from this template when creating the repo. 

- Create new branch "action-formatting" (Make sure changes from last module have been merged, and that you start from the main branch)
- 4.1 Github Action
    - Copy the GitHub action file `full_test.yml` (in the `.github/workflows` folder) from the python template https://github.com/DHI/template-python-library to your own library (make sure it sits in the same folder).
    - Change all occurrences of "my_library" in the yml file to your package name "tscleaner"
    - Comment out the line with "ruff-action" with "#"
    - Commit, push and create a pull request; the tests should now run, verify that they all run before you move on
- 4.2 Linting with ruff
    - Enable the "ruff-action" be removing the "#" you added above
    - Commit and push; your actions will probably fail now - inspect the problems by clicking the red cross (did you also get an email?)
    - Install "ruff" on your local machine with mamba/conda/pip
    - Navigate to your project root folder and run ruff with "ruff check"
    - Add the following line to your `__init__.py` file 
        `__all__ = ["SpikeCleaner", "FlatPeriodCleaner", "OutOfRangeCleaner", "plot_timeseries"]` 
    - fix remaining issues until ruff passes
    - Commit, push and verify that you action now succeeds
- 4.3 Formatting with ruff
    - Run "ruff format" from your project root folder; inspect the differences; commit
- 4.4 pyproject.toml
    - Copy the `pyproject.toml` from the python template https://github.com/DHI/template-python-library (this file should replace your `setup.py`)
    - Modify the file contentes to fit your package
    - Remove the `setup.py` file
    - Commit, push and verify that the GitHub action runs
    - If it fails, you probably forgot some dependencies - go back and fix
    - [Optional] You should also re-install your local package with `>pip install --upgrade -e .`
- 4.5 [Optional] Enable ruff extensions in VSCode; set ruff format to run on save
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)

{{< include _footer.md >}}