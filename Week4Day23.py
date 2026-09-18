import torch 
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report)

trans=transforms.ToTensor()
train_data=datasets.MNIST(
    root="data",
    train=True,
    transform=trans,
    download=True

)
test_data=datasets.MNIST(
    root="data",
    train=False,
    transform=trans,
    download=True
)

trainL=DataLoader(
    train_data,
    batch_size=32,
    shuffle=True
)
testL=DataLoader(
    test_data,
    batch_size=32,
    shuffle=False
)

print(len(train_data))
print(len(test_data))

images,labels=next(iter(trainL))
print(images)
print(labels)
print(images.shape)
print(images.dtype)
print(labels.shape)

print(labels[0])
print(len(trainL))


class my(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.fl=nn.Flatten()
        self.l1=nn.Linear(784,128)
        self.r1=nn.ReLU()
        self.l2=nn.Linear(128,10)
        
    def forward(self,x):
        x=self.fl(x)
        x=self.l1(x)
        x=self.r1(x)
        x=self.l2(x)
        
        return x
model=my()
print(model)

out=model(images)
print(out)
print(out[0])

loss=nn.CrossEntropyLoss()

op=optim.Adam(model.parameters(),lr=0.001)


for epoch in range(5):
    model.train()
    losses=[]
    for images,labels in trainL:
        
        op.zero_grad()

        newvar=model(images)

        loss_v=loss(newvar,labels)
        losses.append(loss_v.item())
        loss_v.backward()

        op.step()
    avg=sum(losses)/len(losses)
    print(epoch+1,avg)

model.eval()
all_pre=[]
all_label=[]
with torch.no_grad():
    for images,labels in testL:
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


torch.save(model.state_dict(),"mnist_ann.pth")
        
       
