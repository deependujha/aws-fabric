#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y git curl vim
sudo apt-get install -y build-essential
curl -LsSf https://astral.sh/uv/install.sh | sh

# ---

uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
