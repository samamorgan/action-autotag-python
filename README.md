# Python Container Action Template

This action will read a python version file and compare the version variable to the project's known tags. If a corresponding tag does not exist, it will be created.

## Usage

The following is an example `.github/workflows/main.yml` that will execute when a `push` to the `master` branch occurs.

### Example workflow

```yaml
name: Python 🐍 Auto Version Tag

on:
  push:
    branches: [master]

jobs:
  tag:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Version tag
        uses: samamorgan/action-autotag-python@master

        with:
          path: package/__version__.py
          variable: __version__
          github_token: ${{ secrets.GITHUB_TOKEN }}
          prefix: v
```

### Inputs

| Input               | Description                                  |
| ------------------- | -------------------------------------------- |
| path                | Path to version file                         |
| variable            | Variable name containing version information |
| prefix _(optional)_ | Prefix to add to the version tag             |
| suffix _(optional)_ | Suffix to add to the version tag             |

## Configuration

The `GITHUB_TOKEN` must be passed in. Without this, it is not possible to create a new tag. Make sure the autotag action looks like the following example:

```yaml
- uses: samamorgan/action-autotag-python@master
  with:
    path: package/__version__.py
    variable: __version__
    github_token: ${{ secrets.GITHUB_TOKEN }}
```

The action will automatically extract the token at runtime. **DO NOT MANUALLY ENTER YOUR TOKEN.** If you put the actual token in your workflow file, you'll make it accessible (in plaintext) to anyone who ever views the repository (it will be in your git history).
