# GitHub Utilities

### Setup

This project utilises Visual Studio Dev Containers to manage dependencies. For more information on VS Code Development Containers, see the following:
1. https://code.visualstudio.com/docs/remote/containers
2. https://code.visualstudio.com/learn/develop-cloud/containers

References:
1. [PyGitHub API Reference](https://pygithub.readthedocs.io/en/latest/apis.html)
2. [PyGitHub API Object Reference](https://pygithub.readthedocs.io/en/latest/github_objects.html)
3. [Python Requirements file](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

### Usage 

Working examples: https://github.com/jpshrader/github-utilities-examples

#### Merge branches

The `merge_branch` instruction creates a new branch (`merge-{from_branch}-to-{to_branch}-{timestamp}`) off of `from_branch`, and opens a pull request targeting `to_branch`. PR labels and reviewers can also be passed to this instruction

Examples:
```
- action: merge_branch
  repo_name: jpshrader/github-utilities
  from_branch: main
  to_branch: test
  labels:
    - bug
    - documentation
  reviewers:
    - jpshrader
```

| Argument      | Description                                    | Example Value                | Required | Default Value |
|---------------|------------------------------------------------|------------------------------|----------|---------------|
| `repo_name`   | the full name of a repo (ex. `{owner}/{slug}`) | `jpshrader/github-utilities` | `true`   | `N/A`         |
| `from_branch` | name of the origin branch                      | `main`                       | `true`   | `N/A`         |
| `to_branch`   | name of the destination branch                 | `main`                       | `true`   | `N/A`         |
| `labels`      | a list of label names to add to the PR         | `bug`                        | `false`  | `[]`          |
| `reviewers`   | a list of user logins to request reviews from  | `jpshrader`                  | `false`  | `[]`          |

#### List Empty Branches

The `list_empty_branches` instruction iterates over every branch in a given repo and prints a list of branches that are:
 - Not protected
 - Not the `target_branch`
 - 0 commits ahead of `target_branch`

Examples:
```
- action: list_empty_branches
  repo_name: jpshrader/github-utilities
  target_branch: main
  include:
    - test
  exclude: 
    - jawn
```

| Argument        | Description                                                       | Example Value                | Required | Default Value          |
|-----------------|-------------------------------------------------------------------|------------------------------|----------|------------------------|
| `repo_name`     | the full name of a repo (ex. `{owner}/{slug}`)                    | `jpshrader/github-utilities` | `true`   | `N/A`                  |
| `target_branch` | name of the branch to diff against                                | `main`                       | `true`   | Default branch of repo |
| `include`       | a list of branch names to include (uses string contains to match) | `feature/`                   | `false`  | `[]`                   |
| `exclude`       | a list of branch names to ignore (uses string contains to match)  | `releases/`                  | `false`  | `[]`                   |

#### List Unprotected Branches

The `list_unprotected_branches` instruction iterates over every branch in a given repo and prints a list of branches that do not have [protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)

Examples:
```
- action: list_unprotected_branches
  repo_name: jpshrader/github-utilities
  include:
    -test
  exclude: 
    - jawn
```

| Argument        | Description                                                       | Example Value                | Required | Default Value          |
|-----------------|-------------------------------------------------------------------|------------------------------|----------|------------------------|
| `repo_name`     | the full name of a repo (ex. `{owner}/{slug}`)                    | `jpshrader/github-utilities` | `true`   | `N/A`                  |
| `include`       | a list of branch names to include (uses string contains to match) | `feature/`                   | `false`  | `[]`                   |
| `exclude`       | a list of branch names to ignore (uses string contains to match)  | `releases/`                  | `false`  | `[]`                   |
