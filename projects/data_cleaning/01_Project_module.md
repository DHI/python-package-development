---
title: "Module 1: GitHub and basic functions"
---

Let's get started on the project! You have received the script [`clean_project_data_v4_final2.py`](clean_project_data_v4_final2.py) from a colleague and in this module you will create a GitHub repository, add the script and improve the script by using functions. 

- 1.1 GitHub repo
    - Create a new GitHub repository "timeseriescleaner" on your own GitHub profile (not on your organization's GitHub)
        - Make it private, no template, add readme, gitignore python, no license
    - Go to repo settings/Collaborators add your instructors and your "buddy"
    - Clone repo to local machine
    - Create a virtual environment for this course project (use `uv venv`)
    - Download the provided Python script and add it to the repo
    - Commit the file and push the changes (Check that the file can be found on GitHub)
    - Open the project in vscode and make a single character change to the file (add a comment)
    - Commit and push the changes (Check that you can find it on GitHub)
- 1.2 Functions
    - Create a local branch "refactor-functions"
    - Refactor the code to use functions (`clean_spikes`, `clean_outofrange`, `clean_flat`, `plot_timeseries`) 
    - You should be able to run the cleaning using this loop:       
```python
for data in [data1, data2, data3]:
    data_original = data.copy()
    data = clean_spikes(data, max_jump=10)
    data = clean_outofrange(data, min_val=0, max_val=50)
    data = clean_flat(data, flat_period=5)
    plot_timeseries(data_original, data)
```
    - Check that your code runs and produce the same results as before (you should not change the functionality when refactoring!)
    - Commit your code in one or more commits (in the end, your code should be approximately 75 lines long)
- Create a pull request in GitHub and "request review" from your reviewers
- Wait for feedback, Adjust code until approval, then merge (and delete branch)

{{< include _footer.md >}}