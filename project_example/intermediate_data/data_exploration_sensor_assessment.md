# Sensor Assessment Results

## Description
Comprehensive assessment of sensor informativeness for predictive modeling.

## File Information
- **Filename**: data_exploration_sensor_assessment.csv
- **Shape**: (21, 8)

## Column Description
- `sensor`: Sensor name
- `variance`: Sensor variance in training data
- `cv`: Coefficient of variation
- `rul_correlation`: Absolute correlation with RUL
- `range`: Value range (max - min)
- `unique_values`: Number of unique values
- `snr_approx`: Approximate signal-to-noise ratio
- `predictive_score`: Combined predictive value score

## Loading Instructions
```python
import pandas as pd
from pathlib import Path

assessment = pd.read_csv(Path('../intermediate_data/data_exploration_sensor_assessment.csv'))
```

## Key Findings
- **High informative sensors**: 11
- **Low informative sensors**: 10
- **Top predictive sensors**: ['sensor_9', 'sensor_14', 'sensor_4', 'sensor_11', 'sensor_12']
