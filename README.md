# Web Team - Test Percy GHA Migration

This repository holds testing scripts for the effort to migrate [Vanilla Framework](https://github.com/canonical/vanilla-framework)'s
[Percy](https://percy.io) visual testing integration from CircleCI to Github Actions.

This repo was created to test this behavior outside of the main VF repo, as part of [WD-11242](https://warthogs.atlassian.net/browse/WD-11242).
Work will be moved to the main VF repo once sufficient knowledge is gained from this repo.

## Workflows

### `upload-diff-files`

Copies files in specified directories into a GitHub Actions artifact. It is intended to run in
the context of a fork PR, meaning it will not have access to base repository secretse but it does have access to the SCM
for the proposed change.

### `create-percy-snapshots`

Downloads files from `upload-diff-files` artifact upload, uses them to start a local web server, and runs Percy to
capture and upload screenshots.
