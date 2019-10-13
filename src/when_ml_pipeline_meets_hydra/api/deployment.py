from textwrap import indent


def foo(cluster_info):
    print("========== Run deployment's 'foo' subcommand ==========")
    print(f"cluster:\n{indent(cluster_info.pretty(resolve=True), '  ')}")
    print("Do something here!")


def bar(cluster_info):
    print("========== Run deployment's 'bar' subcommand ==========")
    print(f"cluster:\n{indent(cluster_info.pretty(resolve=True), '  ')}")
    print("Do something here!")
