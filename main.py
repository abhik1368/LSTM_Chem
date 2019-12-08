#!/usr/bin/env python3

from copy import copy
import tensorflow as tf
from data_loader.data_loader import DataLoader
from models.model import LSTMChem
from trainers.trainer import LSTMChemTrainer
from utils.config import process_config
from utils.dirs import create_dirs

CONFIG_FILE = './configs/LSTMChem_config.json'


def main():
    config = process_config(CONFIG_FILE)

    # create the experiments dirs
    create_dirs([config.tensorboard_log_dir, config.checkpoint_dir])

    print('Create the data generator.')
    train_dl = DataLoader(config, data_type='train')
    valid_dl = copy(train_dl)
    valid_dl.data_type = 'valid'

    print('Create the model.')
    model = LSTMChem(config)

    print('Create the trainer')
    trainer = LSTMChemTrainer(model.model, train_dl, valid_dl, config)

    print('Start training the model.')
    trainer.train()


if __name__ == '__main__':
    main()
