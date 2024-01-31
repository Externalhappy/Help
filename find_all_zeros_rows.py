def find_rows_all_zeros(matrix):
    all_zeros_mask = (matrix == 0.0)
    all_zeros_rows = torch.all(all_zeros_mask, dim=1)
    if torch.any(all_zeros_rows):
        return torch.nonzero(all_zeros_rows).squeeze().tolist()
    else:
        return None
