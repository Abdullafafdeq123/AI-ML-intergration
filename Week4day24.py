import torch 
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report)



transform=transforms.ToTensor()
traind=datasets.MNIST(
    root="data",
    train=True,
    transform=transform,
    download=True
)
testd=datasets.MNIST(
    root="data",
    train=False,
    transform=transform,
    download=True

)

traindl=DataLoader(
    traind,
    batch_size=32,
    shuffle=True
    
)
testdl=DataLoader(
    testd,
    batch_size=32,
    shuffle=False
)
images,labels=next(iter(traindl))
print(images.shape)
print(labels.shape)

class my(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.c1=nn.Conv2d(
            in_channels=1,
            out_channels=16,
            kernel_size=3
        )
        self.r1=nn.ReLU()
        
        self.m1=nn.MaxPool2d(kernel_size=2)
        
        self.f=nn.Flatten()
        
        self.l=nn.Linear(2704,10)
    
    def forward(self, x):
         x = self.c1(x)
         x = self.r1(x)
         x = self.m1(x)
         x = self.f(x)
         x = self.l(x)
            
         return x
                

        
                 
                       
               
        
   
model=my()
print(model)

out=model(images)
print(out.shape)

l=nn.CrossEntropyLoss()
print(l)

op=optim.Adam(
    model.parameters(),
    lr=0.001
)
print(op)

for epoch in range(5):
    model.train()
    tl=0
    
    for images,labels in traindl:
        out=model(images)
        
        loss=l(out,labels)
        
        op.zero_grad()
        
        loss.backward()
        
        op.step()
        
        tl+=loss.item()
    
    avgl=tl/len(traindl)
    
    print(epoch+1,avgl)
    
        

model.eval()

all_pre=[]
all_label=[]
with torch.no_grad():
    for images,labels in testdl:
        out=model(images)
    
        pred=out.argmax(dim=1)
        
        all_pre.extend(pred.tolist())
        all_label.extend(labels.tolist())
        
acc=accuracy_score(all_label,all_pre)
print(acc)

pre=precision_score(all_label,all_pre,average="macro")
print(pre)

rec=recall_score(all_label,all_pre,average="macro")
print(rec)

f1=f1_score(all_label,all_pre,average="macro")
print(f1)

con=confusion_matrix(all_label,all_pre)
print(con)

cr=classification_report(all_label,all_pre)
print(cr)