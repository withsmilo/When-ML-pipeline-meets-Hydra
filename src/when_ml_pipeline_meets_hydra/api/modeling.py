import json


def foo(model_info, param_info):
    print("========== Run modeling's 'foo' subcommand ==========")
    print(f"model_info:\n{json.dumps(dict(model_info), indent=2)}")
    print(f"param_info:\n{json.dumps(dict(param_info), indent=2)}")
    print("Do something here!")


def bar(model_info, param_info):
    print("========== Run modeling's 'bar' subcommand ==========")
    print(f"model_info:\n{json.dumps(dict(model_info), indent=2)}")
    print(f"param_info:\n{json.dumps(dict(param_info), indent=2)}")
    print("Do something here!")
