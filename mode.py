import numpy as np

# Create a sample tensor (you can replace this with your own tensor)
tensor = np.array([[1, 4, 3, 4],
                   [2, 3, 4, 5],
                   [3, 4, 5, 6]])

# Calculate mode along a specific axis (axis=1 for rows, axis=0 for columns)
mode_values = np.apply_along_axis(lambda x: np.argmax(np.bincount(x)), axis=1, arr=tensor)

# Calculate the count of the mode along the same axis
mode_counts = np.apply_along_axis(lambda x: np.max(np.bincount(x)), axis=1, arr=tensor)

print("Mode values along each row:", mode_values)
print("Mode counts along each row:", mode_counts)


## -------------- Pytorch ---------------------------
import torch
import numpy as np
# Create a sample tensor (you can replace this with your own tensor)
tensor = torch.tensor([[1, 4, 3, 4],
                       [2, 3, 4, 5],
                       [3, 4, 5, 6]])

# Convert the tensor to a numpy array for easy mode calculation
numpy_tensor = tensor.numpy()

# Calculate mode along a specific axis (axis=1 for rows, axis=0 for columns)
mode_values = torch.tensor([np.argmax(np.bincount(row)) for row in numpy_tensor])

# Calculate the count of the mode along the same axis
mode_counts = torch.tensor([np.max(np.bincount(row)) for row in numpy_tensor])

print("Mode values along each row:", mode_values)
print("Mode counts along each row:", mode_counts)