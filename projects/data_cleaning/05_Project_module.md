---
title: "Module 5: Object-oriented design"
---

In this module you will benefit from the automatic testing that you have added in the last module. Let's explore some other object-oriented designs for our code base... 

- Create new branch "oop-dataclasses" (Make sure changes from last module have been merged, and that you start from the main branch)
- 5.1 Type Hints
    - Uncomment out the line with `- name: Static type check` in your github actions workflow. 
    - Add type hints to all functions and methods. Commit
- 5.2 Data class
    - Make all the cleaner classes dataclasses.
    ```python
    from dataclasses import dataclass

    @dataclass
    class SpikeCleaner:
        ...
    ```
    - remove the `__init__` method (not needed anymore)
    - Check that the notebook still runs and that the classes indeed work as data classes (e.g. have a string representation and support equality testing etc)
    - Commit
    

- 5.3 Module level function
    - Make a private module function `_print_stats()` that prints the number of cleaned values
    - call the function from each of the clean methods (note: inheritance is not required to obtain common functionality)
- 5.4 Composition or inheritance
    - Create a new cleaner class called CleanerWorkflow that takes a list of cleaners when constructed and has a clean method that run all the cleaners' clean methods. 
    ```python
    class CleanerWorkflow:
        def __init__(self, cleaners) -> None:
            self.cleaners = cleaners

        def clean(self, data: pd.Series) -> pd.Series:
            data_cleaned = data.copy()
            for cleaner in self.cleaners:
            ...
    ```
    - Modify the notebook to use the CleanerWorkflow instead of looping over the cleaners
    - Consider what type of validation you would want CleanerWorkflow to have? Is it better check validity up front or to just go ahead and handle problems afterwards? 
    - Consider whether it would be better to create a base class BaseCleaner - write down your considerations as a comment in the pull request, refer to specific lines of code
    - e.g. how would you handle e.g. common plotting functionality in the cleaner classes? 
    - Create pull request in GitHub and "request review" from your reviewers
    - Get feedback, Adjust code until approval, then merge (and delete branch)

    



{{< include _footer.md >}}