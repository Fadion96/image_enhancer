from typing import Union

import torch

from apps.image_enhancer.network.data_setup import gram_matrix


def compute_content_loss(
    target: torch.Tensor, content: torch.Tensor
) -> torch.Tensor:
    loss = torch.mean((target - content) ** 2)

    return loss


def compute_style_loss(
    target_features: dict[str, torch.Tensor],
    style_grams: dict[str, torch.Tensor],
) -> torch.Tensor:
    loss = 0

    for layer in target_features:
        target_f = target_features[layer]
        target_gram = gram_matrix(target_f)
        style_gram = style_grams[layer]
        b, c, h, w = target_f.shape
        layer_loss = 0.2 * torch.mean((target_gram - style_gram) ** 2)
        loss += layer_loss / (c * h * w)
    return loss


def compute_total_loss(
    content_loss: torch.Tensor,
    style_loss: torch.Tensor,
    content_weight: Union[int, float],
    style_weight: Union[int, float],
) -> torch.Tensor:
    loss = content_weight * content_loss + style_weight * style_loss

    return loss
