import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


class SimpleModel(nn.Module):
    def __init__(self, input_dim=10, hidden_dim=32, output_dim=1):
        super().__init__()
        self.l1 = nn.Linear(input_dim, hidden_dim)
        self.l2 = nn.ReLU()
        self.l3 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.l1(x)
        x = self.l2(x)
        x = self.l3(x)
        return x


def get_dataloader(
    fabric=None,
    batch_size=8,
    num_samples=1000,
    input_dim=10,
    rng_seed=42,
    drop_last=True,
):
    features = torch.randn(num_samples, input_dim)
    targets = torch.randn(num_samples, 1)

    dataset = TensorDataset(features, targets)
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        drop_last=drop_last,
    )

    return dataloader


def get_model_loss_optimizer(input_dim=10):
    model = SimpleModel(input_dim=input_dim)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    return model, criterion, optimizer
