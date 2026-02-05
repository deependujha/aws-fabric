import torch
import torch.nn as nn
import lightning as L

from lightning.fabric import Fabric
from torch.utils.data import DataLoader
from utils import get_dataloader, get_model_loss_optimizer

def train(model: nn.Module, criterion: nn.Module, optimizer: torch.optim.Optimizer, dataloader: DataLoader, fabric: Fabric|None=None):
    _print = print if fabric is None else fabric.print

    if fabric is not None:
        model, optimizer = fabric.setup(model, optimizer)
        dataloader = fabric.setup_dataloaders(dataloader)

    model.train()

    _print(" Training: ".center(100, "-"), end="\n\n")


    for epoch in range(20):
        epoch_loss = []
        for batch in dataloader:
            input, target = batch

            optimizer.zero_grad()
            output = model(input)
            loss = criterion(output, target)

            epoch_loss.append(loss.clone().detach().item())

            if fabric is None:
                loss.backward()
            else:
                fabric.backward(loss)
            optimizer.step()

        _print(f"Epoch {epoch+1}, Loss: {sum(epoch_loss)/len(epoch_loss)}")



def main():
    fabric = Fabric()
    # fabric.launch()
    fabric.barrier()
    fabric.seed_everything(42)
    fabric.barrier()

    fabric.print(" Details about the distributed setup:".center(100, "-"), end="\n\n")
    fabric.print(f"using strategy: {fabric.strategy}")
    fabric.print(f"using launcher: {fabric.strategy.launcher}")
    start_method = getattr(fabric.strategy, "_start_method", "None")
    fabric.print(f"using start method: {start_method}")
    fabric.print(f"Using device: {fabric.device}")

    model, criterion, optimizer = get_model_loss_optimizer()
    dataloader = get_dataloader()
    fabric.barrier()

    train(model, criterion, optimizer, dataloader, fabric)

    fabric.print("Training complete. 😳")


if __name__ == "__main__":
    main()
