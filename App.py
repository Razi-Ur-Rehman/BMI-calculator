import streamlit as st


def bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)


def category(bmi_value: float) -> str:
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"

# --- CSS ---
st.markdown(
    """
    <style>
    body {background-color:#001f3f;}
    .stApp {background-color:#001f3f;}
    .stTextInput>div>div>input {background-color:#0b2d52;color:white;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("BMI Calculator — Streamlit Edition (Navy UI)")

w = st.number_input("Weight (kg)", min_value=0.1, format="%.2f")
h = st.number_input("Height (meters)", min_value=0.1, format="%.2f")

if st.button("Compute"):
    val = bmi(w, h)
    st.write(f"BMI = {val:.2f}")
    st.write("Category:", category(val))

    # number line plot
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7, 1.2))
    ax.set_xlim(10, 40)
    ax.set_ylim(0, 1)
    ax.axvline(val, linewidth=6)
    ax.set_yticks([])
    ax.set_xlabel("BMI scale 10 → 40")

    st.pyplot(fig)
