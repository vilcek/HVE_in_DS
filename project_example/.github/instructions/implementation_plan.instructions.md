---
applyTo: '**/*.ipynb'
---

# Implementation Plan: C-MAPSS Aircraft Engine RUL Prediction

## Overview
This plan implements a comprehensive data science workflow for predicting Remaining Useful Life (RUL) of aircraft gas turbine engines using the C-MAPSS dataset (FD001). The workflow follows a CRISP-DM methodology structured across five main tasks, each implemented as an independent Jupyter notebook.

## Dataset Context
- **Focus**: FD001 dataset only (100 training trajectories, 100 test trajectories)
- **Conditions**: One operating condition (sea level)
- **Fault Modes**: One fault mode (High-Pressure Compressor degradation)
- **Target Variable**: RUL (Remaining Useful Life) - calculated from cycle data for training, provided separately for test
- **Data Format**: 26 columns (unit_id, time_cycles, 3 operational settings, 21 sensor measurements)
- **File Separator**: `\s+` (whitespace)
- **Headers**: None (column names must be created)

## Column Naming Convention
```python
COLUMN_NAMES = [
    'unit_id', 'time_cycles', 'op_setting_1', 'op_setting_2', 'op_setting_3',
    'sensor_1', 'sensor_2', 'sensor_3', 'sensor_4', 'sensor_5', 'sensor_6',
    'sensor_7', 'sensor_8', 'sensor_9', 'sensor_10', 'sensor_11', 'sensor_12',
    'sensor_13', 'sensor_14', 'sensor_15', 'sensor_16', 'sensor_17', 'sensor_18',
    'sensor_19', 'sensor_20', 'sensor_21'
]
```

---

## Task 1: Data Exploration (`01_data_exploration.ipynb`)

### Phase 1.1: Data Loading and Initial Inspection
**Objective**: Load and understand the basic structure of the FD001 dataset

#### Step 1.1.1: Environment Setup and Data Loading
- Import required libraries (pandas, numpy, matplotlib, seaborn, plotly)
- Define data paths and column names
- Load training, test, and RUL data for FD001
- Display basic dataset information (shape, dtypes, memory usage)

#### Step 1.1.2: Initial Data Quality Assessment
- Check for missing values across all datasets
- Identify data types and ranges for each column
- Examine unique values for categorical-like columns
- Document any data quality issues

### Phase 1.2: Univariate Analysis
**Objective**: Understand the distribution and characteristics of individual variables

#### Step 1.2.1: Target Variable Analysis (RUL)
- Calculate RUL for training data (max_cycles - current_cycle + 1)
- Analyze RUL distribution in training data
- Compare with test RUL values
- Visualize RUL distributions and statistics

#### Step 1.2.2: Operational Settings Analysis
- Examine distributions of operational settings (op_setting_1, op_setting_2, op_setting_3)
- Check for constant values or limited variability
- Visualize operational settings distributions
- Identify potential operational regimes

#### Step 1.2.3: Sensor Measurements Analysis
- Analyze distribution of each sensor measurement
- Identify sensors with constant values or minimal variation
- Create summary statistics table for all sensors
- Visualize sensor value ranges and distributions

### Phase 1.3: Temporal Analysis
**Objective**: Understand temporal patterns and degradation trends

#### Step 1.3.1: Engine Lifecycle Analysis
- Analyze engine lifecycle lengths (number of cycles per unit)
- Visualize lifecycle distribution
- Identify outliers in engine longevity
- Compare training vs test lifecycle characteristics

#### Step 1.3.2: Degradation Pattern Analysis
- Plot sensor values over time for sample engines
- Identify sensors showing clear degradation patterns
- Analyze early vs late lifecycle sensor behaviors
- Visualize degradation trends across different engines

#### Step 1.3.3: Operational Conditions Impact
- Analyze how operational settings change over engine lifecycle
- Examine correlation between operational settings and sensor readings
- Identify if operational conditions affect degradation patterns

### Phase 1.4: Multivariate Analysis
**Objective**: Understand relationships between variables and identify patterns

#### Step 1.4.1: Correlation Analysis
- Calculate correlation matrix for all numerical variables
- Identify highly correlated sensor pairs
- Analyze correlation between operational settings and sensors
- Visualize correlation patterns with heatmaps

