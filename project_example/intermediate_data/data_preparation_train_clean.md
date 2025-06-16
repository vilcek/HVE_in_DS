# Clean Training Data

## Description
Cleaned and prepared training data from FD001 dataset, ready for feature engineering.

## File Information
- **Filename**: data_preparation_train_clean.csv
- **Shape**: (20631, 12)
- **Columns**: 12
- **Rows**: 20631

## Column Description
- `unit_id`: Engine unit identifier (1-100)
- `time_cycles`: Operational cycle number
- `RUL`: Remaining Useful Life (target variable)
- Sensor columns: 9 informative sensors
- Operational settings: 0 settings

## Data Preparation Applied
- **Features removed**: 16 features (uninformative + leakage prevention)
- **Data leakage prevention**: lifecycle_stage column removed (derived from target)
- **Outliers**: Preserved (important for degradation patterns)
- **Missing values**: None (0 missing values)
- **Data types**: Optimized for memory efficiency
- **Temporal structure**: Validated and maintained

## Removed Features
['sensor_6', 'sensor_2', 'sensor_5', 'sensor_8', 'sensor_16', 'op_setting_1', 'sensor_10', 'sensor_13', 'sensor_15', 'sensor_18', 'op_setting_3', 'sensor_14', 'op_setting_2', 'sensor_1', 'sensor_19', 'lifecycle_stage']

## Data Leakage Prevention
- **lifecycle_stage**: Removed as it's derived from RUL (target variable)
- **max_cycles**: Removed as it contains future information
- All features verified to contain no future information

## Loading Instructions
```python
import pandas as pd
from pathlib import Path

train_data = pd.read_csv(Path('../intermediate_data/data_preparation_train_clean.csv'))
```

## Next Steps
- Apply normalization using saved parameters
- Perform feature engineering
- Temporal feature extraction
