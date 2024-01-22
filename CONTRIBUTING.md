# Table of Contents

<!-- toc -->
- [Contributing to QTSIT](#contributing-to-QTSIT)
  - [Getting Started](#getting-started)
  - [Pull Request Process](#pull-request-process)
  - [Coding Conventions](#coding-conventions)
  - [Documentation Conventions](#documentation-conventions)
- [The Agreement](#the-agreement)
<!-- tocstop -->

## Contributing to QTSIT

We actively encourage community contributions to QTSIT. The first
place to start getting involved is
[the tutorials](https://qtsit.readthedocs.io/en/latest/get_started/tutorials.html).
Afterwards, we encourage contributors to give a shot to improving our documentation.
While we take effort to provide good docs, there's plenty of room
for improvement. All docs are hosted on Github, either in `README.md`
file, or in the `docs/` directory.

Once you've got a sense of how the package works, we encourage the use
of Github issues to discuss more complex changes, raise requests for
new features or propose changes to the global architecture of QTSIT.
Once consensus is reached on the issue, please submit a PR with proposed
modifications. All contributed code to QTSIT will be reviewed by a member
of the QTSIT team, so please make sure your code style and documentation
style match our guidelines!

### Getting Started

To develop QTSIT on your machine, we recommend using Anaconda for managing
packages. If you want to manage multiple builds of QTSIT, you can make use of
[conda environments](https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)
to maintain seperate Python package environments, each of which can be tied
to a specific build of QTSIT. Here are some tips to get started:

1. Fork the [QTSIT](https://github.com/QTSIT/qtsit/) repository
and clone the forked repository

```bash
git clone https://github.com/YOUR-USERNAME/QTSIT.git
cd QTSIT
```

&nbsp;&nbsp;&nbsp;&nbsp; 1.1. If you already have QTSIT from source, update it by running
```bash
git fetch upstream
git rebase upstream/main
```

2. Set up a new conda environment for QTSIT

```bash
conda create -n QTSIT python=3.10
conda activate QTSIT
```

3. Install QTSIT in `develop` mode

```bash
python setup.py develop
```

This mode will symlink the Python files from current local source tree into
the Python install. Hence, if you modify a Python file, you do not need to
reinstall QTSIT again and again.

In case you need to reinstall, uninstall QTSIT first by running
`pip uninstall QTSIT` until you see `Warning: Skipping QTSIT
as it is not installed`; run `python setup.py clean` and install in `develop` mode again.

Some other tips:
- Every contribution must pass the unit tests. Some tests are
[marked](https://docs.pytest.org/en/6.2.x/example/markers.html) with custom
markers like `@pytest.mark.tensorflow`. This helps mainly in two ways: 1) restricting the tests only
to the part of code marked with the marker 2) giving
[flexibility](https://docs.pytest.org/en/6.2.x/example/markers.html) in running
the unit tests depending on the environment.
- QTSIT has a number of soft requirements which can be found [here](https://QTSIT.readthedocs.io/en/latest/get_started/requirements.html).
- If a commit is simple and doesn't affect any code (keep in mind that some
docstrings contain code that is used in tests), you can add `[skip ci]`
(case sensitive) somewhere in your commit message to [skip all build /
test steps](https://github.blog/changelog/2021-02-08-github-actions-skip-pull-request-and-push-workflows-with-skip-ci/). Note that changing the pull request body or title on GitHub itself has no effect.


### Pull Request Process

Every contribution, must be a pull request and must have adequate time for
review by other committers.

A member of the Technical Steering Committee will review the pull request.
The default path of every contribution should be to merge. The discussion,
review, and merge process should be designed as corrections that move the
contribution into the path to merge. Once there are no more corrections,
(dissent) changes should merge without further process.

On successful merge the author will be added as a member of the QTSIT organization.

### Coding Conventions

QTSIT uses these tools or styles for keeping our codes healthy.

- [YAPF](https://github.com/google/yapf) (code format)
- [Flake8](https://flake8.pycqa.org/en/latest/) (code style check)
- [mypy](http://mypy-lang.org/) (type check)
- [doctest](https://docs.python.org/3/library/doctest.html) (interactive examples)
- [pytest](https://docs.pytest.org/en/6.2.x/index.html) (unit testing)

Before making a PR, please check your codes using them.
You can confirm how to check your codes from [Coding Conventions](https://qtsit.readthedocs.io/en/latest/development_guide/coding.html).

### Document Conventions

QTSIT uses [Sphinx](https://www.sphinx-doc.org/en/master/) to build
[the document](https://QTSIT.readthedocs.io/en/latest/index.html).
The document is automatically built by
[Numpy style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html#numpydoc-docstring-guide)
in source codes and [Napoleon extension](http://www.sphinx-doc.org/en/stable/ext/napoleon.html).
For any changes or modification to source code in a PR, please don't forget to add or modify Numpy style docstrings.

## The Agreement

Contributor offers to license certain software (a “Contribution” or multiple
“Contributions”) to QTSIT, and QTSIT agrees to accept said Contributions,
under the terms of the open source license [The MIT License](https://opensource.org/licenses/MIT)

The Contributor understands and agrees that QTSIT shall have the
irrevocable and perpetual right to make and distribute copies of any Contribution, as
well as to create and distribute collective works and derivative works of any Contribution,
under [The MIT License](https://opensource.org/licenses/MIT).

QTSIT understands and agrees that Contributor retains copyright in its Contributions.
Nothing in this Contributor Agreement shall be interpreted to prohibit Contributor
from licensing its Contributions under different terms from the
[The MIT License](https://opensource.org/licenses/MIT) or this Contributor Agreement.
