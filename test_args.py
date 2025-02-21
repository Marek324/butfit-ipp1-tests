from tests.utils_tests import run_arg_test

def test_arg_help():
    run_arg_test(['--help'], 0)

def test_arg_help_short():
    run_arg_test(['-h'], 0)

def test_arg_wrong():
    run_arg_test(['wrong'], 10)

def test_arg_too_many():
    run_arg_test(['too', 'many'], 10)

def test_arg_wrong_and_help():
    run_arg_test(['wrong', '--help'], 10)

def test_arg_help_and_wrong():
    run_arg_test(['--help', 'wrong'], 10)

def test_arg_help_and_help():
    run_arg_test(['--help', '--help'], 10)

def test_arg_help_and_short_help():
    run_arg_test(['--help', '-h'], 10)
