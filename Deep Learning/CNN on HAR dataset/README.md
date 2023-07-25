# Human activity recognition (HAR) using Deep learning

Dataset used : [UCI-dataset](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones)

## Libaries required: 
Tensorflow, Keras, Sklearn, and other basic libaries like Numpy, Pandas, Matplotlib

## Some Screenshots

![image](https://github.com/hkcs1206/MindWave/assets/96352622/b2400e7a-0b70-469f-ac37-945f78ee6c0c)
![image](https://github.com/hkcs1206/MindWave/assets/96352622/d15182a0-3a68-42bf-8775-f7929608b278)

## Results

| Models | train accuracy | train loss | test accuracy | test loss |
|--------|----------------|------------|---------------|-----------|
| CNN    | 97.49%         | 0.1328     | 96.99%        | 0.1423    |
| DNN    | 94.53%         | 0.1353     | 94.05%        | 0.1698    |
| RNN    | 98.88%         | 0.0387     | 98.25%        | 0.0474    |

* training : validation = 6 : 4
* 50 epochs run for each model
