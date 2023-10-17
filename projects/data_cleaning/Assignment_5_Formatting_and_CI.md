### Assignment 5: Formatting and GitHub Actions

In this module, you'll focus on improving the readability of your code by utilizing code formatters. You'll also automate the testing and code formatting processes using GitHub Actions, ensuring that your code is consistently clean and that tests are passing with every change made.

#### Tasks

**5.1 Install the Code Formatters**

- Use pip to install the 'black' and 'ruff' code formatters. These tools will help ensure that your code adheres to Python's PEP 8 standards and is consistently clean and readable.

**5.2 Format Code with Black**

- Run 'black' on your entire Python codebase. Check all the files to ensure they are well-formatted and adheres to PEP 8 standards.

**5.3 Identify and Fix Issues with Ruff**

- Utilize 'ruff' to identify any remaining or intricate code issues that 'black' might not handle. Make the necessary adjustments to your code to resolve these issues.

**5.4 Develop a GitHub Actions Workflow**

- In the `.github/workflows` directory of your repository, create a new file for defining your GitHub Actions workflow, such as `ci.yml`.
- Set up the workflow to install the project dependencies, run tests, and apply 'black' and 'ruff' on every push or pull request to ensure consistent code quality and that all tests are passing.

**5.5 Confirm Successful Workflow Execution**

- After pushing your workflow file to GitHub, check the Actions tab on your repository’s GitHub page. Confirm that the workflow is triggered and executes successfully upon every push or pull request.
- Address any issues or errors that occur to ensure that the workflow reliably ensures code quality and passes all tests.

#### Deliverables:

- A GitHub commit showing that all code has been formatted using 'black'.
- Another commit showing fixes applied after running 'ruff' on the codebase.
- A `ci.yml` file within the `.github/workflows` directory, containing the defined GitHub Actions workflow for automated testing and formatting.
- A successful execution log of the GitHub Actions workflow, visible in the Actions tab of your GitHub repository.

Ensure that your code is clean, well-commented, and consistently formatted. The automated workflow should help maintain code quality as the project progresses.