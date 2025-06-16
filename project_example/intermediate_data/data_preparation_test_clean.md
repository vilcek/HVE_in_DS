# Clean Test Data

## Description
Cleaned and prepared test data from FD001 dataset, ready for feature engineering.

## File Information
- **Filename**: data_preparation_test_clean.csv
- **Shape**: (13096, 12)
- **Columns**: 12
- **Rows**: 13096

## Column Description
- `unit_id`: Engine unit identifier (1-100)
- `time_cycles`: Operational cycle number
- `RUL`: Remaining Useful Life (calculated from true RUL values)
- Sensor columns: 9 informative sensors
- Operational settings: 0 settings

## Data Preparation Applied
- **Same feature removal**: As training data (16 features removed)
- **Data leakage prevention**: Same columns removed as training data
- **Outliers**: Preserved for consistency
- **Missing values**: None (0 missing values)
- **Data types**: Consistent with training data
- **RUL calculation**: Based on true test RUL values

## Data Leakage Prevention
- **lifecycle_stage**: Removed (was derived from RUL)
- **max_cycles**: Removed (future information)
- No training data information used in preprocessing

## Loading Instructions
```python
import pandas as pd
from pathlib import Path

test_data = pd.read_csv(Path('../intermediate_data/data_preparation_test_clean.csv'))
```

## Notes
- Use same normalization parameters as training data
- No data leakage from training set
- Ready for identical feature engineering pipeline
