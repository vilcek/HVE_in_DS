# Test Data

## Description
Processed test data from FD001 dataset (trajectories truncated before failure).

## File Information
- **Filename**: data_exploration_test_data.csv
- **Shape**: (13096, 26)
- **Columns**: 26
- **Rows**: 13096

## Column Description
- `unit_id`: Engine unit identifier (1-100)
- `time_cycles`: Operational cycle number
- `op_setting_1`, `op_setting_2`, `op_setting_3`: Operational settings
- `sensor_1` to `sensor_21`: Sensor measurements

## Loading Instructions
```python
import pandas as pd
from pathlib import Path

data = pd.read_csv(Path('../intermediate_data/data_exploration_test_data.csv'))
```

## Data Quality
- No missing values
- All numerical features
- Trajectories end before engine failure
