# Multi-node distributed training on `AWS` using `Lightning Fabric` ⚡️

## Create 2 AWS EC2 instances

- Use latest `Ubuntu` AMI
- Instance type: `t2.large` (2 vCPU, 8 GiB memory)
- Security Group: Allow ssh traffic and all tcp traffic between the instances (for inter-node communication)
![security-group](/assets/security-group.png)

- Add storage of `50 GB` or more (so you don't get out of space when installing dependencies)
- Create 2 instances and connect in parallel using `tmux` or `terminator` (or any terminal multiplexer of your choice)
![connect-instances](/assets/connect.png)

---

## Setup both machines for distributed training

- add `clean` command (clear terminal, personal preference) & Setup machine

```bash
# paste the following commands in both instances

echo "alias clean='clear;clear'" >> ~/.bashrc && source ~/.bashrc &&\
    sudo apt-get update  &&\
    sudo apt-get upgrade -y &&\
    sudo apt-get install -y git curl vim tree &&\
    sudo apt-get install -y build-essential &&\
    curl -LsSf https://astral.sh/uv/install.sh | sh &&\
    git clone https://github.com/deependujha/aws-fabric.git &&\
    cd aws-fabric;

source $HOME/.local/bin/env uv.sh &&\
    uv venv && source .venv/bin/activate &&\
    uv pip install -r requirements.txt &&\
    echo "Setup complete!"
```

---

## Get private IP address of 0th node (main node)

```bash
# on node 0
hostname -I # for ubuntu
```

- it should return something like `172.31.16.139`, which will be used as `main-address` for both nodes in the next step

---

## MMT on two nodes, each with 2 CPU devices

> MMT: Multi-node, Multi-Device Training
![command](/assets/command.png)


```bash
# Terminal 1
fabric run \
    --node-rank=0  \
    --main-address=172.31.16.139 \
    --accelerator=cpu \
    --devices=2 \
    --num-nodes=2 \
    src/main.py

# ---

# Terminal 2
fabric run \
    --node-rank=1  \
    --main-address=172.31.16.139 \
    --accelerator=cpu \
    --devices=2 \
    --num-nodes=2 \
    src/main.py
```

![training](/assets/distributed-training.png)

---

Thanks.

Credits: [Lightning AI multi node training](https://lightning.ai/docs/fabric/stable/guide/multi_node/barebones.html)
