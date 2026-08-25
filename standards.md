# Python package standards

The rules from the [Python package development](index.qmd) course, distilled into one page.
Every section is a rule you can link to directly.

**Blocker** — the package is not fit to share until this is fixed.
**Recommended** — expected of a DHI package.
**Nice** — worth doing when you get to it.

## Repository

### Small, focused pull requests
*Recommended.* One concern per pull request. Commit messages say what changed and why. Track
work with issues.

### No data in git
*Blocker.* Only small test fixtures. Everything generated goes in `.gitignore`.

### No credentials in git
*Blocker.* Passwords, tokens and connection strings belong in GitHub secrets or a secret
store — never in the repository, not even in history.

## Layout

### src layout
*Recommended.* Package code under `src/my_library/`, tests in `tests/`, docs in `docs/`.
Imports then resolve to the *installed* package, not the working directory.

```
my_library/
├── .github/workflows/
├── src/my_library/__init__.py
├── tests/test_*.py
├── docs/index.md
├── pyproject.toml
├── uv.lock
├── README.md
└── LICENSE
```

### Modules group related code
*Recommended.* A module is one `.py` file; a package is a directory of modules with
`__init__.py`. Split by what the code is about, not by file size.

### Explicit public API
*Recommended.* `__init__.py` re-exports the names users should touch. What you export is what
you have to keep working.

```python
from ._pfsdocument import PfsDocument   # mikeio.PfsDocument is the supported name
```

