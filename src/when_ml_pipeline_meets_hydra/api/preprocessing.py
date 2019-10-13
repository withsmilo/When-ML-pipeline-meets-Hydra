import json


def foo(dataset_info, param_info):
    print("========== Run preprocessing's 'foo' subcommand ==========")
    print(f"dataset:\n{json.dumps(dict(dataset_info), indent=2)}")
    print(f"p_param:\n{json.dumps(dict(param_info), indent=2)}")
    print("Do something here!")


def bar(dataset_info, param_info):
    print("========== Run preprocessing's 'bar' subcommand ==========")
    print(f"dataset:\n{json.dumps(dict(dataset_info), indent=2)}")
    print(f"p_param:\n{json.dumps(dict(param_info), indent=2)}")
    print("Do something here!")
