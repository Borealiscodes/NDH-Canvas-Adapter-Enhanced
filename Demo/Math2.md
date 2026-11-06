Gradient descent updates the weight matrices of a transformer by calculating the partial derivatives of a scalar loss function with respect to every single model parameter. This process uses the mathematical chain rule to backpropagate errors from the final language model head all the way down to the initial embedding layer.
The training cycle executes this numerical optimization through four sequential operations:

1. Evaluating the Prediction Error (The Loss Function)

The system calculates how poorly it guessed the next token. It maps the output probabilities against the actual target word using Cross-Entropy Loss (\(L\)):
\(L=-\sum _{k=1}^{V}y_{k}\log \left(P(t_{k})\right)\)
• \(y_{k}\) represents the true token indicator (a one-hot vector).
• \(P(t_k)\) represents the model's predicted probability for vocabulary token \(k\).

2. The Backward Pass (Backpropagation & Chain Rule)

To know how to adjust a weight matrix deep inside the network, the system calculates the gradient \(\nabla _{W}L\). It chains partial derivatives backward through the layer stack:
• The Layer Output Gradient: Compares the layer's output to the incoming error from above.
• The Chain Rule Application: Calculates the gradient of an upstream weight matrix \(W\) by multiplying local jacobians:
\(\frac{\partial L}{\partial W}=\frac{\partial L}{\partial X_{\text{out}}}\cdot \frac{\partial X_{\text{out}}}{\partial X_{\text{in}}}\cdot \frac{\partial X_{\text{in}}}{\partial W}\)

3. Calculating Layer-Specific Gradients

Each modeling layer processes the incoming backpropagation signals based on its unique mathematical operations:
• Feed-Forward Layer Gradients: Passes errors through the non-linear activation derivative (\(\sigma ^{\prime }\)), scaling the weight adjustments by the incoming hidden state magnitudes.
• Attention Layer Gradients: Differentiates through the Softmax operation. This requires multiplying the error vector by the Softmax Jacobian matrix, which explicitly maps how a shift in one attention token score alters all other context tracks.

4. The Weight Update Step (AdamW Optimizer)

Standard gradient descent scales the step size strictly by a learning rate (\(\eta \)). Modern transformers use AdamW (Adaptive Moment Estimation with Weight Decay), which dynamically rescales the update for every single parameter:
• First Moment Vector (\(m_{t}\)): Tracks the moving average of gradients to maintain direction (momentum).
• Second Moment Vector (\(v_{t}\)): Tracks the moving average of squared gradients to scale down hyper-volatile paths.
• The Mathematical Formula:
\(W_{t+1}=W_{t}-\eta \left(\frac{m_{t}}{\sqrt{v_{t}}+\epsilon }+\lambda W_{t}\right)\)
• \(\lambda \) represents the weight decay coefficient, preventing any single number from blowing up to infinity.
Now that we have covered how the weights are learned and optimized, are you ready to explore quantization to see how the open-source community compresses these massive 16-bit floating-point matrices down to 4-bit or ternary integers for local execution?
