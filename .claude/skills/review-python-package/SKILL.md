---
name: review-python-package
description: Audit a Python package repository against the DHI Python package standards — layout, pyproject, dependencies, tests, code smells, docs, CI and release setup. Produces a findings report with links to the rule each finding breaks, and offers to open GitHub issues. Use when asked to review, audit or health-check a Python package or repo, or asked "is this a proper package yet".
---

# Review a Python package

Audit a whole repository against the DHI Python package standards. This is a repository
audit — it judges the package as it stands, not a single change. If asked to review a pull
request or a diff, review only the changed files against the same standards.

## Standards

The rules live in `standards.md` at the root of the `python-package-development` repository,
published at:

```
https://dhi.github.io/python-package-development/standards.html
```

Read the local file if this skill is running inside that repository
(`../../../standards.md` from this skill's directory); otherwise fetch the published page.
**Read it before reviewing** — do not audit from memory. Every rule carries a severity
(*Blocker* / *Recommended* / *Nice*) and its heading is the anchor you cite.

## Gather evidence

Work from what the repository actually contains. Do not guess at numbers you can measure.

Run these — fast, read-only, no side effects:

```bash
ls -a                              # layout, .gitignore, LICENSE, README
cat pyproject.toml                 # build system, metadata, dependencies, versioning
ls .github/workflows/ && cat .github/workflows/*.yml
ruff check .                       # ground truth, not a guess
ruff format --check .
git log --oneline -20              # commit hygiene
git ls-files | grep -Ei '\.(csv|nc|dfs.|xlsx|zip|parquet)$'   # data in git
```

Then read the source: `src/` (or the package directory), `tests/`, `docs/`.

**Do not run** `pytest`, `mypy` or `uv sync` on your own initiative — they are slow, may need
network or credentials, and an unfamiliar test suite may have side effects. Report what the
test suite looks like and offer to run it.

## Check for the code smells the course names

Grep as a starting point, then read the hits — a grep match is a candidate, not a finding.

| Rule | Starting point |
| --- | --- |
| Mutable default arguments | `grep -rEn 'def .*=\s*(\[\]\|\{\}\|set\(\))' src/` |
| Class variables that should be instance variables | mutable assignment in a class body, outside `__init__` |
| Modified input arguments | assignment to a parameter's elements inside a function |
| Mixed return types | multiple `return` statements of different types in one function |
| Silently swallowed errors | `grep -rn 'except.*:\s*pass\|except:' src/` |
| Java-like API | `grep -rEn 'def [a-z]+[A-Z]' src/` |
| Reaching into another object's internals | `grep -rEn '\w+\.\w*\._[a-z]' src/` — exclude `self._` |
| Missing docstrings | public functions and classes with no `"""` |
| Removals with no deprecation path | `git log -p` on the public API vs `CHANGELOG.md` |

## Report

Print the report in the conversation. Do not write a file unless asked.

- One-line verdict first — is this a package someone can install and depend on, or not.
- Then **Blockers**, **Recommended**, **Nice** in that order. Omit empty sections.
- Every finding: `file:line` where there is one, what is wrong in one line, the fix, and the
  anchor URL of the rule.
- Say what you checked and found clean — a short "✓ Packaging, docs, CI" line. Silence reads
  as "not checked".
- Report what you did not check and why (tests not run, package not installed).

```
**my_library** — not installable yet

Blockers
  ✗ pyproject.toml — no [build-system], so pip cannot build this
    https://dhi.github.io/python-package-development/standards.html#pyproject.toml
  ✗ No LICENSE — effectively all rights reserved, colleagues cannot legally use it
    https://dhi.github.io/python-package-development/standards.html#license
  ⚠ src/clean.py:22 — mutable default `cart=[]` is shared across every call; use None
    https://dhi.github.io/python-package-development/standards.html#mutable-default-arguments

Recommended
  ⚠ No .github/workflows/ — tests never run outside your machine
    https://dhi.github.io/python-package-development/standards.html#ci-on-every-push-and-pull-request

✓ Clean: layout, README, naming, dependency groups
Not checked: test suite not run (offer: `uv run pytest`)
```

Do not pad the report. A package that is in good shape gets a short report saying so.

## Afterwards

Offer, do not act:

- Open a GitHub issue per blocker (`gh issue create`) — **ask first, and confirm the target
  repository**. Creating issues is outward-facing.
- Run the test suite, or `mypy`.
- Fix the findings.
