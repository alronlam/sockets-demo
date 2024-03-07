Repo with very simple demos of how sockets work.

### Local Set-up
```
make conda-env
conda activate ./env
make setup
```

### Run Examples

Remember to activate the env like this (assuming your terminal is at the project root):
```
conda activate ./env
```

In one terminal:
```
python src/1_simplest_demo/server.py
```

In another terminal:
```
python src/1_simplest_demo/client.py
```