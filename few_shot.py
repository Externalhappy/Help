from torch.utils.data import Subset
from collections import defaultdict

def build_dataset(dataset, num_shot):
    class_indices = defaultdict(list)
    for i, element in enumerate(dataset.samples):
        class_indices[element[1]].append(i)
    selected_indices = []
    for indices in class_indices.values():
        # Check if k is greater than the number of elements in the class
        if  num_shot> len(indices):
            print(f"Warning: Class has fewer than {num_shot} elements.")
            selected_indices.extend(indices)
        else:
            selected_indices.extend(random.sample(indices, num_shot))
    subset_dataset = Subset(dataset, selected_indices)    
    return subset_dataset