#### Step 1.4.2: Sensor Informativeness Assessment
- Identify sensors with minimal variation (candidates for removal)
- Assess sensor signal-to-noise ratio
- Evaluate sensor sensitivity to degradation
- Rank sensors by potential predictive value

#### Step 1.4.3: Cross-Engine Variability Analysis
- Compare sensor patterns across different engines
- Identify consistent vs variable degradation signatures
- Analyze initial conditions variability across engines
- Assess manufacturing variation impact

### Phase 1.5: Data Export and Documentation
**Objective**: Save exploration results and insights for subsequent tasks

#### Step 1.5.1: Key Insights Documentation
- Summarize main findings from exploration
- Document data quality issues and recommendations
- List sensors recommended for feature engineering
- Identify potential modeling challenges

#### Step 1.5.2: Processed Data Export
- Save cleaned training data with RUL column
- Export test data with proper formatting
- Save exploration metadata and insights
- Create data documentation files for next tasks

---

## Task 2: Data Preparation (`02_data_preparation.ipynb`)

### Phase 2.1: Data Loading and Setup
**Objective**: Load raw data and prepare for cleaning and preprocessing

#### Step 2.1.1: Environment Setup and Data Import
- Load training, test, and RUL data for FD001
- Apply consistent column naming convention
- Verify data integrity and basic statistics
- Set up data processing pipeline framework

#### Step 2.1.2: Target Variable Creation
- Calculate RUL for training data using time cycles
- Merge test data with true RUL values
- Validate RUL calculations and distributions
- Handle any RUL calculation edge cases

### Phase 2.2: Data Cleaning
**Objective**: Clean data and handle quality issues identified in exploration

#### Step 2.2.1: Missing Value Treatment
- Confirm no missing values exist (based on exploration)
- Implement missing value strategy if any are found
- Document any imputation methods used
- Validate cleaned data completeness

#### Step 2.2.2: Outlier Detection and Treatment
- Identify statistical outliers in sensor measurements
- Analyze outliers in context of engine degradation
- Decide on outlier treatment strategy (keep/cap/remove)
- Document outlier handling decisions and rationale

#### Step 2.2.3: Data Type Optimization
- Optimize data types for memory efficiency
- Convert appropriate columns to categorical if needed
- Ensure consistent data types across train/test
- Validate data type conversions

### Phase 2.3: Feature Selection and Engineering Preparation
**Objective**: Prepare foundation for feature engineering by selecting relevant variables

#### Step 2.3.1: Uninformative Feature Removal
- Remove sensors with zero or minimal variance
- Eliminate perfectly correlated redundant features
- Drop constant operational settings (based on exploration)
- Document feature removal rationale

#### Step 2.3.2: Data Normalization Preparation
- Identify features requiring normalization/scaling
- Calculate normalization parameters from training data only
- Prepare scaling strategy for temporal features
- Document normalization approach for consistency

#### Step 2.3.3: Temporal Structure Validation
- Verify temporal ordering within each engine unit
- Check for missing time steps or irregularities
- Validate engine lifecycle completeness
- Ensure proper time series structure

### Phase 2.4: Train-Test Split Validation
**Objective**: Ensure proper separation between training and test data

#### Step 2.4.1: Data Leakage Prevention
- Verify no overlap between training and test engines
- Confirm temporal boundaries are respected
- Check for any potential data leakage sources
- Document data splitting methodology

#### Step 2.4.2: Distribution Comparison
- Compare feature distributions between train and test
- Identify any significant distribution shifts
- Analyze operational conditions consistency
- Document distribution differences and implications

### Phase 2.5: Prepared Data Export
**Objective**: Save cleaned and prepared data for feature engineering

#### Step 2.5.1: Clean Data Export
- Export cleaned training data with RUL
- Save cleaned test data and true RUL values
- Store feature selection metadata
- Create normalization parameters file

#### Step 2.5.2: Data Documentation
- Create comprehensive data dictionary
- Document all cleaning steps and decisions
- Provide loading instructions for next tasks
- Save data quality assessment results

---

## Task 3: Feature Engineering (`03_feature_engineering.ipynb`)

### Phase 3.1: Data Loading and Baseline Features
**Objective**: Load prepared data and establish baseline feature set

