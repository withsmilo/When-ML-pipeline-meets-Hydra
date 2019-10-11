import hydra

from when_ml_pipeline_meets_hydra.command import router


@hydra.main(config_path="config/config.yaml")
def main(cfg):
    # print(cfg.pretty(resolve=True))
    router(cfg)


# this function is required to allow automatic detection of the module name when running
# from a binary script. It should be called from the executable script and not the
# hydra.main() function directly.
def entry():
    main()


if __name__ == "__main__":
    main()
