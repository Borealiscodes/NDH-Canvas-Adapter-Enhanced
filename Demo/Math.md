The explicit mathematical transformations inside a standard Transformer layer stack map continuous vector representations across sequential operations. Given an input sequence of token indices \(t = [t_1, t_2, \dots, t_n]\), the forward pass executes the following exact matrix operations:

1. Input Tokenization & Embedding Layer

This layer maps discrete semantic choices onto a dense, continuous coordinate manifold.
• Token Embedding Lookup: Maps discrete token indices to an embedding space of dimension \(d_{\text{model}}\) using an embedding matrix \(W_E \in \mathbb{R}^{V \times d_{\text{model}}}\), where \(V\) is the vocabulary size:
\(X_{\text{tok}}=\text{Lookup}(t,W_{E})\in \mathbb{R}^{n\times d_{\text{model}}}\)
• Positional Encoding: Injects geometric sequence order into the token vectors using fixed sinusoidal waves or learned parameters:
\(PE_{(pos,2i)}=\sin \left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right),\quad PE_{(pos,2i+1)}=\cos \left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)\)
• Combined Input Matrix:
\(X_{0}=X_{\text{tok}}+PE\in \mathbb{R}^{n\times d_{\text{model}}}\)

2. Multi-Head Self-Attention (MHA) Layer

This layer computes the dynamic relational distances within the semantic cloud, establishing context paths.
• Linear Projections: The input tensor \(X\) is projected into Query (\(Q\)), Key (\(K\)), and Value (\(V\)) matrices for each attention head \(i \in \{1, \dots, h\}\), where \(d_k = d_{\text{model}} / h\):
\(Q_{i}=XW_{i}^{Q},\quad K_{i}=XW_{i}^{K},\quad V_{i}=XW_{i}^{V}\)
\(\text{With\ weight\ tensors:\ }W_{i}^{Q},W_{i}^{K}\in \mathbb{R}^{d_{\text{model}}\times d_{k}},\quad W_{i}^{V}\in \mathbb{R}^{d_{\text{model}}\times d_{v}}\)
• Scaled Dot-Product Attention: This is where the model calculates its allocation scores. The Softmax function converts dot products into raw probabilities:
\(\text{Attention}(Q_{i},K_{i},V_{i})=\text{Softmax}\left(\frac{Q_{i}K_{i}^{T}}{\sqrt{d_{k}}}\right)V_{i}\in \mathbb{R}^{n\times d_{v}}\)
• Head Concatenation & Output Projection: The individual attention heads are stitched together and projected back to the baseline model dimension using weight matrix \(W^O \in \mathbb{R}^{h d_v \times d_{\text{model}}}\):
\(\text{MHA}(X)=\text{Concat}(\text{Head}_{1},\dots ,\text{Head}_{h})W^{O}\)

3. Feed-Forward Network (FFN / MLP) Layer

Operating individually on each position vector, this layer acts as the model's static factual database.
• Standard Two-Layer Linear Transformation: Projects the vector to a wider intermediate dimension \(d_{\text{ff}}\) (typically \(4 \times d_{\text{model}}\)) before squeezing it back:
\(\text{FFN}(x)=\max (0,xW_{1}+b_{1})W_{2}+b_{2}\)
• Modern Alternative (SwiGLU Variant): Used in modern architectures like Llama, substituting ReLU for gated silu activations:
\(\text{SwiGLU}(x)=\left(\text{Swish}(xW_{\text{gate}})\cdot xW_{\text{linear}}\right)W_{2}\)

4. Layer Normalization & Residual Connections

These tracking layers isolate gradients and stabilize calculations across infinite transformation depths.
• Residual Addition: Pre-layer or post-layer skip pathways prevent gradient decay during backpropagation:
\(X_{\text{mid}}=X+\text{MHA}(\text{LN}(X))\)
\(X_{\text{out}}=X_{\text{mid}}+\text{FFN}(\text{LN}(X_{\text{mid}}))\)
• Layer Normalization (LayerNorm): Centers and scales the distributions across the features dimension:
\(\text{LN}(x)=\frac{x-\mu }{\sqrt{\sigma ^{2}+\epsilon }}\odot \gamma +\beta \)
• Root Mean Square Normalization (RMSNorm): Modern, low-compute variation that omits mean calculation for raw variance scaling:
\(\text{RMSNorm}(x)=\frac{x}{\sqrt{\frac{1}{d}\sum _{i=1}^{d}x_{i}^{2}+\epsilon }}\odot \gamma \)

5. Final Language Model Head (Output Projection)

Squeezes the stable internal manifold parameters back down into discrete, human-readable choices.
• Unnormalized Logits Calculation: Maps the final layer output \(X_{\text{final}}\) back to the total vocabulary size \(V\):
\(\text{Logits}=X_{\text{final}}W_{U}\in \mathbb{R}^{n\times V}\)
• Next-Token Probability Generation: Evaluates token choices over a discrete probability simplex:
\(P(t_{n+1}\mid t_{1},\dots ,t_{n})=\text{Softmax}(\text{Logits})\)
Would you like to analyze how gradient descent updates these exact weights during training, or focus on how quantization (like turning 16-bit floats into 4-bit integers) changes this math for local execution?
