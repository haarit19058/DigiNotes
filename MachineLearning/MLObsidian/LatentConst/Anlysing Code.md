
# Notes

  

## super().__init__()

  

When you create a subclass of `nn.Module`, such as `MNISTEncoder`, you inherit a lot of useful functionality from `nn.Module`. Initializing the parent class with `super(MNISTEncoder, self).__init__()` ensures that this functionality is properly set up. Here’s a more detailed breakdown:

  

1. **Internal Structures Setup**:

- `nn.Module`’s constructor initializes internal dictionaries (like `self._modules`, `self._parameters`, and `self._buffers`) that are used to keep track of sub-modules, learnable parameters, and other tensors.

- These structures are essential for operations such as parameter updates, moving the model between devices (CPU/GPU), and saving/loading model states.

  

2. **Parameter Registration**:

- When you add layers or parameters to your model (e.g., `self.conv1 = nn.Conv2d(...)`), they need to be registered in the module’s internal structures.

- The registration happens as part of the logic defined in `nn.Module`'s `__init__` and in the attribute assignment mechanism.

- Without calling the parent class's `__init__`, the model might not correctly track these parameters, leading to issues during training or inference.

  

1. **Consistency and Functionality**:

- Many built-in methods, such as `to(device)`, `eval()`, `train()`, `state_dict()`, and `load_state_dict()`, depend on the initialization done in `nn.Module`.

- For example, when you call `model.to('cuda')`, the method iterates over all registered parameters and buffers. If these aren’t registered because the parent wasn’t properly initialized, the model might not move to the desired device correctly.

  

2. **Extensibility and Maintenance**:

- By using `super().__init__()`, you ensure that if `nn.Module` changes in future versions of PyTorch (e.g., adding new functionality in its constructor), your subclass will automatically benefit from these improvements without requiring changes in your code.

  

3. **Avoiding Subtle Bugs**:

- Omitting the parent initialization can lead to subtle bugs that are hard to trace. For instance, missing parameters in the state dictionary can result in errors when you try to load a checkpoint, or unexpected behavior when switching between training and evaluation modes.

  

In summary, initializing the parent class with `super(MNISTEncoder, self).__init__()` is crucial for properly setting up your module, ensuring that all the features provided by `nn.Module` are available to your model, and maintaining consistency with PyTorch’s internal design.


# Softmax

The **softplus** function is a smooth, differentiable approximation of the ReLU (Rectified Linear Unit) function. Mathematically, it is defined as:

softplus(x)=log⁡(1+ex)\text{softplus}(x) = \log(1 + e^x)

### Key Points:

- **Smoothness:** Unlike ReLU, which has a sharp corner at x=0x = 0, softplus is smooth everywhere. This can be beneficial in optimization since gradients change continuously.
    
- **Output Range:** The function outputs positive values for all real numbers. As x→−∞x \to -\infty, softplus(x)→0\text{softplus}(x) \to 0 and as x→∞x \to \infty, softplus(x)→x\text{softplus}(x) \to x. This behavior makes it similar to ReLU for large positive inputs while remaining smooth.
    
- **Derivative:** The derivative of softplus is the sigmoid function:
    
    ddxsoftplus(x)=11+e−x=σ(x)\frac{d}{dx} \text{softplus}(x) = \frac{1}{1 + e^{-x}} = \sigma(x)

### Usage Example in Neural Networks:

In models like the Variational Autoencoder (VAE), softplus is often used to ensure parameters such as standard deviations are positive. By passing raw outputs through softplus, we guarantee that the standard deviation (σ) is always positive, which is necessary for a valid Gaussian distribution.

Overall, softplus provides a balance between smoothness and maintaining a behavior similar to ReLU, making it a useful tool in deep learning architectures.


# Why Softplus give positive standard deviations

Below is an explanation in Obsidian-compatible Markdown:

---

# How Softplus Ensures Positive Standard Deviations

When modeling a Gaussian distribution in a Variational Autoencoder (VAE), the standard deviation (σ) must be strictly positive. However, the neural network outputs for σ can be any real number, which might include negative values. To guarantee that σ is positive, we apply the **softplus** function.

## Mathematical Explanation

The softplus function is defined as:

$softplus(x)=log⁡(1+e^x)$
### Why It Always Outputs Positive Values

1. **Exponential Term is Always Positive:**
    For any $x \in \mathbb{R}$
    $e^x > 0$
2. **Adding 1:**
    Therefore,
    $1 + e^x > 1$
    This guarantees that the argument of the logarithm is always greater than 1.
3. **Logarithm of a Number Greater Than 1:**
    The logarithm of any number greater than 1 is positive:
    $\log(1 + e^x) > 0$
    Hence, for any $x \in \mathbb{R}$, we have:
    $\text{softplus}(x) > 0$

### Application to Standard Deviations

When we compute the standard deviation in our VAE, we start with a raw output x (which can be negative or positive). By applying softplus:

$\sigma = \text{softplus}(x) = \log(1 + e^x)$

this transformation guarantees that σ is always a positive number. This is crucial because a standard deviation must be positive to represent the spread of a Gaussian distribution properly.

---

This mathematical property of softplus makes it a reliable choice for ensuring that the standard deviations output by the network are valid, i.e., strictly positive.

