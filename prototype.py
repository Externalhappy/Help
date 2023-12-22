unique_y = torch.unique(labels)
means = []
for i in unique_y:
    idx = labels == i
    means.append(torch.mean(features[idx], dim=0))
prototypes = torch.stack(means, 0)