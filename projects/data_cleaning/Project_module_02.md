## Module 2: Modules and classes

After last module, your script now uses functions `clean_spikes`, `clean_outofrange`, `clean_flat`, `plot_timeseries` and has a nice home on GitHub. In this module, you will improve the functions, move them to separate modules and then refactor your code to use classes. Finally, you will check that it all works by running a notebook.  

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
            - `def __init__(max_jump)`
            - `def clean(data)`
        - modify `main.py` and check that it runs
            - cleaners = [
            -   SpikeCleaner(max_jump=10),
            -   OutOfRangeCleaner(min_val=0, max_val=50),
            -   FlatPeriodCleaner(flat_period=5),
            - ]
            - for cleaner in cleaners:
            -   data = cleaner.clean(data)
    - Download [`notebook_A.ipynb`](notebook_A.ipynb) and csv file `example_data1.csv` and make sure it runs. (remove any remaining print statements)
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)

{{< include _footer.md >}}