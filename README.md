# GitHub Api Workflows

## Setup

This project utilises Visual Studio Dev Containers to manage dependencies. For more information on VS Code Development Containers, see the following:
1. https://code.visualstudio.com/download
2. https://code.visualstudio.com/docs/remote/containers
3. https://code.visualstudio.com/learn/develop-cloud/containers

References:
1. [PyGitHub API Reference](https://pygithub.readthedocs.io/en/latest/apis.html)
2. [PyGitHub API Object Reference](https://pygithub.readthedocs.io/en/latest/github_objects.html)
3. [Python Requirements file](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

## Community Resources

- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [License](LICENSE)
- [Security Policy](SECURITY.md)

## Usage 

Working examples: https://github.com/jpshrader/github-api-workflow-examples

```
name: 'Run GitHub Utility'

on:
  workflow_dispatch:
    inputs:
      instructions:
        description: 'GitHub Utility instruction set to use'
        type: choice
        options:
          - './list-empty-branches.yml'
          - './list-unprotected-branches.yml'
          - './merge-branch.yml'
        required: true
      access_token:
        description: 'GitHub Api Access Token'
        type: string
        required: true

jobs:
  execute:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: jpshrader/github-api-workflows@main
        with:
          file_type: yaml
          access_token: ${{ github.event.inputs.access_token }}
          instructions: ${{ github.event.inputs.instructions }}
```

| Argument       | Description                                    | Example Value                    | Required | Supported Value(s) |
|----------------|------------------------------------------------|----------------------------------|----------|--------------------|
| `access_token` | GitHub personal access token for user          | `N/A`                            | `true`   | `N/A`              |
| `instructions` | path to instructions file                      | `./list-empty-branches.yml`      | `true`   | `N/A`              |
| `file_type`    | file format for instructions                   | `yaml`                           | `true`   | `yaml`             |

### Authentication

This utility uses [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to authenticate with the api. As a consequence, all actions performed through this utility will be 'done by' the owner of the token.

In your consuming consuming workflow, you may accept the [access token as a parameter](https://github.com/jpshrader/github-api-workflow-examples/blob/main/.github/workflows/github-utility.yml#L14-L17) or store it as a [secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets#about-encrypted-secrets).

#### Token permissions

This will of course vary on the types of operations you're performing, but at the least your token will probably need these permissions:
- repo
- user

### Merge branches

The `merge_branch` instruction checks whether there are changes to merge from `from_branch` to `to_branch`. If there are, it creates a new branch (`merge-{from_branch}-to-{to_branch}-{timestamp}`) off of `to_branch`, merges `from_branch` into that new branch, and then opens a pull request targeting `to_branch`. PR labels and reviewers can also be passed to this instruction

Examples:
```
- action: merge_branch
  repo_name: jpshrader/github-api-workflows
  from_branch: main
  to_branch: test
  labels:
    - bug
    - documentation
  reviewers:
    - jpshrader
```

| Argument      | Description                                    | Example Value                    | Required | Default Value |
|---------------|------------------------------------------------|----------------------------------|----------|---------------|
| `repo_name`   | the full name of a repo (ex. `{owner}/{slug}`) | `jpshrader/github-api-workflows` | `true`   | `N/A`         |
| `from_branch` | name of the origin branch                      | `main`                           | `true`   | `N/A`         |
| `to_branch`   | name of the destination branch                 | `main`                           | `true`   | `N/A`         |
| `labels`      | a list of label names to add to the PR         | `bug`                            | `false`  | `[]`          |
| `reviewers`   | a list of user logins to request reviews from  | `jpshrader`                      | `false`  | `[]`          |

### List Empty Branches

The `list_empty_branches` instruction iterates over every branch in a given repo and prints a list of branches that are:
 - Not protected
 - Not the `target_branch`
 - 0 commits ahead of `target_branch`

Examples:
```
- action: list_empty_branches
  repo_name: jpshrader/github-api-workflows
  target_branch: main
  include:
    - test
  exclude: 
    - jawn
```

| Argument       | Description                                                      | Example Value                   | Required | Default Value          |
|----------------|------------------------------------------------------------------|---------------------------------|----------|------------------------|
| `repo_name`    | the full name of a repo (ex. `{owner}/{slug}`)                   | `jpshrader/github-api-workflows`| `true`   | `N/A`                  |
| `target_branch`| name of the branch to diff against                               | `main`                          | `false`  | Default branch of repo |
| `include`      | a list of branch names to include (uses string contains to match)| `feature/`                      | `false`  | `[]`                   |
| `exclude`      | a list of branch names to ignore (uses string contains to match) | `releases/`                     | `false`  | `[]`                   |

### Delete Empty Branches

The `delete_empty_branches` instruction iterates over every branch in a given repo and deletes all branches that are:
 - Not protected
 - Not the `target_branch`
 - 0 commits ahead of `target_branch`

Examples:
```
- action: delete_empty_branches
  repo_name: jpshrader/github-api-workflows
  target_branch: main
  include:
    - test
  exclude: 
    - jawn
```

| Argument       | Description                                                      | Example Value                   | Required | Default Value          |
|----------------|------------------------------------------------------------------|---------------------------------|----------|------------------------|
| `repo_name`    | the full name of a repo (ex. `{owner}/{slug}`)                   | `jpshrader/github-api-workflows`| `true`   | `N/A`                  |
| `target_branch`| name of the branch to diff against                               | `main`                          | `false`  | Default branch of repo |
| `include`      | a list of branch names to include (uses string contains to match)| `feature/`                      | `false`  | `[]`                   |
| `exclude`      | a list of branch names to ignore (uses string contains to match) | `releases/`                     | `false`  | `[]`                   |

### List Unprotected Branches

The `list_unprotected_branches` instruction iterates over every branch in a given repo and prints a list of branches that do not have [protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)

Examples:
```
- action: list_unprotected_branches
  repo_name: jpshrader/github-api-workflows
  include:
    -test
  exclude: 
    - jawn
```

| Argument    | Description                                                       | Example Value                    | Required | Default Value          |
|-------------|-------------------------------------------------------------------|----------------------------------|----------|------------------------|
| `repo_name` | the full name of a repo (ex. `{owner}/{slug}`)                    | `jpshrader/github-api-workflows` | `true`   | `N/A`                  |
| `include`   | a list of branch names to include (uses string contains to match) | `feature/`                       | `false`  | `[]`                   |
| `exclude`   | a list of branch names to ignore (uses string contains to match)  | `releases/`                      | `false`  | `[]`                   |
