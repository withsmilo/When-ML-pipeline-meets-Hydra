from textwrap import indent


def foo(dataset_info, param_info):
    print("========== Run preprocessing's 'foo' subcommand ==========")
    print(f"dataset:\n{indent(dataset_info.pretty(resolve=True), '  ')}")
    print(f"p_param:\n{indent(param_info.pretty(resolve=True), '  ')}")
    print("Do something here!")


def bar(dataset_info, param_info):
    print("========== Run preprocessing's 'bar' subcommand ==========")
    print(f"dataset:\n{indent(dataset_info.pretty(resolve=True), '  ')}")
    print(f"p_param:\n{indent(param_info.pretty(resolve=True), '  ')}")
    print("Do something here!")
