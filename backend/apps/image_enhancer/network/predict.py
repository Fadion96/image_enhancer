import numpy as np
from PIL import Image
from torch import optim

from apps.image_enhancer.network.data_setup import (
    deprocess,
    get_features,
    gram_matrix,
    preprocess,
)
from apps.image_enhancer.network.loss_functions import (
    compute_content_loss,
    compute_style_loss,
    compute_total_loss,
)
from apps.image_enhancer.network.model import create_vgg_model


def predict(
    content_image: Image.Image, style_image: Image.Image
) -> Image.Image:
    # Create model
    model = create_vgg_model()

    # Transform images
    content_tensor = preprocess(content_image)
    style_tensor = preprocess(style_image)
    target_tensor = content_tensor.clone().requires_grad_(True)

    content_features = get_features(content_tensor, model)
    style_features = get_features(style_tensor, model)

    style_gram = {
        layer: gram_matrix(style_features[layer]) for layer in style_features
    }

    # Inference
    optimizer = optim.Adam([target_tensor], lr=0.06)

    content_weight = 1
    style_weight = 1e2
    epochs = 200

    for _ in range(epochs):
        target_features = get_features(target_tensor, model)

        content_loss = compute_content_loss(
            target_features["layer_4"], content_features["layer_4"]
        )
        style_loss = compute_style_loss(target_features, style_gram)
        total_loss = compute_total_loss(
            content_loss, style_loss, content_weight, style_weight
        )

        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

    results = deprocess(target_tensor)

    return Image.fromarray((results * 255).astype(np.uint8))


#
