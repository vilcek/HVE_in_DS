# Training Data with RUL

## Description
Processed training data from FD001 dataset with calculated RUL (Remaining Useful Life) values.

## File Information
- **Filename**: data_exploration_train_with_rul.csv
- **Shape**: (20631, 28)
- **Columns**: 28
- **Rows**: 20631

## Column Description
- `unit_id`: Engine unit identifier (1-100)
- `time_cycles`: Operational cycle number
- `op_setting_1`, `op_setting_2`, `op_setting_3`: Operational settings
- `sensor_1` to `sensor_21`: Sensor measurements
- `max_cycles`: Maximum cycles for each engine
- `RUL`: Remaining Useful Life (calculated as max_cycles - time_cycles + 1)

## Loading Instructions
```python
import pandas as pd
from pathlib import Path

data = pd.read_csv(Path('../intermediate_data/data_exploration_train_with_rul.csv'))
```

## Data Quality
- No missing values
- All numerical features
- RUL calculated using formula: max_cycles - current_cycle + 1
