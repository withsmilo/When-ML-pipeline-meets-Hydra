from enum import Enum

from when_ml_pipeline_meets_hydra.api.preprocessing import bar, foo


class PreprocessingSubCmd(Enum):
    FOO = "foo"
    BAR = "bar"


def _print_help():
    subs = [sub.value for sub in PreprocessingSubCmd]
    print(f"Please add 'c/preprocessing_sub={subs}' to your command!")


def process_preprocessing_command(cfg):
    try:
        sub = cfg.preprocessing_sub.name
        if sub == PreprocessingSubCmd.FOO.value:
            foo(dataset_info=cfg.dataset, param_info=cfg.p_param)
        elif sub == PreprocessingSubCmd.BAR.value:
            bar(dataset_info=cfg.dataset, param_info=cfg.p_param)
        else:
            _print_help()
    except KeyError:
        _print_help()
