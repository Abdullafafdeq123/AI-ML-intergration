import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets,transforms
from torch.utils.data import DataLoader
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix)
import matplotlib.pyplot as plt

transform=transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.4914,0.4822,0.4465),std=(0.2470,0.2435,0.2616))
])

vt=transforms.ToTensor()
vtrans=datasets.CIFAR10(
    root="data",
    train=True,
    transform=vt,
    download=True
)

traind=datasets.CIFAR10(
    root="data",
    train=True,
    transform=transform,
    download=True

)
testd=datasets.CIFAR10(
    root="data",
    train=False,
    transform=transform,
    download=True
)
print(traind[0])

images,label=traind[0]
print(images.shape)
print(label)

trainld=DataLoader(
    traind,
    batch_size=32,
    shuffle=True
)

testld=DataLoader(
    testd,
    batch_size=32,
    shuffle=False
)

images,labels=next(iter(trainld))
print(images.shape)
print(labels.shape)

class my(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.c1=nn.Conv2d(
            in_channels=3,
            out_channels=32,
            kernel_size=3,
            stride=1,
            padding=1
        )
        self.r1=nn.ReLU()
        self.m1=nn.MaxPool2d(kernel_size=2,stride=2)
        
        self.c2=nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3,stride=1,padding=1)
        self.r2=nn.ReLU()
        self.m2=nn.MaxPool2d(kernel_size=2,stride=2)
        
        self.f=nn.Flatten()
        self.l1=nn.Linear(4096,128)
        self.r3=nn.ReLU()
        self.l2=nn.Linear(128,10)
    
    
    def forward(self,x):
        x=self.c1(x)
        x=self.r1(x)
        x=self.m1(x)
        x=self.c2(x)
        x=self.r2(x)
        x=self.m2(x)
        x=self.f(x)
        x=self.l1(x)
        x=self.r3(x)
        x=self.l2(x)
        
        return x
    
model=my()
print(model)

out=model(images)
print(out.shape)
print(out)

loss=nn.CrossEntropyLoss()
print(loss)
        


opt=optim.Adam(
    model.parameters(),
    lr=0.001
    
)
print(opt)



for epoch in range(5):
    model.train()
    tl=0
    for images,labels in trainld:
        out=model(images)
        losses=loss(out,labels)
        opt.zero_grad()
        losses.backward()
        opt.step()
        
        tl+=losses.item()
        
    avg=tl/len(trainld)
    print(epoch+1,avg)
                
        
model.eval()
pred=[]
actual_labels=[]
with torch.no_grad():
    for images,labels in testld:
        out=model(images)
        p=out.argmax(dim=1)
        pred.extend(p.tolist())
        actual_labels.extend(labels.tolist())
        

acc=accuracy_score(actual_labels,pred)
print(acc)
pre=precision_score(actual_labels,pred,average="weighted")
print(pre)
rec=recall_score(actual_labels,pred,average="weighted")
print(rec)
f1=f1_score(actual_labels,pred,average="weighted")
print(f1)
con=confusion_matrix(actual_labels,pred)
print(con)
print(con.shape)

images,label=vtrans[0]

print(images.shape)
print(label)

# re arrange height width channel dim1=height,dim2=width,dim3=channel
images=images.permute(1,2,0)
print(images.min())
print(images.max())
plt.imshow(images)
plt.title(f"Label:{label}")
plt.imshow(images, interpolation="nearest")
plt.show()
