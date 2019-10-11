from when_ml_pipeline_meets_hydra.command import AppCmd


def process_help_command(cfg):
    print(f"This app has {[c.value for c in AppCmd]} commands")
