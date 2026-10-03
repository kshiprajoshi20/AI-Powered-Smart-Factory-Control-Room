import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# ==========================================================
# LOAD DATASET AND MODEL
# ==========================================================

df = pd.read_csv("Dataset/ai4i2020.csv")
model = joblib.load("models/model.pkl")


# ==========================================================
# PAGE SETTINGS
# ==========================================================

st.set_page_config(
    page_title="🏭 AI-Powered Smart Factory Control Room",
    page_icon="⚙️",
    layout="wide"
)


# ==========================================================
# TITLE
# ==========================================================

st.title("🏭 AI-Powered Smart Factory Control Room")
st.write("Industrial Digital Twin & Failure Diagnosis System")

st.markdown("---")


# ==========================================================
# DASHBOARD METRICS
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🎯 Accuracy", "99.9%")

with col2:
    st.metric("🏭 Machines", "10000")

with col3:
    st.metric("⚠ Failure Types", "5")

with col4:
    st.metric("🟢 Status", "ACTIVE")

st.markdown("---")


# ==========================================================
# MACHINE PARAMETERS
# ==========================================================

st.header("⚙️ Machine Parameters")

col_input1, col_input2, col_input3, col_input4, col_input5 = st.columns(5)

with col_input1:
    air_temp = st.number_input(
        "Air Temperature [K]",
        min_value=250.0,
        max_value=400.0,
        value=300.0,
        step=1.0
    )

with col_input2:
    process_temp = st.number_input(
        "Process Temperature [K]",
        min_value=250.0,
        max_value=450.0,
        value=310.0,
        step=1.0
    )

with col_input3:
    rpm = st.number_input(
        "Rotational Speed [RPM]",
        min_value=0,
        max_value=5000,
        value=1500,
        step=50
    )

with col_input4:
    torque = st.number_input(
        "Torque [Nm]",
        min_value=0.0,
        max_value=100.0,
        value=40.0,
        step=1.0
    )

with col_input5:
    tool_wear = st.number_input(
        "Tool Wear [min]",
        min_value=0,
        max_value=300,
        value=50,
        step=5
    )


# ==========================================================
# PREDICTION
# ==========================================================

if st.button("🔮 Predict Machine Status", use_container_width=True):

    input_data = pd.DataFrame({
        "Air temperature [K]": [air_temp],
        "Process temperature [K]": [process_temp],
        "Rotational speed [rpm]": [rpm],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear]
    })

    # Model prediction
    prediction = model.predict(input_data)

    # Prediction probability
    probability = model.predict_proba(input_data)

    healthy_probability = probability[0][0] * 100
    failure_probability = probability[0][1] * 100

    health_score = round(healthy_probability)

    # Store values for graphs
    st.session_state["predicted"] = True
    st.session_state["health_score"] = health_score
    st.session_state["failure_probability"] = failure_probability
    st.session_state["prediction"] = prediction[0]

    # ------------------------------------------------------
    # MACHINE STATUS
    # ------------------------------------------------------

    if prediction[0] == 1:
        st.error("⚠️ Machine Failure Predicted")
    else:
        st.success("✅ Machine Healthy")

    # ------------------------------------------------------
    # MACHINE HEALTH SCORE
    # ------------------------------------------------------

    st.subheader("🏥 Machine Health Score")

    st.progress(
        min(max(int(health_score), 0), 100)
    )

    colA, colB = st.columns(2)

    with colA:
        st.metric(
            "Machine Health",
            f"{health_score}%"
        )

    with colB:
        st.metric(
            "Failure Risk",
            f"{failure_probability:.1f}%"
        )

    # ------------------------------------------------------
    # RISK ASSESSMENT
    # ------------------------------------------------------

    st.subheader("🚨 Risk Assessment")

    if health_score > 80:
        st.success("🟢 LOW RISK")

    elif health_score > 50:
        st.warning("🟡 MEDIUM RISK")

    else:
        st.error("🔴 HIGH RISK")

    # ------------------------------------------------------
    # MAINTENANCE RECOMMENDATION
    # ------------------------------------------------------

    st.subheader("🔧 Maintenance Recommendation")

    if air_temp > 330:

        st.warning(
            "🌡️ High air temperature detected. "
            "Inspect cooling system immediately."
        )

    elif process_temp > 350:

        st.warning(
            "🌡️ High process temperature detected. "
            "Check thermal conditions."
        )

    elif tool_wear > 200:

        st.warning(
            "🛠️ High tool wear detected. "
            "Replace tool within 48 hours."
        )

    elif torque > 65:

        st.warning(
            "⚙️ High torque detected. "
            "Inspect motor load condition."
        )

    elif rpm > 2500:

        st.warning(
            "⚙️ High rotational speed detected. "
            "Inspect motor operating condition."
        )

    else:

        st.success(
            "✅ Machine operating within normal conditions. "
            "No immediate maintenance required."
        )


