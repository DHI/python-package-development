## Module 5: Documentation

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