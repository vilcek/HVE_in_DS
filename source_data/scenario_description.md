### ✅ **Proposed Problem to Be Solved**

The core problem is to **predict the Remaining Useful Life (RUL)** of aircraft gas turbine engines using multivariate time series data. This falls under the field of **prognostics**, specifically the estimation of how many operational cycles remain before engine failure.

The challenge was motivated by the **lack of real-world run-to-failure data**, which makes it difficult to develop and benchmark prognostic algorithms. Therefore, synthetic data was generated using a high-fidelity engine simulation (C-MAPSS) to mimic realistic degradation processes.

Participants in the PHM 2008 data challenge were tasked to:

* Use historical sensor data from engines to **predict RUL**.
* Develop data-driven prognostic models without relying on the underlying physical models.

---

### ✅ **Dataset Provided**

The data folder is `source_data`.
The datasets are divided into four cases (FD001–FD004), described in the `readme.txt`:

| **Dataset** | **Train trajectories** | **Test trajectories** | **Conditions**           | **Fault Modes**                                  |
| ----------- | ---------------------- | --------------------- | ------------------------ | ------------------------------------------------ |
| FD001       | 100                    | 100                   | One (sea level)          | One (High-Pressure Compressor (HPC) degradation) |
| FD002       | 260                    | 259                   | Six operating conditions | One (HPC degradation)                            |
| FD003       | 100                    | 100                   | One (sea level)          | Two (HPC + Fan degradation)                      |
| FD004       | 248                    | 249                   | Six operating conditions | Two (HPC + Fan degradation)                      |

Key characteristics:

* Each engine has its **own multivariate time series** with operational settings and sensor measurements.
* Data include **26 columns**: unit number, time (cycles), three operational settings, and 22 sensor readings.
* **Training sets** go until failure; **test sets** are truncated before failure.
* The goal is to **predict the RUL** (i.e., how many cycles remain) for each engine in the test set.
* True RUL values are provided for evaluating predictions.

---

### ✅ **Model Evaluation Approach**

Models are evaluated based on:

1. **Prediction accuracy of RUL** for each engine in the test set.

2. **Scoring function** used in the PHM’08 challenge:

   * Asymmetric exponential penalty:

     * Early predictions are penalized less.
     * Late predictions are penalized more heavily.
   * Formula (simplified form):

     $$
     s = \sum_{i=1}^n \begin{cases}
     \exp\left(-\frac{d_i}{\alpha_1}\right), & \text{if } d_i < 0 \\
     \exp\left(\frac{d_i}{\alpha_2}\right), & \text{if } d_i \geq 0
     \end{cases}
     $$

     where $d_i = \text{estimated RUL} - \text{true RUL}$, and $\alpha_1, \alpha_2$ are penalty constants.

3. **Correlation metrics** (suggested for future improvement):

   * To capture consistency across units under test (UUTs).
   * To distinguish between models that predict well on average vs. consistently.

---

### ✅ **Summary**

The challenge provides a **realistic simulated degradation dataset** for developing data-driven RUL prediction models. Participants are expected to:

* Build models using **training data**;
* Predict RUL for **test data**;
* Evaluate using provided **true RUL values** and an **asymmetric scoring function** that rewards early, accurate predictions.
