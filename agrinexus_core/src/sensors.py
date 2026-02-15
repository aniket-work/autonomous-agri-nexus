import numpy as np
import matplotlib.pyplot as plt
import random
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class SoilData:
    nitrogen: float  # mg/kg
    phosphorus: float # mg/kg
    potassium: float # mg/kg
    ph: float
    moisture: float # %
    timestamp: str

class SoilSensorNetwork:
    """
    Simulates a network of IoT soil sensors distributed across a field.
    """
    def __init__(self, crop_type: str = "corn"):
        self.crop_type = crop_type
        # Define optimal ranges to generate realistic deviations
        self.profiles = {
            "corn": {"n": (140, 200), "p": (30, 70), "k": (100, 200), "ph": (5.8, 7.0), "moisture": (60, 80)},
            "soybean": {"n": (20, 40), "p": (30, 60), "k": (100, 150), "ph": (6.0, 7.0), "moisture": (50, 70)},
            "wheat": {"n": (100, 150), "p": (40, 60), "k": (80, 120), "ph": (6.0, 7.5), "moisture": (40, 60)},
        }
        self.profile = self.profiles.get(crop_type, self.profiles["corn"])

    def read_sensors(self, zones: int = 4) -> List[Dict]:
        """Generates reading for N zones with realistic variance."""
        readings = []
        for i in range(zones):
            # Introduce some "problematic" variability
            is_problem_zone = random.random() < 0.3
            
            n_base = random.uniform(*self.profile["n"])
            p_base = random.uniform(*self.profile["p"])
            k_base = random.uniform(*self.profile["k"])
            ph_base = random.uniform(*self.profile["ph"])
            m_base = random.uniform(*self.profile["moisture"])

            if is_problem_zone:
                # Simulate a deficiency or excess
                n_base *= 0.6  # Nitrogen deficiency
                m_base *= 1.4  # Waterlogging
            
            readings.append({
                "zone_id": i + 1,
                "nitrogen": round(n_base, 2),
                "phosphorus": round(p_base, 2),
                "potassium": round(k_base, 2),
                "ph": round(ph_base, 2),
                "moisture": round(m_base, 2),
                "status": "Check Required" if is_problem_zone else "Optimal"
            })
        return readings

    def generate_heatmap(self, data: List[Dict], filename: str = "field_heatmap.png"):
        """Generates a visual heatmap of the field status."""
        # Simplified 2x2 grid for 4 zones
        grid = np.zeros((2, 2))
        grid[0, 0] = data[0]["nitrogen"]
        grid[0, 1] = data[1]["nitrogen"]
        grid[1, 0] = data[2]["nitrogen"]
        grid[1, 1] = data[3]["nitrogen"]

        plt.figure(figsize=(6, 5))
        plt.imshow(grid, cmap='RdYlGn', interpolation='nearest')
        plt.colorbar(label='Nitrogen Level (mg/kg)')
        plt.title(f"{self.crop_type.capitalize()} Field - Nitrogen Heatmap")
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        print(f"Heatmap saved to {filename}")
