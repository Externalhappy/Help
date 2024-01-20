second_indx = torch.tensor((prob.argsort(-1)[:,-2]).tolist()).to(device)
second_score = torch.tensor([row[indices].item() for row, indices in zip(prob, second_indx)]).to(device)