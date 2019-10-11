import json


def foo(cluster_info):
    print("========== Run deployment's 'foo' subcommand ==========")
    print(f"cluster_info:\n{json.dumps(dict(cluster_info), indent=2)}")
    print("Do something here!")


def bar(cluster_info):
    print("========== Run deployment's 'bar' subcommand ==========")
    print(f"cluster_info:\n{json.dumps(dict(cluster_info), indent=2)}")
    print("Do something here!")
