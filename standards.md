# Python package standards

The rules from the [Python package development](index.qmd) course, distilled into one page.
Every section is a rule you can link to directly.

**Blocker** — the package is not fit to share until this is fixed.
**Recommended** — expected of a DHI package.
**Nice** — worth doing when you get to it.

## Repository

### Small, focused pull requests
*Recommended.* One concern per pull request. Commit often, with messages that say what
changed and why. Track work with issues.

### No data in git
*Blocker.* Only very small test fixtures belong in the repository. Use `.gitignore` for
everything generated.

### No credentials in git
*Blocker.* Passwords, tokens and connection strings go in GitHub secrets or a secret store —
never in the repository, not even in history.

## Layout

### src layout
*Recommended.* Package code under `src/my_library/`, tests in `tests/`, docs in `docs/`.
Importing then tests the *installed* package, not the working directory.

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
*Recommended.* `__init__.py` re-exports the names users should touch; internal modules are
named with a leading underscore. What you export is what you have to keep working.

```python
from ._pfsdocument import PfsDocument   # mikeio.PfsDocument is the supported name
```

### Underscore means internal
*Recommended.* A leading underscore says "not part of the public API". You may change or
remove `_foo` without it counting as a [breaking change](#breaking-changes-bump-major) —
anyone importing it did so at their own risk. Declare the public surface with `__all__` so
the boundary is explicit rather than implied. (Double underscore, `__foo`, is name mangling —
a different thing.)

### Naming conventions
*Recommended.* `lowercase_with_underscores` for variables, functions and methods;
`CamelCase` for classes; `UPPERCASE_WITH_UNDERSCORES` for constants.

## Packaging

### pyproject.toml
*Blocker.* A package without `[build-system]` and `[project]` is not installable. `uv init
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
requires-python = ">=3.12"
authors = [{ name="First Last", email="initials@dhigroup.com" }]
dependencies = ["numpy"]

[project.urls]
"Homepage" = "https://github.com/DHI/my_library"
"Bug Tracker" = "https://github.com/DHI/my_library/issues"
```

### Semantic versioning
*Recommended.* `{major}.{minor}.{patch}` — major means breaking, minor means new features,
patch means fixes. Start at `0.1.0`. `1.0` is a promise that the API is stable.

### Breaking changes bump major
*Blocker.* Removing a function, renaming one, or changing a signature — including reordering
positional arguments — breaks callers. Avoid it; when you can't, bump the major version. This
applies to the [public API](#underscore-means-internal) only.

### Deprecate before removing
*Recommended.* Warn in one version, remove in the next major — never both at once. Give
people at least a release to migrate, and say in the message what to use instead.

```python
from warnings import deprecated      # Python 3.13+

@deprecated("Use new_function instead; removed in 2.0")
def old_function(x): ...
```

`DeprecationWarning` is for developers (hidden by default, shows in test runs);
`FutureWarning` is for end users (always visible). `mypy --enable-error-code=deprecated`
catches uses of `@deprecated` at type-check time.

### Changelog
*Nice.* A `CHANGELOG.md` in [keepachangelog](https://keepachangelog.com/) format. Release
notes written from a git log are not release notes — the reader wants to know what broke,
what's new, and what's deprecated.

Curating one by hand is real work, and a stale changelog is worse than none. Think twice
before starting: if nobody reads it, skip it. If you do want one, let a tool assemble it from
a fragment per pull request — [towncrier](https://towncrier.readthedocs.io/) or
[git-cliff](https://git-cliff.org/) — so the cost lands on the author of each change rather
than on you at release time.

### License
*Blocker.* Without a license the package is "all rights reserved" and legally unusable by
others. MIT for open, a copyright notice for internal-only. Check your dependencies' licenses
too.

```
# Copyright (c) DHI
# All rights reserved.
```

## Dependencies

### Every dependency is a decision
*Recommended.* You are shipping someone else's code to your users, and pulling in everything
*it* depends on. Before adding one, check: is it maintained, what's the license (GPL can force
your package to be GPL), and does it need compiled extensions that will break installation on
a colleague's laptop? `uv pip tree` shows what you actually ship.

Neither extreme is right — don't reinvent NumPy, but don't take a dependency for twenty lines
you could write and understand yourself.

### Libraries loose, applications pinned
*Recommended.* A library is imported by other code, so keep bounds wide (`numpy>=1.11.0`) to
avoid conflicting with whatever else the user has installed. An application is run by a user,
so pin (`numpy==1.11.0`) for reproducibility.

### Development dependencies are separate
*Recommended.* pytest, ruff, mypy and mkdocs are needed to *develop* the package, not to
*run* it. They belong in `[dependency-groups]`, not `[project].dependencies`.

```toml
[dependency-groups]
dev = ["pytest", "ruff", "mypy", "mkdocs", "mkdocstrings[python]", "mkdocs-material"]
```

### uv for environments and locking
*Recommended.* One virtual environment per project, managed by `uv`. Commit `uv.lock` so
everyone resolves to the same set of packages.

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
path, and **never as a fallback default** — a default like
`os.environ.get("REF_DATA", Path.home() / "data")` looks configurable but only ever resolves
on its author's machine.

```python
TESTDATA = Path(__file__).parent / "testdata"          # good
TESTDATA = Path.home() / "src" / "ref" / "TestData"    # never
```

The wrong path is only the symptom. The damage is that the test passes for its author and
skips for everyone else, including CI, so the suite reports green while verifying nothing.

A skip is not a fix. This was a common accident before CI was the norm; now the more likely
version is a `skip` added deliberately — often by a coding agent — to get a red suite green.
That is worse than the failure it hides, because it turns a visible problem into an invisible
one. A skip whose condition is false only on your machine is a hole with no bottom.

Make CI fail on unexpected skips rather than trusting the summary line. pytest has no
built-in flag for this, but a small `conftest.py` hook that turns a skip into a failure does
the job. Then read the skip list in review: every remaining skip should have a reason you
would defend out loud.

If the data cannot be committed (see *No data in git*), the check belongs in a script, not in
the test suite.

### Good unit tests
*Recommended.* Fast, in-memory, deterministic, order-independent, and each one about a single
logical concept. No database, no network, no random numbers.

### Test the edges
*Recommended.* Empty list, single element, empty string, empty dict, `None`, `np.nan`. That is
where the bugs are.

### Tests document behaviour
*Recommended.* A test name should state a rule. Someone reading the test file should learn how
the code is meant to behave.

```python
def test_operable_period_can_be_missing():
    assert is_operable(height=1.0, period=None)

def test_height_can_not_be_missing():
    with pytest.raises(ValueError):
        is_operable(height=None)
```

### Meaningful coverage
*Nice.* `pytest --cov=my_library` to find untested code. Use the report to aim tests, not to
chase a number.

## Code

### Mutable default arguments
*Blocker.* Defaults are evaluated once, when the function is defined — not per call. A mutable
default is shared by every call, forever.

```python
def add_to_cart(x, cart=[]):      # one shared list
def add_to_cart(x, cart=None):    # ✓ then: if cart is None: cart = []
```

### Don't modify input arguments
*Recommended.* Arguments are passed by reference, so mutating them surprises the caller.
Return a new object instead.

```python
def clip(values):
    for i in range(len(values)):  # caller's list silently changed
        values[i] = max(0, values[i])

def clip(values):
    return [max(0, v) for v in values]     # ✓
```

### One return type
*Blocker.* A function that returns a `bool` on success and a `str` on failure will read as
success — a non-empty string is truthy.

A function with a `return` on one path and nothing on another is the same bug: the missing
path returns `None`.

```python
def is_operable(height, period):
    if height > 10.0:
        return "No way!"       # str here, None on every other path
    return True                # ...and bool here

if is_operable(height=12.0, period=5.0):   # "No way!" is truthy — this runs
    print("Go ahead!")
```

### Errors should never pass silently
*Blocker.* Raise rather than let a bad value propagate. Exceptions are how your code talks to
its user. Use built-ins (`ValueError`, `KeyError`, `FileNotFoundError`) or define your own
where the domain warrants it. Never swallow with a bare `except`.

```python
if height < 0.0:
    raise ValueError(f"Supplied value of {height=} is unphysical.")
```

### Pure functions where you can
*Recommended.* Same input, same output, no side effects — easier to reason about and trivial
to test. Where side effects are necessary (files, databases, plots), keep them deliberate and
in few places.

### Instance variables, not class variables
*Blocker.* A list defined in the class body is shared by every instance. Assign in `__init__`.

```python
class Toolbox:
    tools = []                # shared by all instances
    def __init__(self):
        self.tools = []       # ✓ one per object
```

### Type hints
*Recommended.* On public functions at minimum. They are hints, not enforcement — they exist
for the reader and the editor, until you add a [type checker](#type-checking-in-ci).

```python
def clip(values: list[int], *, threshold: int = 0) -> list[int]: ...
```

### Keyword-only arguments
*Recommended.* One or two positional parameters is fine — that is the data the function
operates on. Everything after them is configuration, and belongs after a `*` so callers have
to name it. You can then reorder or add options without breaking anyone.

Three or more positional parameters is a strong smell: `resample(df, 3, 0, True)` can't be
read at the call site, and nobody can safely change the order again.

```python
def resample(data, freq, *, offset=0, dropna=True): ...
resample(df, "1h", dropna=False)      # ✓ the data and its frequency; the rest is named
```

### Dataclasses for data
*Recommended.* Fields with type hints, a constructor, a useful `repr`, and equality by value
rather than by identity — for free.

```python
@dataclass
class Interval:
    start: date
    end: date
```

### Composed methods
*Recommended.* Each function does one identifiable task, and all operations inside it sit at
the same level of abstraction. Expect many small functions. A script split by comments is
asking to be split into functions.

```python
def main():
    df = get_data("raw_data.csv")
    cleaned = clean_data(df)
    final = transform_data(cleaned)
    return predict(final)
```

### Comments say why, not what
*Recommended.* A comment that restates the code is noise that goes stale. Write the ones that
capture what the code cannot say — the reason. If you need a comment to explain *what* is
happening, rename something instead.

```python
# Calculate the average temperature          ← says nothing the code doesn't
# Sensors report -999 when disconnected      ← you could not have known this
```

### When a long signature is a smell
*Nice.* Many optional keyword arguments with sane defaults are perfectly Pythonic — see
`read_csv`, `plot`, or any sklearn estimator. The smell is not the total count (that's
[positional arguments](#keyword-only-arguments), which are a separate rule); it's when the
arguments are switches for **separate jobs** the function has absorbed. If half the signature
only applies when another argument is set, that's several functions wearing one signature.

Then: group related parameters into a config dataclass, offer named presets, or split into
composable pieces that each do one thing.

```python
plot_scatter(ax, x, y, show_density=True)   # ✓ each does one job
plot_reg_line(ax, x, y)
add_skill_table(ax, x, y, metrics=["bias"])
```

### Names carry meaning
*Recommended.* `n_freezing_days` over `n`, `FREEZING_POINT` over `0.0`. Renaming is the
cheapest refactoring there is.

## Design

### Composition over inheritance
*Recommended.* Composition is "has a", inheritance is "is a". Use inheritance only to
specialize behaviour — most of the time composition is the better fit.

### Encapsulate invariants
*Recommended.* A rule enforced only in `__init__` does not survive assignment. Use `_name`
plus a property when the invariant must hold.

```python
@property
def name(self): return self._name

@name.setter
def name(self, value): self._name = value.upper()
```

### Don't reach into other classes
*Blocker.* Classes talk through public APIs. Touching another object's `_private` attributes
couples you to its internals, and it will break. If you need something that isn't public, the
other class is missing a method — add it there.

```python
values = values[self.da.geometry.top_elements]   # reaching in
da = da.sel(layers="top")                        # ✓ ask it properly
```

### Pythonic over Java-like
*Recommended.* Implement the dunder and get the language feature: `__len__` for `len(obj)`,
`__contains__` for `in`, `__iter__` for `for`, `__getitem__` for `obj[key]`. Your objects
should feel like the built-in types — `tb["hammer"]`, not `tb.getToolByName("hammer")`.

### Duck typing
*Recommended.* The caller cares that the methods exist, not what the type is. No base class or
interface required — that is what makes a scikit-learn transformer work.

### Postel's law
*Recommended.* Be liberal in what you accept, conservative in what you send. Normalize input
types once, at the boundary. Pydantic does this for you.

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
*Recommended.* On every public function and class. Written once, read in `help()`, in the
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
*Nice.* Documentation that is wrong is worse than documentation that is missing. `doctest`
runs the examples in your docstrings. For prose pages, [Quarto](https://quarto.org/) executes
every snippet as part of the build, so the docs cannot ship broken — the build fails first.

```bash
python -m doctest -v add.py
```

### Published API documentation
*Recommended.* `mkdocs` + `mkdocstrings` + GitHub Pages, at
`https://dhi.github.io/<repository>/`. [Quarto](https://quarto.org/),
[Great Docs](https://github.com/machow/great-docs) (which wraps Quarto) and
[zensical](https://zensical.org/) are viable alternatives.

A private repository can have access-controlled Pages on GitHub Enterprise — use that when the
site should stay internal, rather than relying on the URL not being found.

## Automation

### CI on every push and pull request
*Blocker.* A workflow in `.github/workflows/` that installs and runs the tests. This is what
solves "it works on my machine".

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
*Recommended.* There is no reason not to. One binary, no configuration required, and it
replaces flake8, black and isort at once. `ruff check` finds unused imports, undefined names
and dead variables — usually typos, sometimes bugs. `ruff format` ends style arguments. Run
both in CI.

```bash
ruff check .        ruff format --check .
```

### Type checking in CI
*Nice.* [Type hints](#type-hints) are not enforcement — a type checker is. Run `mypy` (or
`ty`) in CI on the package, not the tests, and turn it on for new code before old. It also
catches uses of anything you have marked
[`@deprecated`](#deprecate-before-removing).

```bash
uv run mypy src --enable-error-code=deprecated
```

### A task runner
*Nice.* One source of truth for how to run the project's tools, and the fastest onboarding
document there is — for people and for coding agents. Prefer
[`just`](https://just.systems) (`uv tool install rust-just`): a single cross-platform binary,
`Makefile`-like syntax, and `just --list` documents itself. `make` works too, but it is not
installed on Windows and is a build tool pressed into service as a task runner. The
[DHI template](https://github.com/DHI/template-python-library) ships a `justfile`.

```just
check: lint typecheck test    # justfile
lint:
    uv run ruff check src
test:
    uv run pytest
```

### Test the matrix
*Nice.* If you claim to support Windows and Python 3.10, test on Windows and Python 3.10.

Test what you claim and no more. CI is not free — every cell costs minutes on every push. An
[application](#libraries-loose-applications-pinned) has one deployment target, so one cell is
the honest matrix; a library that others install needs the range it advertises in
`requires-python`.

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    python-version: ["3.10", "3.13"]
```

## Release

### Tag every release
*Recommended.* An annotated `vX.Y.Z` tag, pushed. It is what makes "which commit is 1.2.0?"
answerable a year later, and what lets you diff two releases. Just do it — it costs one
command.

```bash
git tag -a v1.2.0 -m "v1.2.0"
git push --tags
```

### Publish from a tag or a release
*Recommended.* Let a workflow build and publish; never upload from your laptop. Use
[Trusted Publishers](https://docs.pypi.org/trusted-publishers/) so there are no secrets to
manage.

Trigger on the tag, or on a published GitHub release — either works with Trusted Publishers.
The release gives you somewhere to put release notes; the tag is one step fewer.

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
