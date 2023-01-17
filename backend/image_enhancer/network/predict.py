
from .model import create_vgg_model
from .data_setup import preprocess, deprocess, get_features, gram_matrix
from .loss_functions import content_loss, style_loss, total_loss
from torch import optim
import numpy as np
from PIL import Image


def predict(content_image, style_image):

    # Create model
    model = create_vgg_model() 

    # Transform images
    content_img = preprocess(content_image) 
    style_img = preprocess(style_image)
    target_img = content_img.clone().requires_grad_(True)

    content_features = get_features(content_img, model) 
    style_features = get_features(style_img, model)
    
    style_gram = {layer: gram_matrix(style_features[layer]) for layer in style_features}

   # Inference
    optimizer = optim.Adam([target_img], lr=0.06)

    alpha_param = 1
    beta_param = 1e2
    epochs = 200
  
    for i in range(epochs):
      target_features = get_features(target_img, model)

      c_loss = content_loss(target_features['layer_4'], content_features['layer_4'])
      s_loss = style_loss(target_features, style_gram)
      t_loss = total_loss(c_loss, s_loss, alpha_param, beta_param)

      optimizer.zero_grad()
      t_loss.backward()
      optimizer.step()
        
    results = deprocess(target_img)

    return Image.fromarray((results * 255).astype(np.uint8))

#
