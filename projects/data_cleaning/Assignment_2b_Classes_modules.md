### Module 2B Assignment: Implement Classes and Modules

#### Objective:
Build upon the code from the previous module to encapsulate the data cleaning logic within classes. Furthermore, split the code into separate modules to enhance the organization and modularity of your code. 

#### Detailed Instructions:

1. **Create Classes for Data Cleaning:**

    - **TimeSeriesData:**
        - Create a class that encapsulates the time series data.
        - Include methods for each data cleaning operation (range cleaning, jump checking, and checking for flat periods).
        - Ensure the class can accept a pandas Series and store both the original and cleaned data.

    - **DataVisualizer:**
        - Create another class dedicated to data visualization.
        - Include a method to plot both the original and cleaned data in one graph.

2. **Split Code into Modules:**

    - Create separate Python files for each class and use import statements to organize your code.
        - `time_series_data.py`: Contains the `TimeSeriesData` class.
        - `data_visualizer.py`: Contains the `DataVisualizer` class.
        - `main.py`: Contains the code to execute the cleaning and visualization processes.

3. **Implement and Test Classes:**

    - Instantiate the `TimeSeriesData` class, perform the cleaning, and store the cleaned data.
    - Instantiate the `DataVisualizer` class and pass the cleaned data to it for visualization.

4. **Push Changes to GitHub:**

    - Commit your changes and push them to your GitHub repository.
    - Ensure the new Python files and any updated scripts are added.

5. **Open Pull Request:**

    - Create a pull request and detail the changes made, ensuring to highlight the introduction of classes and modules.

#### Submission Process:

1. **Pull Request:**
    - Your submission will be through the pull request.
    - Include a description that explains your implementation, the classes created, and methods within those classes.

2. **Code Review:**
    - Participate in the code review process, review the code of peers, and implement the received feedback.

#### Evaluation Criteria:

- **Implementation of Classes (40%):** Effective use of classes to encapsulate data cleaning and visualization logic.
- **Code Modularity (30%):** Successful splitting of code into separate modules and appropriate use of import statements.
- **Code Quality (20%):** Clean, readable, and well-documented code with appropriate comments.
- **GitHub Workflow (10%):** Proper use of commits, push, and pull requests, including a clear and descriptive pull request.

#### Example Structure:

1. **TimeSeriesData Class:**
    - Methods for data cleaning.
    - Attributes to store the original and cleaned data.

2. **DataVisualizer Class:**
    - Method to plot data.
    - Accepts data from a `TimeSeriesData` object.

3. **Modules:**
    - Organize these classes into separate Python files and import them as needed.

#### Deadline:
- The pull request should be opened by [specific date and time], and peers should complete reviews by [review deadline].

Use this opportunity to practice object-oriented programming and enhance the structure of your code to be more modular and organized. Happy coding!