from behave import *
import scripts as s
import glob
import os

tmp_path = "behave/test_folders"


@given("empty directories")
def step_imp(context):
    s.temporary_file_paths = [os.path.abspath(tmp_path)]
    # s.temporary_file_paths = [tmp_path]
    [os.remove(f) for f in glob.glob(f"{tmp_path}/*")]


@given("not empty directories")
def step_imp(context):
    with open(f"{tmp_path}/test.txt", "w") as f:
        pass
    s.temporary_file_paths = [os.path.abspath(tmp_path)]


@given("no temporary folders provided")
def step_imp(context):
    s.temporary_file_paths = []


@when("clean method is called")
def step_imp(context):
    context.res = s.clean()


@when("count method is called")
def step_imp(context):
    context.res = s.count_temp_files()


@then('the result is "{d}"')
def step_imp(context, d):
    assert context.res == int(d)
    # cleaning
    os.remove(f"{tmp_path}/test.txt")


@then("the result is False")
def step_imp(context):
    assert context.res is False
