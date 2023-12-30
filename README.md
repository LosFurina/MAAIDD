# MAAIDD

# 1. Introduce
This project focus on analysing the effect on different Multi-agent dynamic system and graph.

## 1.1 Dynamic function

$$
\dot x_i(t)=f(x_i(t),t)- \alpha \sum_{j=1}^{N}  l_{ij}x_j(t_k), t_k \le t < t_{k+1},k \in N, i=1,2, \cdots, N
$$

## 1.2 Project skeleton

- 📁 **src**: Source code of the project.
  - 📁 **package**
    - 📁 agent: single agent class
      - 📄 agent.py
      - 📄 model.py
      - 📄 __init__.py
    - 📁 h: config file and logger file
      - 📄 config.py
      - 📄 logger.py
    - 📁 topology: topology class
      - 📄 topology.py
      - 📄 __init__.py
- 📁 **result**: Data used or generated by the project.
  - 📁 exp_id: experiment id
    - 📁 data: Save generated data
    - 📁 log: Save log
    - 📁 topology: Save generated topology
- 📁 **draw**: Tools for drawing generated data(result/exp_id/data/.gzip[.csv])
- 📄 **LICENSE**: Project's license file.
- 📄 **requirements.txt**: List of project dependencies.
- 📄 **.gitignore**: Gitignore file.
- 📄 **README.md**: README

# 2. Usage

Strongly recommend use miniconda or conda
```sh
conda create --name=MAAIDD python=3.8
conda activate MAAIDD
```

## 2.1. Clone
```sh
git clone https://github.com/LosFurina/MAAIDD.git
cd ./MAAIDD
```
## 2.2. Install requirement
```sh
pip install -r ./requirement.txt
```
## 2.3. Run and save data

- You have no need to add any parameters when running, all parameters have been set below

- Please confirm you have changed correct arguments at config.py which relates to final data saving path
```sh
python run.py
```

# 3. Config file (valid)

All parameters have been set at src/package/h/config.py

Maybe later, we will deprecate .py as config file, but moving some const hyperparameters to .yaml

Before run this project, you should change it follow your project

## 3.1. parameters introduce

| Variable Name        | Default Value | Description                                                |
|----------------------|---------------|------------------------------------------------------------|
| `node_num`           | 10            | Number of nodes in the graph                                |
| `sample_interval`    | 0.01          | Sampling interval                                          |
| `total_duration`     | 20            | Total sampling time (units: s)                              |
| `spread_interval_time`| 0.4           | Duration between control variable spread                   |
| `alpha`              | 1.5           | Strength among different agents                            |
| `is_random_graph`    | True          | If set to False, node number must be 7                      |
| `is_draw_process`    | True          | Whether drawing track draft when running simulation        |
| `is_show_log`        | True          | If True, print all log on the terminal; otherwise, print log to file |


# 4. Issue

Please open issue following request

# 5. Connect us

EthanLee0302@proton.me