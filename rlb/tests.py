import os
from click.testing import CliRunner
from .rlb import cli


# Passed 2/15/2021
# Entry point test to make sure that it is able to actually use the CLI
def test_entrypoint():
    exit_status = os.system('rlb --help')
    assert exit_status == 0


# Passing - 2/15/2021
# Testing CLI with no Typescript
def test_no_ts():
    runner = CliRunner()
    path_to = os.getcwd()
    result = runner.invoke(
        cli, ['--path', path_to, '--project-name', 'project-test'])
    assert not result.exception
    assert result.exit_code == 0


# Passing - 2/15/2021
# Testing CLI with Typescript
def test_ts():
    runner = CliRunner()
    path_to = os.getcwd()
    print(path_to)
    result = runner.invoke(
        cli, ['--path', path_to, '--project-name', 'test-project', '--typescript'])
    assert not result.exception
    assert result.exit_code == 0
