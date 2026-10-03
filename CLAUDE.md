# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational course repository for "Python package development" by DHI. Course content is delivered as Quarto-based reveal.js slide decks and hosted on GitHub Pages at https://dhi.github.io/python-package-development.

## Build & Deploy

- **Render site locally:** `quarto render`
- **Preview locally:** `quarto preview`
- **CI/CD:** GitHub Actions (`.github/workflows/publish.yml`) renders and publishes to gh-pages on push to main
- **Python version:** 3.13
- **Dependencies:** `pip install -r requirements.txt` (numpy, pytest, pydantic, jupyter)

## Repository Structure

- `standards.md` — The course distilled into linkable rules; published at `standards.html` and used as the rubric by the `review-python-package` skill. Keep the two in sync.
- `.claude/skills/review-python-package/` — Skill that audits a Python package against `standards.md`
- `*.qmd` files — Course modules (00-07), each a Quarto slide deck
- `_quarto.yml` — Quarto site configuration
- `projects/data_cleaning/` — Capstone homework project (progressive weekly assignments)
- `group_work/` — Group discussion prompts per module
- `examples/` — Code examples organized by module (03_oop, 04_testing, 06_documentation)

## Content Conventions

- Slide decks use Quarto reveal.js format with `##` for new slides
- The course teaches modern Python tooling: ruff, uv, pytest, mypy, pyproject.toml
- Weekly homework assignments in `projects/data_cleaning/01-07_Project_module.md`
