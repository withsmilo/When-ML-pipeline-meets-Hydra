from enum import Enum

from when_ml_pipeline_meets_hydra.api.modeling import bar, foo


class ModelingSubCommand(Enum):
    FOO = "foo"
    BAR = "bar"


def _print_help():
    subs = [sub.value for sub in ModelingSubCommand]
    print(f"Please add 'c/modeling_sub={subs}' to your command!")


def process_modeling_command(cfg):
    try:
        sub = cfg.modeling_sub.name
        if sub == ModelingSubCommand.FOO.value:
            foo(model_info=cfg.model, param_info=cfg.m_param)
        elif sub == ModelingSubCommand.BAR.value:
            bar(model_info=cfg.model, param_info=cfg.m_param)
        else:
            _print_help()
    except KeyError:
        _print_help()
