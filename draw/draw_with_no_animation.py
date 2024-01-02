import pandas as pd
import matplotlib.pyplot as plt

# 从 gzip 压缩文件读取数据
df_collect = pd.read_csv("D:\\git\\MAAIDD\\result\\7-80-20240102-0109\\data\\df_collect", compression="gzip")

# 选择 agent_id 列为 1 的行
df_list = []
for agent_id in df_collect["AgentID"].unique():
    df_agent_id = df_collect[df_collect['AgentID'] == agent_id]
    df_list.append(df_agent_id)

# 创建轨迹图
plt.subplots()

for agent_id in df_collect["AgentID"].unique():
    plt.scatter(df_list[int(agent_id)].X, df_list[int(agent_id)].Y, label=f"Agent {agent_id}", s=5)

# 设置图表标题和标签
plt.title('Agent Trajectories')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')

# 显示图例
plt.legend()
plt.show()
