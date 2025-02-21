from tests.utils_tests import run_arg_test

def test_arg_help(capsys):
    run_arg_test(['--help'], 0, capsys)

def test_arg_help_short(capsys):
    run_arg_test(['-h'], 0, capsys)

def test_arg_wrong(capsys):
    run_arg_test(['wrong'], 10, capsys)

def test_arg_too_many(capsys):
    run_arg_test(['too', 'many'], 10, capsys)

def test_arg_wrong_and_help(capsys):
    run_arg_test(['wrong', '--help'], 10, capsys)

def test_arg_help_and_wrong(capsys):
    run_arg_test(['--help', 'wrong'], 10, capsys)

def test_arg_help_and_help(capsys):
    run_arg_test(['--help', '--help'], 10, capsys)

def test_arg_help_and_short_help(capsys):
    run_arg_test(['--help', '-h'], 10, capsys)
