# Task 4: Modeling Results

## Executive Summary

This document summarizes the results of Task 4: Modeling for the C-MAPSS aircraft engine RUL prediction project.

### Best Model Performance
- **Best Model**: Weighted Ensemble
- **RMSE**: 9.21
- **R²**: 0.982
- **MAE**: 5.30
- **MAPE**: 7.53%
- **PHM Score**: 13970.27

### Improvement Over Baseline
- **Baseline RMSE**: 10.37
- **Best Model RMSE**: 9.21
- **Improvement**: 11.2% reduction in RMSE

## Models Evaluated

            Model      RMSE       MAE       R²      MAPE    PHM_Score
Linear Regression 35.059987 25.550042 0.740164 59.002602 2.342748e+06
 Ridge Regression 35.213814 25.713783 0.737879 62.701359 2.261207e+06
 Lasso Regression 36.213090 26.821893 0.722791 62.453005 3.413756e+06
    Random Forest 10.367854  5.641531 0.977278  9.109550 2.069470e+04
          XGBoost  9.382183  5.251529 0.981393  7.409893 3.129940e+04
         LightGBM  9.782240  5.841335 0.979772  8.134839 1.205326e+04
   Neural Network 24.488360 15.760492 0.873236 17.766739 7.521851e+05
Gradient Boosting 10.339076  6.310432 0.977404  8.815723 2.469227e+04
  Voting Ensemble  9.225282  5.339787 0.982010  7.544227 1.412023e+04
Weighted Ensemble  9.209836  5.301936 0.982070  7.525359 1.397027e+04

## Top Features (Average Importance)

                   feature  avg_importance
 sensor_4_cumulative_range      262.553787
   sensor_3_cumulative_max      251.279469
 sensor_3_cumulative_range      221.013363
   sensor_9_cumulative_std      213.271666
          time_since_start      199.308151
 sensor_7_cumulative_range      199.263425
sensor_11_cumulative_range      183.269519
  sensor_11_cumulative_std      174.038134
   sensor_3_cumulative_std      161.259928
   sensor_7_cumulative_std      160.009193
   sensor_4_cumulative_std      147.263975
   sensor_3_rolling_min_10      121.003441
   sensor_3_rolling_max_10       93.253979
   sensor_4_rolling_mean_3       92.261788
                  sensor_9       90.502161

## Model Usage Instructions

### Loading the Best Model

```python
import joblib
from pathlib import Path

# Load the best model
MODELS_PATH = Path('results_data/trained_models')
best_model = joblib.load(MODELS_PATH / 'best_model.pkl')

# Load appropriate scaler
if 'Weighted Ensemble' == 'Neural Network':
    scaler = joblib.load(MODELS_PATH / 'scaler_minmax.pkl')
else:
    scaler = joblib.load(MODELS_PATH / 'scaler_standard.pkl')

# Make predictions
X_new_scaled = scaler.transform(X_new)
predictions = best_model.predict(X_new_scaled)
```

### Test Predictions

Test predictions have been generated and saved to:
- File: `modeling_test_predictions.csv`
- Format: unit_id, predicted_RUL
- Shape: (13096, 2)
- RUL Range: 3.5 - 291.1

## Next Steps

1. **Task 5: Evaluation** - Comprehensive model evaluation using domain-specific metrics
2. **Model Deployment** - Prepare models for production deployment
3. **Business Impact Analysis** - Assess the business value of the predictions

## Files Generated

- `modeling_test_predictions.csv` - Test set predictions
- `modeling_performance_summary.csv` - All model performance metrics
- `modeling_metadata.json` - Comprehensive task metadata
- `modeling_results.md` - This documentation file
- `trained_models/` - Directory containing all saved models and scalers

---
*Generated on 2025-06-03 00:15:41*