### Underscore means internal
*Recommended.* A leading underscore says "not part of the public API": `_foo` may change or
disappear without it counting as a [breaking change](#breaking-changes-bump-major). Declare
the public surface with `__all__` so the boundary is explicit. (`__foo` is name mangling — a
different thing.)

### Naming conventions
*Recommended.* `lowercase_with_underscores` for variables, functions and methods;
`CamelCase` for classes; `UPPERCASE_WITH_UNDERSCORES` for constants.

## Packaging

### pyproject.toml
*Blocker.* Without `[build-system]` and `[project]` the package is not installable. `uv init
--lib` gives you a working one.

```toml
[build-system]
requires = ["uv_build>=0.8.9,<0.9.0"]
build-backend = "uv_build"

[project]
name = "my_library"
version = "0.0.1"
description = "Useful library"
readme = "README.md"
requires-python = ">=3.11"
authors = [{ name="First Last", email="initials@dhigroup.com" }]
dependencies = ["numpy"]

[project.urls]
"Homepage" = "https://github.com/DHI/my_library"
"Bug Tracker" = "https://github.com/DHI/my_library/issues"
```

### Semantic versioning
*Recommended.* `{major}.{minor}.{patch}` — major breaks, minor adds, patch fixes. Start at
`0.1.0`. `1.0` is a promise that the API is stable.

### Breaking changes bump major
*Blocker.* Removing a function, renaming one, or changing a signature — including reordering
positional arguments — breaks callers. Avoid it; when you can't, bump the major version.
Applies to the [public API](#underscore-means-internal) only.

### Deprecate before removing
*Recommended.* Warn in one version, remove in the next major — never both at once. Say what
to use instead.

```python
from warnings import deprecated      # Python 3.13+

@deprecated("Use new_function instead; removed in 2.0")
def old_function(x): ...
```

`DeprecationWarning` targets developers (hidden by default, shown in test runs);
`FutureWarning` targets end users (always visible). `mypy --enable-error-code=deprecated`
catches uses of `@deprecated`.

### Changelog
*Nice.* A `CHANGELOG.md` in [keepachangelog](https://keepachangelog.com/) format: what broke,
what's new, what's deprecated. A git log is not release notes. A stale one is worse than none,
so assemble it from a fragment per pull request ([towncrier](https://towncrier.readthedocs.io/),
[git-cliff](https://git-cliff.org/)) rather than curating it at release time.

### License
*Blocker.* No license means all rights reserved and legally unusable by others. MIT for open,
a copyright notice for internal-only. Check your dependencies' licenses too.

```
# Copyright (c) DHI
# All rights reserved.
```

## Dependencies

### Every dependency is a decision
*Recommended.* You ship someone else's code, and everything *it* depends on. Check three
things: maintained, license (GPL can force your package to be GPL), and compiled extensions
that will break installation on a colleague's laptop. `uv pip tree` shows what you ship. Don't
reinvent NumPy; don't take a dependency for twenty lines you could own.

### Libraries loose, applications pinned
*Recommended.* A library is imported by other code — keep bounds wide (`numpy>=1.11.0`) so it
doesn't conflict with what the user already has. An application is run by a user — pin
(`numpy==1.11.0`) for reproducibility.

### Development dependencies are separate
*Recommended.* pytest, ruff, mypy and mkdocs are needed to *develop* the package, not to *run*
it. Put them in `[dependency-groups]`, not `[project].dependencies`.

```toml
[dependency-groups]
dev = ["pytest", "ruff", "mypy", "mkdocs", "mkdocstrings[python]", "mkdocs-material"]
```

### uv for environments and locking
*Recommended.* One virtual environment per project, managed by `uv`. Commit `uv.lock` so
everyone resolves to the same packages.

```bash
uv add matplotlib      uv add --dev pytest
uv sync                uv run pytest
```

## Testing

### Tests exist and are automated
*Blocker.* `pytest`, in `tests/`, runnable with one command. Manual checking does not survive
the next change.

### Tests run from a clean clone
*Blocker.* Resolve test data relative to the test file. Never an absolute or home-relative
path, and never as a fallback default.

```python
TESTDATA = Path(__file__).parent / "testdata"          # good
TESTDATA = Path.home() / "src" / "ref" / "TestData"    # never
```

The wrong path is the symptom; the damage is a test that passes for its author and skips for
everyone else, so the suite reports green while verifying nothing.

A skip is not a fix — `skip`, `xfail` or `importorskip` added to turn a suite green trades a
visible failure for an invisible one. Fail CI on unexpected skips (pytest has no flag; use a
`conftest.py` hook). If the data cannot be committed (see
[No data in git](#no-data-in-git)), the check belongs in a script, not the test suite.

### Good unit tests
*Recommended.* Fast, in-memory, deterministic, order-independent, one logical concept each. No
database, no network, no random numbers.

### Test the edges
*Recommended.* Empty list, single element, empty string, empty dict, `None`, `np.nan`. That is
where the bugs are.

### Tests document behaviour
*Recommended.* A test name states a rule. Someone reading the test file should learn how the
code is meant to behave.

```python
def test_operable_period_can_be_missing():
    assert is_operable(height=1.0, period=None)

def test_height_can_not_be_missing():
    with pytest.raises(ValueError):
        is_operable(height=None)
```

### Meaningful coverage
*Nice.* `pytest --cov=my_library` to find untested code. Aim tests with the report; don't chase
the number.

## Code

### Mutable default arguments
*Blocker.* Defaults are evaluated once, at definition — not per call. A mutable default is
shared by every call, forever.

```python
def add_to_cart(x, cart=[]):      # one shared list
def add_to_cart(x, cart=None):    # ✓ then: if cart is None: cart = []
```

### Don't modify input arguments
*Recommended.* Arguments are passed by reference, so mutating them surprises the caller. Return
a new object.

```python
def clip(values):
    for i in range(len(values)):  # caller's list silently changed
        values[i] = max(0, values[i])

def clip(values):
    return [max(0, v) for v in values]     # ✓
```

### One return type
*Blocker.* One type out, on every path. A function returning `bool` on success and `str` on
failure reads as success — a non-empty string is truthy. A `return` on one path and none on
another is the same bug: the silent path returns `None`.

```python
def is_operable(height, period):
    if height > 10.0:
        return "No way!"       # str here...
    return True                # ...bool here

if is_operable(height=12.0, period=5.0):   # "No way!" is truthy — this runs
    print("Go ahead!")
```

### Errors should never pass silently
*Blocker.* Raise rather than let a bad value propagate. Use built-ins (`ValueError`, `KeyError`,
`FileNotFoundError`), or your own where the domain warrants it. Never swallow with a bare
`except`.

```python
if height < 0.0:
    raise ValueError(f"Supplied value of {height=} is unphysical.")
```

### Pure functions where you can
*Recommended.* Same input, same output, no side effects — trivial to test. Where side effects
are necessary (files, databases, plots), keep them in few, deliberate places.

### Instance variables, not class variables
*Blocker.* A mutable value in the class body is shared by every instance. Assign in `__init__`.

```python
class Toolbox:
    tools = []                # shared by all instances
    def __init__(self):
        self.tools = []       # ✓ one per object
```

### Type hints
*Recommended.* On public functions at minimum. They are hints, not enforcement, until you add a
[type checker](#type-checking-in-ci).

```python
def clip(values: list[int], *, threshold: int = 0) -> list[int]: ...
```

### Keyword-only arguments
*Recommended.* One or two positional parameters — the data the function operates on;
everything after is configuration and goes behind a `*`, so callers name it and you can add or
reorder options without breaking anyone. Three or more positional parameters is a smell:
`resample(df, 3, 0, True)` can't be read at the call site, and the order can never safely
change again.

```python
def resample(data, freq, *, offset=0, dropna=True): ...
resample(df, "1h", dropna=False)      # ✓ the data and its frequency; the rest is named
```

### Dataclasses for data
*Recommended.* Fields with type hints, a constructor, a useful `repr`, and equality by value —
for free.

```python
@dataclass
class Interval:
    start: date
    end: date
```

### Composed methods
*Recommended.* One identifiable task per function, all operations inside it at the same level
of abstraction. Expect many small functions. A script split by comments is asking to be split
into functions.

```python
def main():
    df = get_data("raw_data.csv")
    cleaned = clean_data(df)
    final = transform_data(cleaned)
    return predict(final)
```

### Comments say why, not what
*Recommended.* A comment that restates the code is noise that goes stale. Write the ones that
capture the reason. If a comment is needed to explain *what* happens, rename something instead.

```python
# Calculate the average temperature          ← says nothing the code doesn't
# Sensors report -999 when disconnected      ← you could not have known this
```

### When a long signature is a smell
*Nice.* Many optional keyword arguments with sane defaults are Pythonic — see `read_csv`,
`plot`, any sklearn estimator. The smell is not the count (that's
[positional arguments](#keyword-only-arguments), a separate rule) but arguments that switch
between **separate jobs** the function absorbed: if half the signature only applies when
another argument is set, that's several functions wearing one. Group them into a config
dataclass, offer named presets, or split into composable pieces.

```python
plot_scatter(ax, x, y, show_density=True)   # ✓ each does one job
plot_reg_line(ax, x, y)
add_skill_table(ax, x, y, metrics=["bias"])
```

### Names carry meaning
*Recommended.* `n_freezing_days` over `n`, `FREEZING_POINT` over `0.0`. Renaming is the cheapest
refactoring there is.

## Design

### Composition over inheritance
*Recommended.* Composition is "has a", inheritance is "is a". Inherit only to specialize
behaviour; most of the time composition fits better.

### Encapsulate invariants
*Recommended.* A rule enforced only in `__init__` does not survive assignment. Use `_name` plus
a property when the invariant must hold.

```python
@property
def name(self): return self._name

@name.setter
def name(self, value): self._name = value.upper()
```

### Don't reach into other classes
*Blocker.* Classes talk through public APIs. Touching another object's `_private` attributes
couples you to its internals and will break. If what you need isn't public, the other class is
missing a method — add it there.

```python
values = values[self.da.geometry.top_elements]   # reaching in
da = da.sel(layers="top")                        # ✓ ask it properly
```

### Pythonic over Java-like
*Recommended.* Implement the dunder and get the language feature: `__len__` for `len(obj)`,
`__contains__` for `in`, `__iter__` for `for`, `__getitem__` for `obj[key]`. Aim for
`tb["hammer"]`, not `tb.getToolByName("hammer")`.

### Duck typing
*Recommended.* The caller cares that the methods exist, not what the type is. No base class
required — that is what makes a scikit-learn transformer work.

### Postel's law
*Recommended.* Liberal in what you accept, conservative in what you send. Normalize input types
once, at the boundary. Pydantic does this for you.

```python
def process(number: int | str | float) -> int:
    number = int(number)
    return number * 2
```

### Right level of abstraction
*Nice.* Too little means boilerplate everywhere; too much means nothing can be adapted.
`sum(values)` over a loop, but not a framework where a function would do.

## Documentation

### README
*Blocker.* What the package does, what it requires (OS, Python version, non-Python
dependencies), and how to install it.

```bash
pip install my_library
pip install https://github.com/DHI/my_library/archive/main.zip
```

### Docstrings, numpy format
*Recommended.* On every public function and class. Written once; read in `help()`, in the
editor tooltip, and on the generated API site. Numpy format is the DHI default — set
`docstring_style: "numpy"` in mkdocs, since the default is google.

```python
def remove_outlier(data: pd.DataFrame, column: str, threshold: float = 3) -> pd.DataFrame:
    """Remove outliers from a dataframe.

    Parameters
    ----------
    threshold : float, optional
        Number of standard deviations to use as threshold, by default 3

    Returns
    -------
    pd.DataFrame
        Dataframe with outliers removed.
    """
```

### Examples that are tested
*Nice.* Wrong documentation is worse than missing documentation. `doctest` runs the examples in
your docstrings; [Quarto](https://quarto.org/) executes every snippet in prose pages at build
time. Either way broken docs fail the build instead of shipping.

```bash
uv run pytest --doctest-modules src
```

### Published API documentation
*Recommended.* `mkdocs` + `mkdocstrings` + GitHub Pages, at `https://dhi.github.io/<repository>/`.
[Quarto](https://quarto.org/), [Great Docs](https://github.com/machow/great-docs) (which wraps
Quarto) and [zensical](https://zensical.org/) are alternatives. Internal-only sites go on
access-controlled Pages on GitHub Enterprise — not on an unlisted URL.

## Automation

### CI on every push and pull request
*Blocker.* A workflow in `.github/workflows/` that installs the package and runs the tests.
This is what solves "it works on my machine".

```yaml
on:
  push: { branches: [main] }
  pull_request: { branches: [main] }

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: astral-sh/setup-uv@v6
      with: { python-version: "3.13" }
    - run: uv sync
    - run: uv run pytest
```

### Lint and format with ruff
*Recommended.* One binary, no configuration required, replaces flake8, black and isort.
`ruff check` finds unused imports, undefined names and dead variables — usually typos, sometimes
bugs; `ruff format` ends style arguments. Run both in CI.

```bash
ruff check .        ruff format --check .
```

### Type checking in CI
*Nice.* [Type hints](#type-hints) are not enforcement — a type checker is. Run `mypy` (or `ty`)
on the package, not the tests, and turn it on for new code before old. It also catches uses of
anything marked [`@deprecated`](#deprecate-before-removing).

```bash
uv run mypy src --enable-error-code=deprecated
```

### A task runner
*Nice.* One source of truth for how to run the project's tools — the fastest onboarding
document there is, for people and for coding agents. Prefer [`just`](https://just.systems)
(`uv tool install rust-just`): a single binary, `Makefile`-like syntax, `just --list` documents
itself. `make` works, but is absent on Windows. The
[DHI template](https://github.com/DHI/template-python-library) ships a `justfile`.

```just
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

check: lint typecheck test
lint:
    uv run ruff check src
test:
    uv run pytest
```

### Test the matrix
*Nice.* Test what you claim to support, and no more — every cell costs minutes on every push.
An [application](#libraries-loose-applications-pinned) has one deployment target, so one cell is
the honest matrix; a library needs the range it advertises in `requires-python`.

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    python-version: ["3.11", "3.13"]
```

## Release

### Tag every release
*Recommended.* An annotated `vX.Y.Z` tag, pushed. It is what makes "which commit is 1.2.0?"
answerable a year later, and what lets you diff two releases.

```bash
git tag -a v1.2.0 -m "v1.2.0"
git push --tags
```

### Publish from a tag or a release
*Recommended.* Let a workflow build and publish; never upload from your laptop. Use
[Trusted Publishers](https://docs.pypi.org/trusted-publishers/) so there are no secrets to
manage. Trigger on the tag, or on a published release if you want somewhere to put notes.

```yaml
on:
  push:
    tags: ["v*"]      # or:  release: { types: [published] }
```

### Somewhere to install from
*Recommended.* PyPI for public packages; Azure Artifacts or Posit Package Manager for internal
ones. Straight from GitHub works too, and needs no index at all.

```bash
pip install https://github.com/DHI/mikeio/archive/main.zip
```

### Pre-releases for anything unfinished
*Nice.* `1.0.0rc1` is not installed by default and does not appear in search — the safe way to
put something in front of users before committing to it.
