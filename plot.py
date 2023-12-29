import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

X_embedded = TSNE(n_components=2).fit_transform(X.cpu().detach().numpy())
n = X.shape[0]
names = [f'class_{i}' for i in range(1, n+1)]
for i in range(n):
    X_label = X_embedded[i]
    plt.scatter(X_label[0], X_label[1], label=names[i])
plt.legend()
plt.savefig('images.png')