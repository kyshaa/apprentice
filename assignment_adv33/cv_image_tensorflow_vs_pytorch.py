import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor, Lambda, Compose
import torchvision
from sklearn.model_selection import train_test_split
import random
from timeit import timeit


"""TENSORFLOW"""

dataSet = 'master_dataset.npz'
with np.load(dataSet, allow_pickle=True) as data:
    dataImages = data['images']
    dataLabels = data['labels'].astype('int64')
    dataLabelNames = data['labelnames']
    
classNames = sorted(np.unique(dataLabelNames))
classLabels = sorted(np.unique(dataLabels))

# Convert size 

N = len(dataImages)
shape = (N, 200, 200, 3)
y = np.empty(shape)

for i in range(N):
    y[i] = cv.resize(dataImages[i], [200,200], interpolation=cv.INTER_NEAREST)

dataImages = y
print(dataImages.dtype, y.dtype, y.shape)


exportPath = 'tf_model/tf_96'

newModel = tf.keras.models.load_model(exportPath)

newModel.summary()


loss, acc = newModel.evaluate(dataImages, dataLabels, verbose = 2)
print(f'Restored model, accuracy: {100*acc:5.2f}')


newPredictions = newModel.predict(dataImages)
print(newPredictions.shape)


"""PYTORCH"""

dataSet = 'master_dataset.npz'
with np.load(dataSet, allow_pickle=True) as data:
    dataImages = data['images']
    dataLabels = data['labels'].astype('int64')
    dataLabelNames = data['labelnames']
    
classNames = sorted(np.unique(dataLabelNames))
classLabels = sorted(np.unique(dataLabels))

# Convert size 

N = len(dataImages)
shape = (N, 200, 200, 3)
y = np.empty(shape)

for i in range(N):
    y[i] = cv.resize(dataImages[i], [200,200], interpolation=cv.INTER_NEAREST)

dataImages = y
print(dataImages.dtype, y.dtype, y.shape)

dataImages = dataImages / 255.0
dataImages2 = torch.Tensor(dataImages)

# Convert to tuple

all_data = []
for i in range(len(dataImages2)):
   all_data.append([dataImages2[i], dataLabels[i]])

random.shuffle(all_data)

classes = {
    0: "afiq",
    1: "azureen",
    2: "gavin",
    3: "goke",
    4: "inamul",
    5: "jincheng",
    6: "mahmuda",
    7: "numan",
    8: "saseendran"
}

X, y = all_data[0]

batch_size = 20

# Create data loaders.
test_dataloader = DataLoader(all_data, batch_size=batch_size)

for X, y in test_dataloader:
    print("Shape of X [N, C, H, W]: ", X.shape)
    print("Shape of y: ", y.shape, y.dtype)
    break


import torch

# Get cpu or gpu device for training.
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

input_features = 3*200*200
# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(input_features, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 9)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)

def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
    
    return test_loss, correct

model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("pth_94.pth"))


loss_fn = nn.CrossEntropyLoss()
model.eval()

test(test_dataloader, model, loss_fn)
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

