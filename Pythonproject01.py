import streamlit as st

st.set_page_config(page_title="Electronics Engineering Toolkit", page_icon="⚡")
st.title("⚡ Electronics Engineering Toolkit")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Logic Gates", "Number System Converter", "Ohm's Law", "Resistor Color Code"]
)

# =====================================================
# 1. LOGIC GATES  (your original gate functions)
# =====================================================
def and_gate(a, b):
    return a and b
def or_gate(a, b):
    return a or b
def not_gate(a):
    return 1 if a == 0 else 0
def nand_gate(a, b):
    return 0 if a and b == 1 else 1
def nor_gate(a, b):
    return 0 if a or b == 1 else 1
def xor_gate(a, b):
    return 1 if a != b else 0
def xnor_gate(a, b):
    return 1 if a == b else 0

with tab1:
    st.header("Digital Logic Gate Simulator")
    gates = {
        "AND": and_gate, "OR": or_gate, "NOT": not_gate, "NAND": nand_gate,
        "NOR": nor_gate, "XOR": xor_gate, "XNOR": xnor_gate,
    }
    name = st.selectbox("Choose a gate", list(gates.keys()))
    a = st.radio("Binary value of A", [0, 1], horizontal=True)
    if name == "NOT":
        st.success(f"NOT gate output: {not_gate(a)}")
    else:
        b = st.radio("Binary value of B", [0, 1], horizontal=True)
        st.success(f"{name} gate output: {gates[name](a, b)}")

    if st.checkbox("Show truth table"):
        rows = []
        if name == "NOT":
            for a in [0, 1]:
                rows.append({"A": a, "Y": not_gate(a)})
        else:
            for a in [0, 1]:
                for b in [0, 1]:
                    rows.append({"A": a, "B": b, "Y": gates[name](a, b)})
        st.table(rows)

# =====================================================
# 2. NUMBER SYSTEM CONVERTER
# =====================================================
with tab2:
    st.header("Number System Converter")
    options = [
        "Decimal to Binary", "Decimal to Octal", "Decimal to Hexadecimal",
        "Binary to Decimal", "Binary to Octal", "Binary to Hexadecimal",
        "Octal to Decimal", "Octal to Binary",
        "Hexadecimal to Decimal", "Hexadecimal to Binary",
        "1's Complement", "2's Complement",
    ]
    choice = st.selectbox("Choose a conversion", options)
    value = st.text_input("Enter the value")

    if value:
        try:
            if choice == "Decimal to Binary":
                st.success(f"Binary value of {value} is {bin(int(value))[2:]}")
            elif choice == "Decimal to Octal":
                st.success(f"Octal value of {value} is {oct(int(value))[2:]}")
            elif choice == "Decimal to Hexadecimal":
                st.success(f"Hexadecimal value of {value} is {hex(int(value))[2:]}")
            elif choice == "Binary to Decimal":
                st.success(f"Decimal value of {value} is {int(value, 2)}")
            elif choice == "Binary to Octal":
                st.success(f"Octal value of {value} is {oct(int(value, 2))[2:]}")
            elif choice == "Binary to Hexadecimal":
                st.success(f"Hexadecimal value of {value} is {hex(int(value, 2))[2:]}")
            elif choice == "Octal to Decimal":
                st.success(f"Decimal value of {value} is {int(value, 8)}")
            elif choice == "Octal to Binary":
                st.success(f"Binary value of {value} is {bin(int(value, 8))[2:]}")
            elif choice == "Hexadecimal to Decimal":
                st.success(f"Decimal value of {value} is {int(value, 16)}")
            elif choice == "Hexadecimal to Binary":
                st.success(f"Binary value of {value} is {bin(int(value, 16))[2:]}")
            elif choice in ("1's Complement", "2's Complement"):
                int(value, 2)  # checks the input is really binary
                ones = ""
                for bit in value:
                    if bit == "0":          # FIX: was  bit==0  (a text "0" never equals the number 0)
                        ones += "1"
                    else:
                        ones += "0"
                if choice == "1's Complement":
                    st.success(f"1's complement of {value} is {ones}")
                else:
                    twos = bin(int(ones, 2) + 1)
                    st.success(f"2's complement of {value} is {twos[2:]}")
        except ValueError:
            st.error("That value does not match the number system you chose.")

# =====================================================
# 3. OHM'S LAW
# =====================================================
def voltage(current, resistance):
    return current * resistance
