# Python package development

This repo contains slides used in the course "Python package development".
The course is run periodically and the material is kept up to date with current Python tooling.

## Python package standards

The whole course distilled into one page of rules — every rule has its own link, so you can
point someone at exactly the thing you mean.

**<https://dhi.github.io/python-package-development/standards.html>**

```
…/standards.html#mutable-default-arguments
…/standards.html#composition-over-inheritance
…/standards.html#libraries-loose-applications-pinned
```

Source: [`standards.md`](standards.md).

### Reviewing a package against the standards

[`.claude/skills/review-python-package/`](.claude/skills/review-python-package/) is a
[Claude Code](https://claude.com/claude-code) skill that audits a package repository against
these standards — layout, `pyproject.toml`, dependencies, tests, code smells, docs, CI and
release setup — and reports findings linked to the rule each one breaks.

Copy the folder into `~/.claude/skills/` (or your project's `.claude/skills/`), then:

```
> review this package against the DHI standards
```

## Course description

Python is the language of choice for data science, scientific computing and AI.

Are you ready to take your Python skills to the next level and develop your own Python package that can benefit your department, GBU, or all of DHI?

### Who should attend?

This course is ideal for those who have an idea for a Python package they want to develop, and who already have much of the code but need assistance in structuring, refactoring, and packaging it. Participants can apply individually or in small teams of 2-3 people.

### Content

The course comprises these seven modules: 

* Git, Pull Requests, and code reviews
* Python functions, classes, and modules
* Testing and auto-formatting
* Dependencies and Continuous Integration
* Object oriented design in Python
* Documentation
* Distributing your package


## Presentations:

<https://dhi.github.io/python-package-development>

*Made with [Quarto](https://quarto.org/) and hosted by [GitHub Pages](https://pages.github.com/)*

## Development

**Prerequisites:** Python 3.13, [Quarto](https://quarto.org/)

```bash
pip install -r requirements.txt
```

**Preview locally:** `quarto preview`

**Render site:** `quarto render`

CI/CD via GitHub Actions (`.github/workflows/publish.yml`) renders and publishes to gh-pages on push to main.

## Repository Structure

- `standards.md` — The course distilled into linkable rules (published as `standards.html`)
- `.claude/skills/review-python-package/` — Claude Code skill that audits a package against `standards.md`
- `*.qmd` — Course modules (00-07), each a Quarto reveal.js slide deck
- `_quarto.yml` — Quarto site configuration
- `projects/data_cleaning/` — Capstone homework project (progressive weekly assignments)
- `group_work/` — Group discussion prompts per module
- `examples/` — Code examples organized by module (03_oop, 04_testing, 06_documentation)
