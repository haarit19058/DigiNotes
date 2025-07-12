# AutoEncoders

Autoencoders are a type of neural network used primarily for unsupervised learning. They consist of two main parts:

1. **Encoder**: This part compresses the input data into a lower-dimensional representation (called the latent space or bottleneck).
2. **Decoder**: This part reconstructs the input data from the compressed representation.

The objective of an autoencoder is to learn an efficient representation of the data by minimizing the difference between the input and the reconstructed output. In simpler terms, it tries to capture the most important features of the input data and use them to recreate the original data as accurately as possible.

Autoencoders are used for various purposes, such as:

- **Dimensionality reduction**: Compressing high-dimensional data into a lower-dimensional form.
- **Anomaly detection**: Identifying rare or unusual patterns by comparing the reconstruction error.
- **Denoising**: Removing noise from data by training the network to recover the original clean data from noisy input.

There are different types of autoencoders, such as:

- **Variational Autoencoders (VAEs)**: These introduce probabilistic elements into the encoding process, useful in generative tasks.
- **Denoising Autoencoders**: These are trained to reconstruct data from noisy input.
- **Sparse Autoencoders**: These add a regularization term to encourage sparsity in the hidden layer, forcing the model to learn more efficient representations.


# PCA vs Encoders

Both performs dimensionality reduction
PCA learns linear relationship
Encoders can learn non-linear relationships
Encoder = PCA if the activation in linear


Encoder Bottlenech Decoder


## Training the autoencoder

- BackPropogation
- Minimise teh reconstruction error E(original data,reconstructed data)


## What is an ideal auto encoder 

- sensitive enough to input data to reconstrct it
- insensitive enough to input data not to overfit it
- Complex Loss funciotn error + regularizatoin

## Deep Convolutional autoencoder

- Similar to architecter to AE
- Convolutional Layers
- Encoder : Convolution + leaky Relu + Batch
- Decoder: COnvolutional transpose + Leaky Relu + Batch Normalization

## What is the point of compressing and Decompressign the data ??

- The latent space keep shte most important attributes of the input data
- We can levarage the latent space 

## application

- Generation
- Denoising 
- Anamoly detection
- many more
- Tagging of new samples



# Generative Adverserial Network

Understanding the math and theory of GANs.


