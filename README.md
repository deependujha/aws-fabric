# Command

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

- two nodes, each with 2 CPU devices (let main-address be the IP of node 0)

```bash
# Terminal 1
fabric run \
    --node-rank=0  \
    --main-address=10.10.10.16 \
    --accelerator=cpu \
    --devices=2 \
    --num-nodes=2 \
    train.py

# Terminal 2
fabric run \
    --node-rank=1  \
    --main-address=10.10.10.16 \
    --accelerator=cpu \
    --devices=2 \
    --num-nodes=2 \
    train.py
```
