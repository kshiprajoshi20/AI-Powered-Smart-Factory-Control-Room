# 🤖AI-Powered-Smart-Factory-Control-Room
Industrial Digital Twin &amp; Machine Failure Diagnosis System using Machine Learning
An AI-powered predictive maintenance system designed to monitor industrial machine parameters, predict possible machine failures, assess machine health, and provide maintenance recommendations through an interactive control-room dashboard.

---
## 📌 Project Overview

This project implements a **machine failure prediction and monitoring system** for industrial machines using Machine Learning.

The system takes important machine operating parameters as input and uses a trained machine learning model to predict whether the machine is likely to experience a failure.

The project provides an interactive **Streamlit-based Smart Factory Control Room** where users can enter machine parameters and observe the predicted machine condition.

The system provides:

- **Machine health condition**
- **Failure probability**
- **Machine health score**
- **Risk assessment**
- **Maintenance recommendation**
- **Graphical analysis of machine parameters**

The project is developed using the **AI4I 2020 Predictive Maintenance Dataset**.

---

## 🎯 Objectives

The main objectives of this project are:

- To predict possible machine failures before they occur.
- To monitor important industrial machine parameters.
- To calculate an estimated machine health score.
- To determine the probability of machine failure.
- To identify different levels of machine risk.
- To provide suitable maintenance recommendations.
- To develop an interactive industrial monitoring dashboard.
- To demonstrate the application of Machine Learning in predictive maintenance.

---

## ⚙️ Machine Parameters

The prediction system uses the following machine parameters:

| Parameter | Unit | Description |
|---|---|---|
| Air Temperature | K | Temperature of the surrounding air |
| Process Temperature | K | Temperature of the machine process |
| Rotational Speed | RPM | Rotational speed of the machine |
| Torque | Nm | Torque applied to the machine |
| Tool Wear | min | Operating time/wear of the machine tool |

These parameters are provided as inputs to the trained machine learning model.

---

## 🤖 Machine Learning Prediction

The trained Machine Learning model analyzes the machine parameters and predicts the condition of the machine.

### Prediction Output

The system provides one of the following conditions:

- 🟢 **Machine Healthy**
- 🔴 **Machine Failure Predicted**

Along with the prediction, the dashboard displays:

- Machine Health Score
- Failure Risk
- Risk Level
- Maintenance Recommendation

---

## 🏥 Machine Health Score

The system calculates a machine health score based on the predicted probability of the machine being healthy.

The score is displayed as a percentage on the dashboard.

### Risk Assessment

| Health Score | Risk Level |
|---|---|
| Above 80% | 🟢 LOW RISK |
| 51% – 80% | 🟡 MEDIUM RISK |
| 50% or below | 🔴 HIGH RISK |

This provides a simple way for users to understand the current machine condition.

---

## 🚨 Maintenance Recommendation

The system provides maintenance recommendations based on abnormal machine operating conditions.

For example:

- 🌡️ High air temperature → **Inspect cooling system**
- 🔧 High tool wear → **Replace or inspect the tool**
- ⚙️ High torque → **Inspect motor load condition**
- ✅ Normal operating conditions → **No immediate maintenance required**

These recommendations help the user identify possible maintenance requirements at an early stage.

---

## 📊 Interactive Dashboard

The project uses **Streamlit** to create an interactive Smart Factory Control Room.

The dashboard contains:

### Control Room

- 🎯 Model accuracy
- 🏭 Number of machines
- ⚠️ Failure types
- 🟢 System status

### Machine Parameters

Users can enter:

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

### Prediction Section

After clicking the **Predict** button, the system displays:

- Machine condition
- Machine health score
- Failure risk
- Risk assessment
- Maintenance recommendation

### Dataset Analysis

The dashboard also provides graphical analysis of machine operating parameters to help understand the dataset and machine conditions.

---

## 🔄 System Workflow


                Machine Parameters
                       │
                       ▼
                Data Input
                       │
                       ▼
              Data Preprocessing
                       │
                       ▼
             Machine Learning Model
                       │
                       ▼
              Failure Prediction
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      Machine Healthy      Failure Predicted
             │                   │
             └─────────┬─────────┘
                       ▼
              Health Score &
               Failure Risk
                       │
                       ▼
               Risk Assessment
                       │
                       ▼
           Maintenance Recommendation


## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries and Frameworks

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

### Machine Learning

- Supervised Machine Learning
- Classification
- Predictive Maintenance

### Development Tools

- Visual Studio Code
- Git
- GitHub
- GitHub Desktop


## 📁 Project Structure

```text
AI-Powered-Smart-Factory-Control-Room/
│
├── Dataset/
│   └── ai4i2020.csv
│
├── Images/
│
├── models/
│   └── model.pkl
│
├── analysis.py
├── app.py
├── check_data.py
├── missing_values.py
├── save_model.py
├── train_model.py
└── README.md
```


## 📌 Conclusion

The **AI-Powered Smart Factory Control Room** demonstrates how Machine Learning can be applied to predictive maintenance and industrial machine monitoring.
By analyzing machine parameters such as temperature, rotational speed, torque, and tool wear, the system predicts the possibility of machine failure and provides a simple health and risk assessment.
The interactive Streamlit dashboard makes the system easy to use and provides a foundation for developing a more advanced **Industrial Digital Twin and Smart Factory monitoring system**.



## 👩‍💻 Developed By
**Kshipra Kshitij Joshi**

**AI-Powered Smart Factory Control Room**

*Industrial Digital Twin & Machine Failure Diagnosis System using Machine Learning*
