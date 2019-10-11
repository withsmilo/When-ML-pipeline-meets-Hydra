from enum import Enum

from when_ml_pipeline_meets_hydra.api.deployment import bar, foo


class DeploymentSubCommand(Enum):
    FOO = "foo"
    BAR = "bar"


def _print_help():
    subs = [sub.value for sub in DeploymentSubCommand]
    print(f"Please add 'c/deployment_sub={subs}' to your command!")


def process_deployment_command(cfg):
    try:
        sub = cfg.deployment_sub.name
        if sub == DeploymentSubCommand.FOO.value:
            foo(cluster_info=cfg.cluster)
        elif sub == DeploymentSubCommand.BAR.value:
            bar(cluster_info=cfg.cluster)
        else:
            _print_help()
    except KeyError:
        _print_help()
