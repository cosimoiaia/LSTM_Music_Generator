#!/bin/bash

floyd run --gpu --env tensorflow:py2 "python lstm.py --dataset ringtones_256.txt --batch_size 256 --hidden_layer_size 1 --max_sequence_lenght 256 --epochs 5 --model_file /output/lstm_gen-1x256-5.tfl"
