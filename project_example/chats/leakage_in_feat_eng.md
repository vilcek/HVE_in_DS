vilcek: I see the column `time_to_end` being created for both training and test sets, as part of step 3.2.1. 

It looks like this is a case of a direct leakage from the target variable, `RUL`. That column is not used anywhere else, as part of any other feature computation. THus I think it is safe to assume we don't need it.

GitHub Copilot: I'll examine the current notebook to understand the `time_to_end` column creation and remove it since it represents data leakage. Let me first look at the current state of the notebook. Now let me look at the specific area around line 181-216 where the user mentioned the `time_to_end` column creation: Let me continue reading to see the full context of where `time_to_end` is being created for the test data: Now let me search for all usages of `time_to_end` in the notebook to understand if it's used elsewhere: Perfect! I can see that `time_to_end` is indeed a direct copy of the `RUL` column, which represents clear data leakage. The column is created in two places:

1. For training data: `train_features['time_to_end'] = train_features['RUL']`
2. For test data: `test_features['time_to_end'] = test_features['RUL']`

And it's only mentioned in the print statement describing the new columns. Let me remove these lines to eliminate the data leakage. 

Made changes.

Made changes.

Made changes.

Perfect! I've successfully removed the `time_to_end` column creation from both the training and test data sections of the feature engineering notebook. This eliminates the data leakage issue you identified.

## Summary of changes made:

1. **Removed from training data cell**: The line `train_features['time_to_end'] = train_features['RUL']` has been removed
2. **Removed from test data cell**: The line `test_features['time_to_end'] = test_features['RUL']` has been removed  
3. **Updated print statements**: Removed `time_to_end` from the list of new columns being created

The `time_to_end` feature was indeed a direct copy of the `RUL` target variable, which would have given the model perfect information about what it's trying to predict - a clear case of data leakage. By removing this feature, the model will now have to rely on legitimate temporal patterns and sensor readings to predict the remaining useful life, which is the intended challenge.

The remaining temporal features (`cycle_norm`, `time_since_start`, `lifecycle_position`, and `total_cycles`) are all legitimate features that can be derived from the available operational data without knowing the true RUL.