#### Step 3.1.1: Prepared Data Loading
- Load cleaned data from data preparation task
- Apply saved normalization parameters
- Verify data integrity and completeness
- Set up feature engineering pipeline

#### Step 3.1.2: Baseline Feature Set Creation
- Standardize/normalize sensor measurements
- Create basic operational setting features
- Establish baseline feature matrix
- Document baseline feature characteristics

### Phase 3.2: Temporal Feature Engineering
**Objective**: Extract time-based features capturing degradation patterns

#### Step 3.2.1: Time-Based Features
- Create relative time features (cycles from start)
- Generate time until failure features (for training)
- Calculate cycle-based ratios and percentages
- Add temporal binning features (early/mid/late lifecycle)

#### Step 3.2.2: Rolling Window Features
- Implement rolling mean features (windows: 5, 10, 20 cycles)
- Create rolling standard deviation features
- Generate rolling min/max features
- Calculate rolling trend features (slope indicators)

#### Step 3.2.3: Lag and Lead Features
- Create lagged sensor values (1, 3, 5 cycles back)
- Generate sensor differences (current - previous)
- Calculate rate of change features
- Implement cumulative change features

### Phase 3.3: Statistical Feature Engineering
**Objective**: Create statistical features capturing sensor behavior patterns

#### Step 3.3.1: Distributional Features
- Calculate per-engine sensor percentiles
- Generate statistical moments (skewness, kurtosis)
- Create per-engine coefficient of variation
- Implement sensor stability measures

#### Step 3.3.2: Cross-Sensor Features
- Create sensor interaction terms (products, ratios)
- Generate principal component features
- Calculate sensor correlation features
- Implement composite degradation indices

#### Step 3.3.3: Degradation Pattern Features
- Create monotonic trend indicators
- Generate degradation acceleration features
- Calculate sensor deviation from initial values
- Implement anomaly score features

### Phase 3.4: Domain-Specific Feature Engineering
**Objective**: Create aviation domain-specific features based on sensor types

#### Step 3.4.1: Engine Performance Features
- Create efficiency-related combinations
- Generate temperature differential features
- Calculate pressure ratio features
- Implement vibration-based health indicators

#### Step 3.4.2: Operational Context Features
- Enhance operational setting features
- Create operational regime indicators
- Generate load-based features
- Calculate operational stress indicators

#### Step 3.4.3: Health Index Features
- Create composite health scores
- Generate remaining life indicators
- Calculate degradation severity measures
- Implement multi-sensor health indices

### Phase 3.5: Feature Selection and Validation
**Objective**: Select optimal feature set and validate engineering quality

#### Step 3.5.1: Feature Importance Assessment
- Calculate feature-target correlations
- Perform mutual information analysis
- Assess feature stability across engines
- Rank features by predictive potential

#### Step 3.5.2: Multicollinearity Management
- Identify highly correlated feature groups
- Apply variance inflation factor analysis
- Remove redundant features
- Optimize feature set for modeling

#### Step 3.5.3: Feature Set Validation
- Validate features on sample engines
- Check for data leakage in temporal features
- Ensure feature consistency across train/test
- Document final feature set composition

### Phase 3.6: Engineered Data Export
**Objective**: Save engineered features and metadata for modeling

#### Step 3.6.1: Feature Data Export
- Export training data with engineered features
- Save test data with corresponding features
- Store feature engineering parameters
- Create feature transformation pipelines

#### Step 3.6.2: Feature Documentation
- Document all engineered features and rationale
- Create feature engineering metadata
- Provide feature loading and application instructions
- Save feature importance rankings

---

## Task 4: Modeling (`04_modeling.ipynb`)

### Phase 4.1: Modeling Setup and Data Preparation
**Objective**: Prepare modeling environment and load engineered features

#### Step 4.1.1: Environment Setup
- Load engineered features from previous task
- Import modeling libraries (scikit-learn, xgboost, etc.)
- Set up cross-validation framework
- Define evaluation metrics and scoring functions

#### Step 4.1.2: Modeling Data Preparation
- Prepare final training and test datasets
- Handle any remaining preprocessing needs
- Create validation splits for model development
- Set up data loaders for different model types

### Phase 4.2: Baseline Model Development
**Objective**: Establish baseline performance with simple models

