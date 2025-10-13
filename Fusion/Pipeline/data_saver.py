# data_saver.py
import pandas as pd
import os
import numpy as np

def save_graph_snapshot(G, sol, t_eval, sim_id, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    n = len(G.nodes)
    T, I, S, V = np.split(sol.y, 4)
    coords = np.array([[G.nodes[i]['x'], G.nodes[i]['y']] for i in G.nodes])

    for idx, t in enumerate(t_eval):
        df = pd.DataFrame({
            'x': coords[:, 0],
            'y': coords[:, 1],
            'T': T[:, idx],
            'I': I[:, idx],
            'S': S[:, idx],
            'V': V[:, idx]
        })
        df.to_csv(f"{out_dir}/graph_{sim_id:04d}_t{idx:03d}.csv", index=False)
