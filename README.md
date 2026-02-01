# IoT Sensor Fault Detection Model 🏭

## 📌 Overview
This project implements a Machine Learning solution for **Predictive Maintenance** in manufacturing. It analyzes time-series data from IoT sensors (Vibration and Temperature) to detect equipment faults such as overheating drifts and abnormal vibration spikes.

## 🛠️ Technologies Used
* **Python 3.x**
* **Pandas** (Data manipulation & Time-series analysis)
* **Scikit-Learn** (Model training & Evaluation)
* **Matplotlib/Seaborn** (Data Visualization)

## 📂 Project Structure
* `sensor_data.csv`: Synthetic dataset mimicking industrial sensor readings.
* `fault_detection_model.ipynb`: Jupyter Notebook containing the full pipeline (Data Generation → EDA → Modeling → Evaluation).
* `README.md`: Project documentation.

## 🚀 Key Features
1.  **Synthetic Data Generation:** Simulates realistic sensor behavior including Gaussian noise, linear drifts, and variance spikes.
2.  **Robust Preprocessing:** Handles missing values using Forward-Fill imputation suitable for time-series.
3.  **Feature Engineering:** Calculates **Rolling Mean** and **Rolling Std Dev** to capture trends and volatility.
4.  **Binary Classification:** Uses a **Random Forest Classifier** to predict `Normal` (0) vs `Fault` (1) states.

## 📊 Model Performance
The model was evaluated on a held-out test set (20% split) using Stratified Sampling.

| Metric | Score (Approx) | Description |
| :--- | :--- | :--- |
| **Accuracy** | ~99% | Overall correctness of predictions. |
| **Precision** | High | Minimizes false alarms (stopping production unnecessarily). |
| **Recall** | High | Minimizes missed faults (preventing catastrophic failure). |

## 🔧 How to Run
1.  **Install Dependencies:**
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn
    ```
2.  **Run the Notebook:**
    Open `fault_detection_model.ipynb` in Jupyter or Google Colab and execute the cells sequentially.

## 📈 Visuals
The project includes Exploratory Data Analysis (EDA) plots visualizing:
* Normal operating zones (Blue)
* Detected Fault zones (Red) for both Temperature and Vibration sensors.

---
*Created as a Mini-Project for IoT Predictive Maintenance.*
