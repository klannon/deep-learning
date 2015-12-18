# ---------------------------------------------------------------------
# Trains a neural network on the run_3v data generated by OSU
#
# Authors: Colin Dablain, Matthew Drnevich, Kevin Lannon
# ---------------------------------------------------------------------

from __future__ import print_function
import sys
import os
import theano
import pylearn2
import physics # in order for this to not give an ImportError, need to
# set PYTHONPATH (see README.md)
print(physics.__file__)
import pylearn2.training_algorithms.sgd
import pylearn2.models.mlp as mlp
import pylearn2.train
import pylearn2.space
import pylearn2.termination_criteria
from math import floor

def init_train():
    hostname = os.environ["HOST"] # So scripts can be run simultaneously on different machines
    idpath = os.getcwd()
    idpath += "/results/"
    idpath += hostname
    idpath += ("_layers%s" % sys.argv[1])
    print(idpath)
    save_path = idpath + '.pkl'

    # Dataset
    pathToTrainValidData = os.environ['PYLEARN2_DATA_PATH']+os.sep+'train_all_3v_ttbar_wjet.txt'
    pathToTestData = os.environ['PYLEARN2_DATA_PATH']+os.sep+'test_all_3v_ttbar_wjet.txt'
    
    train_fraction = 0.8 # 1700000 in train file for train and valid
    numLabels = 2 # Number of output nodes...softmax interpretation here
    
    dataset_train, dataset_valid, dataset_test  = physics.PHYSICS(pathToTrainValidData,
                                                                  pathToTestData,
                                                                  train_fraction,
                                                                  numLabels=numLabels)
    # For monitoring updates without having to read in a file again.
    monitor_percent = 0.02*train_fraction
    cutoff = floor(monitor_percent*len(dataset_train.X))
    data_dict = {'data': dataset_train.X[:cutoff, :], 'labels': dataset_train.y[:cutoff], 'size': lambda: (cutoff, dataset_train.X.shape[1])}
    dataset_train_monitor = physics._PHYSICS(data_dict, 'monitor', dataset_train.args['benchmark'])


    nvis = dataset_train.X.shape[1] # number of visible layers

    # Model
    network_layers = []
    count = 1
    numlayers = int(sys.argv[1])
    while(count <= numlayers):
        network_layers.append(mlp.RectifiedLinear(
            layer_name=('r%i' % count),
            dim=100,
            istdev=.1))
        count += 1
    # add final layer
    network_layers.append(mlp.Softmax(
        layer_name='y',
        n_classes=2,
        istdev=.001))
    print(network_layers)
    model = pylearn2.models.mlp.MLP(layers=network_layers,
                                     nvis=nvis)
    # Algorithm
    algorithm = pylearn2.training_algorithms.sgd.SGD(
        batch_size=32,
        learning_rate=.001,
        monitoring_dataset = {'train':dataset_train_monitor,
                              'valid':dataset_valid,
                              'test':dataset_test
                          },
        # update_callbacks=pylearn2.training_algorithms.sgd.ExponentialDecay(
        #     decay_factor=1.0000003, # Decreases by this factor every batch. (1/(1.000001^8000)^100 
        #     min_lr=.000001
        # ),
        termination_criterion = pylearn2.termination_criteria.EpochCounter(
                max_epochs = 3)
    )
    # Train
    train = pylearn2.train.Train(dataset=dataset_train,
                                 model=model,
                                 algorithm=algorithm,
                                 save_path=save_path,
                                 # extensions=[AccuracyMonitor(model, dataset_train, dataset_valid, dataset_test, save_path)],
                                 save_freq=100)
    return train

def train(mytrain):
    # Execute training loop.
    logfile = os.path.splitext(mytrain.save_path)[0] + '.log'
    print('Using=%s' % theano.config.device) # Can use gpus.
    print('Writing to %s' % logfile)
    print('Writing to %s' % mytrain.save_path)
    sys.stdout = open(logfile, 'w')
    print("opened log file")
    mytrain.main_loop()

if __name__ == "__main__":
	mytrain = init_train()
    train(mytrain)
