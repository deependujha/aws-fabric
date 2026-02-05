# Command

- add `clean` command & Setup machine

```bash
echo "alias clean='clear;clear'" >> ~/.bashrc && source ~/.bashrc &&\
    sudo apt-get update  &&\
    sudo apt-get upgrade -y &&\
    sudo apt-get install -y git curl vim tree &&\
    sudo apt-get install -y build-essential &&\
    curl -LsSf https://astral.sh/uv/install.sh | sh &&\
    git clone https://github.com/deependujha/aws-fabric.git &&\
    cd aws-fabric &&\
    uv venv && source .venv/bin/activate &&\
    uv pip install -r requirements.txt &&\
    echo "Setup complete! Run 'source .venv/bin/activate' to activate the virtual environment."
```

- single node, 4 CPU devices

```bash
fabric run \
    --node-rank=0  \
    --accelerator=cpu \
    --devices=4 \
    --num-nodes=1 \
    src/main.py
```

---

- check address for 0th node

```bash
(aws-fabric) ubuntu@ip-172-31-26-216:~/aws-fabric$ hostname -I
> 172.31.26.216
```

- two nodes, each with 2 CPU devices (let main-address be the IP of node 0)

```bash
# Terminal 1
fabric run \
    --node-rank=0  \
    --main-address=172.31.26.216 \
    --accelerator=cpu \
    --devices=2 \
    --num-nodes=2 \
    src/main.py

# ---

# Terminal 2
fabric run \
    --node-rank=1  \
    --main-address=172.31.26.216 \
    --accelerator=cpu \
    --devices=2 \
    --num-nodes=2 \
    src/main.py
```
