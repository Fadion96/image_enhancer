
import torch
from torchvision import transforms
from PIL import Image
import numpy as np

def preprocess(img):

  image = img.convert('RGB')
  imsize = 256
  
  transform = transforms.Compose([
      transforms.Resize((imsize, imsize)),
      transforms.ToTensor(),
      transforms.Normalize(mean=[0.485, 0.456, 0.406],
                           std=[0.229, 0.224, 0.225])
  ])

  image = transform(image)
  image = image.unsqueeze(dim=0)

  return image


def deprocess(image): # def show_image
  
  image = image.clone()
  image = image.squeeze(0)
  image = image.permute(1,2,0)
  image = image.detach().numpy()
  image = image * np.array([0.229, 0.224, 0.225]) + np.array([0.485, 0.456, 0.406])
  image = image.clip(0,1)

  return image

def get_features(image, model):

  features = {}
  layers = {
    '0': 'layer_1',
    '5': 'layer_2',
    '10': 'layer_3',
    '19': 'layer_4',
    '28': 'layer_5'
    }
  x = image

  for name, layer in model._modules.items():
    x = layer(x)
    if name in layers:
      features[layers[name]] = x

  return features


def gram_matrix(image):

  b, c, h, w = image.size()
  image = image.view(c, h*w)
  gram = torch.mm(image, image.t())
  return gram
