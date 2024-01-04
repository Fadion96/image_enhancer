import torchvision


def create_vgg_model() -> torchvision.Module:
    # Create model
    model_weights = torchvision.models.VGG19_Weights.DEFAULT
    model = torchvision.models.vgg19(weights=model_weights)

    # Freeze layers
    for param in model.parameters():
        param.requires_grad = False

    # Kepp only the features of the model
    model = model.features

    return model
