import numpy as np
import pandas as pd

from pathlib import Path

np.random.seed(42)

n_samples = 1000

data = {
    "engine_temperature": np.random.normal(85, 10, n_samples),
    "oil_temperature": np.random.normal(90, 8, n_samples),
    "hydraulic_pressure": np.random.normal(180, 25, n_samples),
    "vibration": np.random.normal(3, 1.2, n_samples),
    "engine_rpm": np.random.normal(1800, 300, n_samples),
    "fuel_consumption": np.random.normal(15, 3, n_samples),
    "operating_hours": np.random.randint(100, 10000, n_samples)
}

df = pd.DataFrame(data)

df["failure"] = (
    (df["engine_temperature"] > 100)
    | (df["oil_temperature"] > 105)
    | (df["vibration"] > 5)
).astype(int)

output_path =Path("data/raw/equipment_sensor_data.csv")

output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path, index=False)

print(f"Dataset created successfully: {output_path}")
print(df.head())