# ==========================================================
# INTERACTIVE DATASET ANALYSIS
# ==========================================================

st.markdown("---")
st.header("📊 Interactive Machine Analysis")

st.caption(
    "The distribution represents the historical dataset. "
    "The red marker shows the current machine input."
)


# ==========================================================
# GRAPH 1 - AIR TEMPERATURE
# ==========================================================

col3, col4 = st.columns(2)

with col3:

    fig1, ax1 = plt.subplots(figsize=(5.5, 3.5))

    sns.histplot(
        df["Air temperature [K]"],
        bins=25,
        kde=True,
        color="#3498DB",
        edgecolor="white",
        alpha=0.75,
        ax=ax1
    )

    ax1.axvline(
        air_temp,
        color="#E74C3C",
        linewidth=2.5,
        linestyle="--",
        label=f"Your Input: {air_temp:.0f} K"
    )

    ax1.set_title(
        "Air Temperature",
        fontsize=13,
        fontweight="bold"
    )

    ax1.set_xlabel("Air Temperature [K]")
    ax1.set_ylabel("Number of Machines")

    ax1.grid(
        axis="y",
        linestyle="--",
        alpha=0.25
    )

    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    ax1.legend(fontsize=8)

    plt.tight_layout()

    st.pyplot(
        fig1,
        use_container_width=True
    )

    plt.close(fig1)


# ==========================================================
# GRAPH 2 - PROCESS TEMPERATURE
# ==========================================================

with col4:

    fig2, ax2 = plt.subplots(figsize=(5.5, 3.5))

    sns.histplot(
        df["Process temperature [K]"],
        bins=25,
        kde=True,
        color="#9B59B6",
        edgecolor="white",
        alpha=0.75,
        ax=ax2
    )

    ax2.axvline(
        process_temp,
        color="#E74C3C",
        linewidth=2.5,
        linestyle="--",
        label=f"Your Input: {process_temp:.0f} K"
    )

    ax2.set_title(
        "Process Temperature",
        fontsize=13,
        fontweight="bold"
    )

    ax2.set_xlabel("Process Temperature [K]")
    ax2.set_ylabel("Number of Machines")

    ax2.grid(
        axis="y",
        linestyle="--",
        alpha=0.25
    )

    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    ax2.legend(fontsize=8)

    plt.tight_layout()

    st.pyplot(
        fig2,
        use_container_width=True
    )

    plt.close(fig2)


# ==========================================================
# GRAPH 3 - ROTATIONAL SPEED
# ==========================================================

col5, col6 = st.columns(2)

with col5:

    fig3, ax3 = plt.subplots(figsize=(5.5, 3.5))

    sns.histplot(
        df["Rotational speed [rpm]"],
        bins=25,
        kde=True,
        color="#F39C12",
        edgecolor="white",
        alpha=0.75,
        ax=ax3
    )

    ax3.axvline(
        rpm,
        color="#E74C3C",
        linewidth=2.5,
        linestyle="--",
        label=f"Your Input: {rpm} RPM"
    )

    ax3.set_title(
        "Rotational Speed",
        fontsize=13,
        fontweight="bold"
    )

    ax3.set_xlabel("Rotational Speed [RPM]")
    ax3.set_ylabel("Number of Machines")

    ax3.grid(
        axis="y",
        linestyle="--",
        alpha=0.25
    )

    ax3.spines["top"].set_visible(False)
    ax3.spines["right"].set_visible(False)

    ax3.legend(fontsize=8)

    plt.tight_layout()

    st.pyplot(
        fig3,
        use_container_width=True
    )

    plt.close(fig3)


# ==========================================================
# GRAPH 4 - TORQUE
# ==========================================================

