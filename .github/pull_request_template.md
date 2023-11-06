### Description

<!--- Describe your changes in detail -->

Fixes  #(issue)

### Type of change
  <!--- To check a box: [x] -->
  - [ ] Bug fix (non-breaking change which fixes an issue)
  - [ ] New feature (non-breaking change which adds functionality)
  - [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
    <!--- An API breaking change will require users to also update their code, we would like to minimize these kind of changes. -->
    <!--- This does not mean we can't make those changes, we rather want to make then only once every few years. -->
    <!--- Another option is to implement the new and the old functionality and throw deprecation warnings for the old. -->
    <!--- Depending on the exact chnages the update may need to be postponed to the next major release. -->
    <!--- Below are some quick checks to determine if you break the API. -->

    <!--- IMPORTANT: If your are not sure, submbit your pull request and ask the reviewer to check. -->
    <!--- Feel free to remove the list below. -->

    If you have to check any of the boxes below you probably break the API. (**This list is not exhaustive.**)

    - [ ] Default value changed?
    - [ ] Renamed a function/class/method?
    - [ ] Order of parameters to a function/class/method changed?
    - [ ] Order of return values changed?
    - [ ] Type of input or return value changed, like `list` to `dict` or `int` to `float`.

### PR Checklist
- [ ] Followed guidelines in `CONTRIBUTING.md`.
- [ ] Added a short description of the changes to `CHANGELOG.md`.
- [ ] Added tests to make sure the code works as intended.
- [ ] Added documentation.
- [ ] New dependencies added? `pyproject.toml` and `requirements.txt` updated?
