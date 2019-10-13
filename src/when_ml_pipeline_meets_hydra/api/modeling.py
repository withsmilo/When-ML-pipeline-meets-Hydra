from textwrap import indent


def foo(model_info, param_info):
    print("========== Run modeling's 'foo' subcommand ==========")
    print(f"model:\n{indent(model_info.pretty(resolve=True), '  ')}")
    print(f"m_param:\n{indent(param_info.pretty(resolve=True), '  ')}")
    print("Do something here!")


def bar(model_info, param_info):
    print("========== Run modeling's 'bar' subcommand ==========")
    print(f"model:\n{indent(model_info.pretty(resolve=True), '  ')}")
    print(f"m_param:\n{indent(param_info.pretty(resolve=True), '  ')}")
    print("Do something here!")
