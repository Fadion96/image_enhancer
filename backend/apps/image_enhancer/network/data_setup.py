import numpy as np
import torch
from PIL.Image import Image
from torchvision import transforms


def preprocess(img: Image) -> torch.Tensor:
    image = img.convert("RGB")
    imsize = 256

    transform_function = transforms.Compose(
        [
            transforms.Resize((imsize, imsize)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
            ),
        ]
    )

    image_tensor: torch.Tensor = transform_function(image)
    image_tensor = image_tensor.unsqueeze(dim=0)

    return image_tensor


def deprocess(image_tensor: torch.Tensor) -> np.ndarray:  # def show_image
    image_tensor = image_tensor.clone()
    image_tensor = image_tensor.squeeze(0)
    image_tensor = image_tensor.permute(1, 2, 0)
    image: np.ndarray = image_tensor.detach().numpy()
    image = image * np.array([0.229, 0.224, 0.225]) + np.array(
        [0.485, 0.456, 0.406]
    )
    image = image.clip(0, 1)

    return image


def get_features(
    image_tensor: torch.Tensor, model: torch.nn.Module
) -> dict[str, torch.Tensor]:
    features = {}
    layers = {
        "0": "layer_1",
        "5": "layer_2",
        "10": "layer_3",
        "19": "layer_4",
        "28": "layer_5",
    }
    x = image_tensor

    for name, layer in model._modules.items():
        x = layer(x)
        if name in layers:
            features[layers[name]] = x

    return features


def gram_matrix(image_layer: torch.Tensor) -> torch.Tensor:
    _, c, h, w = image_layer.size()
    image_layer = image_layer.view(c, h * w)
    gram = torch.mm(image_layer, image_layer.t())
    return gram
