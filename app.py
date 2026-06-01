import streamlit as st
from hello import Bank

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)

# ================= CREATE ACCOUNT =================

if menu == "Create Account":

    st.header("Create New Account")

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        step=1
    )

    email = st.text_input("Email")

    pin = st.text_input(
        "4 Digit PIN",
        type="password"
    )

    if st.button("Create Account"):

        if not pin.isdigit():
            st.error("PIN should contain digits only")

        else:

            user, msg = Bank.create_account(
                name,
                age,
                email,
                int(pin)
            )

            if user:

                st.success("Account Created Successfully")

                st.info(
                    f"Your Account Number: {user['accountNo.']}"
                )

                st.json(user)

            else:
                st.error(msg)

# ================= DEPOSIT =================

elif menu == "Deposit Money":

    st.header("Deposit Money")

    acc = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    amount = st.number_input(
        "Amount",
        min_value=1
    )

    if st.button("Deposit"):

        if pin.isdigit():

            status = Bank.deposit(
                acc,
                int(pin),
                amount
            )

            if status:
                st.success("Money Deposited Successfully")

            else:
                st.error("Invalid Account Number or PIN")

# ================= WITHDRAW =================

elif menu == "Withdraw Money":

    st.header("Withdraw Money")

    acc = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    amount = st.number_input(
        "Amount",
        min_value=1
    )

    if st.button("Withdraw"):

        if pin.isdigit():

            result = Bank.withdraw(
                acc,
                int(pin),
                amount
            )

            if result == "success":

                st.success(
                    "Money Withdrawn Successfully"
                )

            elif result == "insufficient":

                st.error(
                    "Insufficient Balance"
                )

            else:

                st.error(
                    "Invalid Account Number or PIN"
                )

# ================= SHOW DETAILS =================

elif menu == "Show Details":

    st.header("Account Details")

    acc = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    if st.button("Show Details"):

        if pin.isdigit():

            userdata = Bank.find_user(
                acc,
                int(pin)
            )

            if userdata:

                st.json(userdata[0])

            else:

                st.error(
                    "Invalid Account Number or PIN"
                )

# ================= UPDATE DETAILS =================

elif menu == "Update Details":

    st.header("Update Details")

    acc = st.text_input("Account Number")

    pin = st.text_input(
        "Current PIN",
        type="password"
    )

    name = st.text_input(
        "New Name (Optional)"
    )

    email = st.text_input(
        "New Email (Optional)"
    )

    new_pin = st.text_input(
        "New PIN (Optional)",
        type="password"
    )

    if st.button("Update Details"):

        if not pin.isdigit():
            st.error("Invalid PIN")

        else:

            npin = None

            if new_pin:

                if new_pin.isdigit():
                    npin = int(new_pin)

            status = Bank.update_details(
                acc,
                int(pin),
                name,
                email,
                npin
            )

            if status:

                st.success(
                    "Details Updated Successfully"
                )

            else:

                st.error(
                    "Invalid Account Number or PIN"
                )

# ================= DELETE ACCOUNT =================

elif menu == "Delete Account":

    st.header("Delete Account")

    acc = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    confirm = st.checkbox(
        "I want to delete my account"
    )

    if st.button("Delete Account"):

        if confirm:

            status = Bank.delete_account(
                acc,
                int(pin)
            )

            if status:

                st.success(
                    "Account Deleted Successfully"
                )

            else:

                st.error(
                    "Invalid Account Number or PIN"
                )

        else:

            st.warning(
                "Please confirm deletion"
            )