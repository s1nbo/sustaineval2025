from model import Model
import wandb
import yaml


'''
W&B
def sweep_entrypoint():
    model = Model()
    model.run_sweep_training(wandb.config)

if __name__ == '__main__':
    sweep_config = yaml.safe_load(open("sweep.yaml"))
    sweep_id = wandb.sweep(sweep_config, project="sustaineval")
    wandb.agent(sweep_id, function=sweep_entrypoint, count=1000)
'''

if __name__ == "__main__":
    model = Model()
    model.optuna_training(n_trials=1000)