#### Step 4.2.1: Linear Regression Baseline
- Implement linear regression model
- Perform feature selection for linear model
- Evaluate baseline performance
- Document linear model characteristics

#### Step 4.2.2: Random Forest Baseline
- Implement random forest regressor
- Tune basic hyperparameters
- Analyze feature importance
- Establish ensemble model baseline

#### Step 4.2.3: Baseline Model Comparison
- Compare baseline model performances
- Analyze prediction patterns and errors
- Identify model strengths and weaknesses
- Select best baseline for comparison

### Phase 4.3: Advanced Model Development
**Objective**: Develop and tune sophisticated models for RUL prediction

#### Step 4.3.1: Gradient Boosting Models
- Implement XGBoost regressor
- Tune hyperparameters using cross-validation
- Implement LightGBM model
- Compare gradient boosting approaches

#### Step 4.3.2: Neural Network Models
- Design multi-layer perceptron architecture
- Implement deep neural network for RUL prediction
- Tune network architecture and parameters
- Apply regularization techniques

#### Step 4.3.3: Time Series Specific Models
- Implement LSTM for sequence modeling
- Design CNN for temporal pattern recognition
- Explore hybrid neural architectures
- Compare temporal modeling approaches

### Phase 4.4: Model Optimization and Selection
**Objective**: Optimize model performance and select best approach

#### Step 4.4.1: Hyperparameter Tuning
- Perform systematic hyperparameter optimization
- Use grid search and random search strategies
- Implement Bayesian optimization where beneficial
- Document optimal parameter settings

#### Step 4.4.2: Ensemble Methods
- Create voting ensemble of best models
- Implement stacking ensemble approach
- Design weighted averaging strategies
- Optimize ensemble composition

#### Step 4.4.3: Model Selection
- Compare all models using consistent validation
- Apply statistical significance testing
- Consider model complexity vs performance trade-offs
- Select final model(s) for evaluation

### Phase 4.5: Model Interpretation and Analysis
**Objective**: Understand model behavior and feature contributions

#### Step 4.5.1: Feature Importance Analysis
- Extract feature importance from tree-based models
- Calculate SHAP values for model interpretation
- Analyze feature contribution patterns
- Identify key predictive features

#### Step 4.5.2: Model Behavior Analysis
- Analyze prediction patterns across engine lifecycles
- Examine model performance by RUL ranges
- Identify prediction biases and limitations
- Document model behavior characteristics

#### Step 4.5.3: Error Analysis
- Analyze prediction errors by engine characteristics
- Identify systematic prediction biases
- Examine residual patterns
- Document model limitations and failure modes

### Phase 4.6: Final Model Export
**Objective**: Save trained models and metadata for evaluation

#### Step 4.6.1: Model Persistence
- Save trained models with all parameters
- Export model preprocessing pipelines
- Store model metadata and configuration
- Create model loading utilities

#### Step 4.6.2: Prediction Generation
- Generate predictions on test set
- Save predictions with confidence intervals
- Export model performance metrics
- Create prediction metadata for evaluation

---

## Task 5: Evaluation (`05_evaluation.ipynb`)

### Phase 5.1: Evaluation Setup and Data Loading
**Objective**: Prepare evaluation environment and load model predictions

#### Step 5.1.1: Environment Setup
- Load test predictions from modeling task
- Import evaluation metrics and visualization libraries
- Load true RUL values for test data
- Set up evaluation framework

#### Step 5.1.2: Prediction Data Preparation
- Align predictions with true RUL values
- Validate prediction data completeness
- Handle any prediction post-processing needs
- Prepare data for comprehensive evaluation

### Phase 5.2: Standard Regression Metrics
**Objective**: Evaluate model performance using standard regression metrics

#### Step 5.2.1: Basic Regression Metrics
- Calculate Mean Absolute Error (MAE)
- Compute Root Mean Square Error (RMSE)
- Calculate R-squared coefficient
- Compute Mean Absolute Percentage Error (MAPE)

#### Step 5.2.2: Distribution-Based Metrics
- Analyze prediction error distributions
- Calculate prediction bias and variance
- Compute prediction interval coverage
- Assess prediction uncertainty quality