with col6:

    fig4, ax4 = plt.subplots(figsize=(5.5, 3.5))

    sns.histplot(
        df["Torque [Nm]"],
        bins=25,
        kde=True,
        color="#1ABC9C",
        edgecolor="white",
        alpha=0.75,
        ax=ax4
    )

    ax4.axvline(
        torque,
        color="#E74C3C",
        linewidth=2.5,
        linestyle="--",
        label=f"Your Input: {torque:.1f} Nm"
    )

    ax4.set_title(
        "Torque",
        fontsize=13,
        fontweight="bold"
    )

    ax4.set_xlabel("Torque [Nm]")
    ax4.set_ylabel("Number of Machines")

    ax4.grid(
        axis="y",
        linestyle="--",
        alpha=0.25
    )

    ax4.spines["top"].set_visible(False)
    ax4.spines["right"].set_visible(False)

    ax4.legend(fontsize=8)

    plt.tight_layout()

    st.pyplot(
        fig4,
        use_container_width=True
    )

    plt.close(fig4)


# ==========================================================
# MACHINE HEALTH & FAILURE RISK
# ==========================================================

st.markdown("---")
st.subheader("🩺 Machine Health Overview")


# Default values before prediction
if "health_score" in st.session_state:

    current_health = st.session_state["health_score"]
    current_failure = st.session_state["failure_probability"]

else:

    current_health = 100
    current_failure = 0


col_health, col_risk = st.columns(2)


# ==========================================================
# GRAPH 5 - MACHINE HEALTH
# ==========================================================

with col_health:

    fig5, ax5 = plt.subplots(figsize=(5.5, 3.2))

    ax5.barh(
        ["Machine Health"],
        [current_health],
        color="#2ECC71",
        height=0.35
    )

    ax5.set_xlim(0, 100)

    ax5.set_xlabel(
        "Health Score (%)"
    )

    ax5.set_title(
        "Machine Health Score",
        fontsize=13,
        fontweight="bold"
    )

    ax5.text(
        min(current_health + 2, 95),
        0,
        f"{current_health}%",
        va="center",
        fontsize=11,
        fontweight="bold"
    )

    ax5.grid(
        axis="x",
        linestyle="--",
        alpha=0.25
    )

    ax5.spines["top"].set_visible(False)
    ax5.spines["right"].set_visible(False)
    ax5.spines["left"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig5,
        use_container_width=True
    )

    plt.close(fig5)


# ==========================================================
# GRAPH 6 - FAILURE RISK
# ==========================================================

with col_risk:

    fig6, ax6 = plt.subplots(figsize=(5.5, 3.2))

    ax6.barh(
        ["Failure Risk"],
        [current_failure],
        color="#E74C3C",
        height=0.35
    )

    ax6.set_xlim(0, 100)

    ax6.set_xlabel(
        "Failure Probability (%)"
    )

    ax6.set_title(
        "Machine Failure Risk",
        fontsize=13,
        fontweight="bold"
    )

    ax6.text(
        min(current_failure + 2, 95),
        0,
        f"{current_failure:.1f}%",
        va="center",
        fontsize=11,
        fontweight="bold"
    )

    ax6.grid(
        axis="x",
        linestyle="--",
        alpha=0.25
    )

    ax6.spines["top"].set_visible(False)
    ax6.spines["right"].set_visible(False)
    ax6.spines["left"].set_visible(False)

    plt.tight_layout()

    st.pyplot(
        fig6,
        use_container_width=True
    )

    plt.close(fig6)


# ==========================================================
# CURRENT MACHINE SUMMARY
# ==========================================================

st.markdown("---")
st.subheader("📋 Current Machine Parameters")

summary_col1, summary_col2, summary_col3, summary_col4, summary_col5 = st.columns(5)

with summary_col1:
    st.metric(
        "Air Temperature",
        f"{air_temp:.1f} K"
    )

with summary_col2:
    st.metric(
        "Process Temperature",
        f"{process_temp:.1f} K"
    )

with summary_col3:
    st.metric(
        "Rotational Speed",
        f"{rpm} RPM"
    )

with summary_col4:
    st.metric(
        "Torque",
        f"{torque:.1f} Nm"
    )

with summary_col5:
    st.metric(
        "Tool Wear",
        f"{tool_wear} min"
    )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.write(
    " Developed by Kshipra Joshi"
)