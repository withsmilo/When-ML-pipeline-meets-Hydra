import json


def foo(dataset_info, param_info):
    print("========== Run preprocessing's 'foo' subcommand ==========")
    print(f"dataset_info:\n{json.dumps(dict(dataset_info), indent=2)}")
    print(f"param_info:\n{json.dumps(dict(param_info), indent=2)}")
    print("Do something here!")


def bar(dataset_info, param_info):
    print("========== Run preprocessing's 'bar' subcommand ==========")
    print(f"dataset_info:\n{json.dumps(dict(dataset_info), indent=2)}")
    print(f"param_info:\n{json.dumps(dict(param_info), indent=2)}")
    print("Do something here!")