#### Step 5.2.3: Comparative Performance Analysis
- Compare metrics across different models
- Perform statistical significance testing
- Rank models by different metric criteria
- Document metric-based model performance

### Phase 5.3: Domain-Specific Evaluation
**Objective**: Evaluate models using prognostics-specific metrics

#### Step 5.3.1: PHM Challenge Scoring Function
- Implement asymmetric exponential penalty function
- Calculate PHM'08 challenge scores
- Compare model scores to literature benchmarks
- Analyze penalty distribution across predictions

#### Step 5.3.2: Prognostics-Specific Metrics
- Calculate Prognostic Horizon (PH)
- Compute Mean Time Between False Alarms
- Calculate Probability of Detection rates
- Assess early vs late prediction penalties

#### Step 5.3.3: Business Impact Metrics
- Estimate maintenance cost implications
- Calculate safety margin compliance
- Assess operational disruption potential
- Evaluate model practical utility

### Phase 5.4: Detailed Error Analysis
**Objective**: Understand model prediction patterns and failure modes

#### Step 5.4.1: Prediction Error Patterns
- Analyze errors by true RUL ranges
- Examine prediction biases across engine lifecycles
- Identify systematic error patterns
- Visualize prediction vs actual relationships

#### Step 5.4.2: Engine-Specific Analysis
- Analyze prediction quality per test engine
- Identify engines with poor predictions
- Examine engine characteristics affecting performance
- Document engine-level prediction patterns

#### Step 5.4.3: Feature Impact on Predictions
- Correlate prediction errors with feature values
- Identify features contributing to prediction failures
- Analyze feature importance vs prediction quality
- Document feature-performance relationships

### Phase 5.5: Model Robustness Assessment
**Objective**: Assess model reliability and generalization capability

#### Step 5.5.1: Prediction Consistency Analysis
- Assess prediction stability across similar engines
- Analyze model sensitivity to input variations
- Evaluate prediction confidence calibration
- Test model robustness to data perturbations

#### Step 5.5.2: Generalization Assessment
- Compare performance across different engine subgroups
- Analyze model behavior on edge cases
- Assess prediction quality for different operational conditions
- Evaluate model limitations and failure boundaries

#### Step 5.5.3: Model Reliability Metrics
- Calculate prediction confidence metrics
- Assess model uncertainty quantification
- Evaluate prediction interval reliability
- Document model reliability characteristics

### Phase 5.6: Final Results and Recommendations
**Objective**: Summarize evaluation results and provide recommendations

#### Step 5.6.1: Comprehensive Results Summary
- Summarize all evaluation metrics and findings
- Compare final model performance to baselines
- Document model strengths and limitations
- Create comprehensive performance dashboard

#### Step 5.6.2: Model Deployment Recommendations
- Provide model selection recommendations
- Document deployment considerations
- Suggest monitoring and maintenance strategies
- Outline model update and retraining procedures

#### Step 5.6.3: Future Work and Improvements
- Identify areas for model improvement
- Suggest additional features or data sources
- Recommend advanced modeling techniques
- Document lessons learned and best practices

---

## Data Flow Between Tasks

### Saved Data Files
- **Task 1 → Task 2**: `01_exploration_insights.json`, `01_data_quality_report.json`
- **Task 2 → Task 3**: `02_cleaned_train.parquet`, `02_cleaned_test.parquet`, `02_normalization_params.json`
- **Task 3 → Task 4**: `03_engineered_train.parquet`, `03_engineered_test.parquet`, `03_feature_metadata.json`
- **Task 4 → Task 5**: `04_trained_models/`, `04_test_predictions.parquet`, `04_model_metadata.json`

### Documentation Files
Each task creates corresponding `.md` files documenting:
- Data file structure and loading instructions
- Processing steps and parameters
- Key findings and recommendations
- Usage instructions for subsequent tasks

## Success Criteria
- **Data Quality**: Clean, well-structured datasets with proper validation
- **Feature Engineering**: Meaningful features capturing degradation patterns
- **Model Performance**: PHM'08 challenge score < 500 (competitive benchmark)
- **Evaluation Depth**: Comprehensive analysis of model behavior and limitations
- **Reproducibility**: Full documentation and code for replication
- **Business Value**: Actionable insights for aircraft maintenance optimization
