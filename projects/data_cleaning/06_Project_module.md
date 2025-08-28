---
title: "Module 6: Documentation"
---

Before, we share our code with others we should document it. This can be done in many ways, with docstrings (visable from the IDE), README file, notebooks, tests and a proper documentation site. 

- Create new branch "docs" (Make sure changes from last module have been merged, and that you start from the main branch)
- 6.1 README
    - Write a README file with basic information about the project.
- 6.2 Docstrings
    - Write NumPy style docstrings for all functions and classes (google it!)
    - [Optional] Install the autodocstrings extension in VSCode (set the style to NumPy), which helps you write docstrings fast by just writing three double quotes.
- 6.3 mkdocs
    - Install mkdocs, mkdocstrings and material design `mamba/pip install mkdocstrings-python mkdocs-material`
    - Create a `mkdocs.yml` file in the project root (copy from https://github.com/DHI/template-python-library and adapt).
    - Create a docs folder and create a markdown file `index.md` inside.
    - The index file can contain text in the markdown format and auto-generated documentation using the syntax: 
        - `::: tscleaner.SpikeCleaner`
    - Create API documentation locally using the command `>mkdocs serve` (which starts a local http server).
    - Check the generated HTML documentation.
    - The local documentation instance will "listen" to changes, try to modify the `index.md` file and watch.
- Create pull request in GitHub and "request review" from your reviewers
- Get feedback, Adjust code until approval, then merge (and delete branch)

{{< include _footer.md >}}