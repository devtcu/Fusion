# generate_dataset.py
import numpy as np
from config import CONFIG
from nuclei_sampler import load_or_sample_coordinates
from graph_builder import build_graph
from ode_simulator import simulate_graph
from data_saver import save_graph_snapshot

def sample_params():
    pr = CONFIG['param_ranges']
    return {k: np.random.uniform(v[0], v[1]) for k, v in pr.items()}

def main():
    n_sim = CONFIG['n_simulations']
    t_eval = np.linspace(*CONFIG['t_span'], CONFIG['n_timepoints'])
    for sim_id in range(n_sim):
        coords = load_or_sample_coordinates()
        G = build_graph(coords)
        params = sample_params()
        sol = simulate_graph(G, params, t_eval)
        save_graph_snapshot(G, sol, t_eval, sim_id, out_dir='./synthetic_dataset')
        print(f"[✓] Generated simulation {sim_id+1}/{n_sim}")

if __name__ == "__main__":
    main()
