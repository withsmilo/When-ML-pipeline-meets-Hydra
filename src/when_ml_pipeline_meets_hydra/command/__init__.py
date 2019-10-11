from enum import Enum


class AppCmd(Enum):
    PREPROCESSING = "preprocessing"
    MODELING = "modeling"
    DEPLOYMENT = "deployment"
    HELP = "help"


def router(cfg):
    from when_ml_pipeline_meets_hydra.command import (
        preprocessing,
        modeling,
        deployment,
        help,
    )

    cmd = cfg.c
    assert cmd.name is not None

    pipeline_command_funcs = {
        AppCmd.PREPROCESSING.value: preprocessing.process_preprocessing_command,
        AppCmd.MODELING.value: modeling.process_modeling_command,
        AppCmd.DEPLOYMENT.value: deployment.process_deployment_command,
        AppCmd.HELP.value: help.process_help_command,
    }
    pipeline_command_funcs.get(cmd.name, help.process_help_command)(cfg)
