# Assignment 7: Publish Your Python Package

#### Objective
In this final assignment, you will be executing the real-world task of preparing, packaging, and distributing your Python project. We're going to use the Test PyPI server to safely practice this process without affecting the real PyPI repository.

#### Tasks:

### 1. **Prepare Your Package:**
   Ensure that all your codes are well-organized, functional, and thoroughly documented. 

   **Subtasks:**
   - Double-check all dependencies and ensure they are correctly listed in the `pyproject.toml`.
   - Confirm that your README file is up-to-date and contains all the necessary information.

### 2. **Package Your Project:**
   Package your project using `hatchling` and ensure it can be installed via `pip`.

   **Subtasks:**
   - Create a `pyproject.toml` file in the root folder of your project with the necessary configurations.
   - Build your package and ensure that it’s installable locally using `pip`.

### 3. **Publish to PyPI Test Server:**
   It's time to publish your package but to the Test PyPI server.

   **Subtasks:**
   - Test the installation process locally to ensure everything is functioning as expected.
   - Publish your package to the Test PyPI server and ensure it can be found and installed.

### 4. **GitHub:**
   Update your GitHub repository with the final version of the project.

   **Subtasks:**
   - Make sure all your final codes, documentation, and essential files are up-to-date.
   - Commit the final changes with a detailed summary of what the changes entail.

### Submission:

Your assignment will be considered complete when you successfully publish your package to the PyPI Test Server, and it should be accessible and installable. Ensure that the package is also updated on your GitHub repository. Share the links to your package on the Test PyPI and your GitHub repository for review.

#### Example:

**Preparing and Publishing to PyPI Test Server:**
```shell
# Building the package
hatchling build

# Installing the package locally to test
pip install .

# Publishing to PyPI test server
twine upload --repository testpypi dist/*
```

**Expected Outcome:**
Your package should be live on the Test PyPI server, and the updated code and documentation should be available on your GitHub repository. Make sure to test the installation process to confirm that users can successfully install the package using `pip` from the Test PyPI server. 

Please remember to adhere to all the best practices learned throughout this course in preparing, packaging, and distributing your Python project. Happy coding!