def current(voltage, resistance):
    return voltage / resistance
def resistance(voltage, current):
    return voltage / current
def power1(voltage, current):
    return voltage * current
def power2(current, resistance):
    return current ** 2 * resistance
def power3(voltage, resistance):
    return voltage ** 2 / resistance

with tab3:
    st.header("Ohm's Law and Power Calculation")
    calc = st.selectbox("What do you want to find?", [
        "Voltage", "Current", "Resistance", "Power",
        "Resistance in series", "Resistance in parallel"])

    if calc == "Voltage":
        i = st.number_input("Current (A)", value=0.0)
        r = st.number_input("Resistance (ohms)", value=0.0)   # FIX: label said K'ohms but the maths uses ohms
        st.success(f"Voltage = {round(voltage(i, r), 3)} volts")

    elif calc == "Current":
        v = st.number_input("Voltage (V)", value=0.0)
        r = st.number_input("Resistance (ohms)", value=1.0)
        if r > 0:
            st.success(f"Current = {round(current(v, r), 3)} Amps")
        else:
            st.error("Resistance cannot be zero!!")

    elif calc == "Resistance":
        v = st.number_input("Voltage (V)", value=0.0)
        i = st.number_input("Current (A)", value=1.0)
        if i != 0:
            st.success(f"Resistance = {round(resistance(v, i), 2)} ohms")
        else:
            st.error("Current cannot be zero!!")

    elif calc == "Power":
        formula = st.radio("Select formula", ["P=V*I", "P=I**2*R", "P=V**2/R"])
        if formula == "P=V*I":
            v = st.number_input("Voltage (V)", value=0.0)
            i = st.number_input("Current (A)", value=0.0)
            st.success(f"Power = {round(power1(v, i), 3)} watts")
        elif formula == "P=I**2*R":
            i = st.number_input("Current (A)", value=0.0)
            r = st.number_input("Resistance (ohms)", value=0.0)
            st.success(f"Power = {round(power2(i, r), 3)} watts")
        else:
            v = st.number_input("Voltage (V)", value=0.0)
            r = st.number_input("Resistance (ohms)", value=1.0)
            if r > 0:
                st.success(f"Power = {round(power3(v, r), 3)} watts")
            else:
                st.error("Resistance cannot be zero!!")

    elif calc == "Resistance in series":
        n = st.number_input("Number of resistors", min_value=1, value=2, step=1)
        total = 0
        for k in range(int(n)):
            r = st.number_input(f"Resistance R{k+1}", value=0.0, key=f"s{k}")
            total += r
        # FIX: in your code the print/return sat inside the for loop, so it stopped after R1
        st.success(f"Total resistance: {total}")

    elif calc == "Resistance in parallel":
        x = st.number_input("Number of resistors", min_value=1, value=2, step=1)
        total = 0
        zero = False
        for k in range(int(x)):
            r = st.number_input(f"Resistance R{k+1}", value=1.0, key=f"p{k}")
            if r == 0:
                zero = True
            else:
                total += 1 / r        # FIX: in your code this line sat after a break, so it never ran
        if zero:
            st.error("Resistance cannot be zero!!")
        else:
            st.success(f"Equivalent resistance: {round(1 / total, 3)}")

# =====================================================
# 4. RESISTOR COLOR CODE
# =====================================================
with tab4:
    st.header("Resistor Colour Code Calculator (4-band)")
    colors = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
              "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    multiplier = {"black": 1, "brown": 10, "red": 100, "orange": 1000,
                  "yellow": 10000, "green": 100000, "blue": 1000000,
                  "violet": 10000000, "grey": 100000000, "white": 1000000000,
                  "gold": 0.1, "silver": 0.01}
    tolerance = {"brown": "±1%", "red": "±2%", "green": "±0.5%", "blue": "±0.25%",
                 "violet": "±0.1%", "grey": "±0.05%", "gold": "±5%",
                 "silver": "±10%", "none": "±20%"}

    band1 = st.selectbox("1st Band", list(colors.keys()))
    band2 = st.selectbox("2nd Band", list(colors.keys()))
    band3 = st.selectbox("Multiplier Band", list(multiplier.keys()))
    band4 = st.selectbox("Tolerance Band", list(tolerance.keys()))

    value = (colors[band1] * 10 + colors[band2]) * multiplier[band3]
    st.success(f"Resistance Value: {value} ohms {tolerance[band4]}")
