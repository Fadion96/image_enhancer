import torch
from .data_setup import gram_matrix


def content_loss(target, content):

    loss = torch.mean((target - content) ** 2)

    return loss


def style_loss(target_features, style_grams):

    loss = 0

    for layer in target_features:
        target_f = target_features[layer]
        target_gram = gram_matrix(target_f)
        style_gram = style_grams[layer]
        b, c, h, w = target_f.shape
        layer_loss = 0.2 * torch.mean((target_gram - style_gram) ** 2)
        loss += layer_loss / (c * h * w)

    return loss


def total_loss(content_loss, style_loss, alpha, beta):

    loss = alpha * content_loss + beta * style_loss

    return loss
