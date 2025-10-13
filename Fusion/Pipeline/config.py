# config.py
CONFIG = {
    'n_simulations': 1000,
    'n_timepoints': 50,
    't_span': (0, 100),  # hours
    'param_ranges': {
        'beta': (1e-8, 1e-7),
        'gamma': (0.01, 0.2),
        'p': (1e6, 1e7),
        'rp': (0.5, 2.0),
        'delta': (0.05, 0.1),
        'rd': (0.5, 2.0),
        'c': (0.05, 0.1),
        'D_V': (1e-3, 1e-2)
    }
}
