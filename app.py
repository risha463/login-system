import streamlit as st
import hashlib
import time

st.set_page_config(page_title="🔐 Strong Login Pro", page_icon="🔐", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, .stApp {
    background: linear-gradient(135deg, #ffd6e7 0%, #ffc2dc 100%) !important;
    font-family: 'Poppins', sans-serif !important;
}

header, footer, .stDeployButton, #MainMenu {
    visibility: hidden !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
    height: 0rem !important;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
    max-width: 1100px !important;
    background: transparent !important;
}

h1, h2, h3, h4, h5, h6, p, label, span {
    color: #111111 !important;
}

h1 {
    text-align: center;
    font-weight: 700 !important;
    margin-bottom: 0.3rem !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 1rem !important;
    border-bottom: none !important;
}

.stTabs [data-baseweb="tab"] {
    color: #000000 !important;
    font-weight: 700 !important;
    background: transparent !important;
    border-radius: 12px !important;
    padding: 10px 14px !important;
}

.stTabs [aria-selected="true"] {
    color: #000000 !important;
    background: rgba(255,255,255,0.35) !important;
}

[data-testid="stForm"] {
    background: rgba(255,255,255,0.35) !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    border-radius: 22px !important;
    padding: 25px !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08) !important;
    backdrop-filter: blur(10px) !important;
}

[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.85) !important;
    border-radius: 14px !important;
    border: 1px solid #f0b6cc !important;
    color: #111111 !important;
}

[data-testid="stButton"] button {
    background: #ffffff !important;
    color: #000000 !important;
    border: 1px solid #d9a2ba !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    padding: 0.6rem 1.2rem !important;
}

[data-testid="stButton"] button:hover {
    background: #ffe6f0 !important;
    border-color: #c97f9f !important;
}

.success-box {
    background: #d8ffe9 !important;
    color: #0b5d2a !important;
    padding: 14px 16px !important;
    border-radius: 14px !important;
    border: 1px solid #8be0ad !important;
}

.error-box {
    background: #ffe0e8 !important;
    color: #8a1130 !important;
    padding: 14px 16px !important;
    border-radius: 14px !important;
    border: 1px solid #f0a5bc !important;
}
</style>
""", unsafe_allow_html=True)

def make_hash(paswo):
    return hashlib.sha256(paswo.encode()).hexdigest()

if "users" not in st.session_state:
    st.session_state.users = {}
if "attempts" not in st.session_state:
    st.session_state.attempts = {}

st.markdown("""
<div style='text-align: center; margin-bottom: 2rem;'>
    <h1>🔐 Strong Login System Pro</h1>
    <p style='color: #111111; font-size: 1.1rem; font-weight: 500;'>Secure • Fast </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
if st.session_state.users:
    with col1:
        st.metric("👥 Users", len(st.session_state.users))
    with col2:
        st.metric("🔒 Secure", "100%")
    with col3:
        st.metric("⚡ SHA256", "Active")

tab1, tab2 = st.tabs(["📝 Create Account", "🚪 Login"])

with tab1:
    st.subheader("✨ Create New Account")
    with st.form("signup_form"):
        col_a, col_b = st.columns([2, 1])
        with col_a:
            username = st.text_input(
                "👤 Username",
                placeholder="Min 5 chars + Upper/Lower/Number",
                help="Example: RishaGupta123"
            )
        with col_b:
            password = st.text_input(
                "🔑 Password",
                type="password",
                placeholder="Min 8 chars + Special char"
            )

        submit = st.form_submit_button("🚀 Create Account")

        if submit:
            if username == "":
                st.markdown('<div class="error-box">user name can\'t be empty</div>', unsafe_allow_html=True)
            elif len(username) < 5:
                st.markdown('<div class="error-box">username is too short</div>', unsafe_allow_html=True)
            elif username in st.session_state.users:
                st.markdown('<div class="error-box">user name already exists</div>', unsafe_allow_html=True)
            elif "--" in username or "'" in username:
                st.markdown('<div class="error-box">suspicious username 🚫</div>', unsafe_allow_html=True)
            elif not (any(c.isupper() for c in username) and any(c.islower() for c in username) and any(c.isdigit() for c in username)):
                st.markdown('<div class="error-box">Username not valid ❌<br>Must contain uppercase, lowercase and digit</div>', unsafe_allow_html=True)
            elif (len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password)):
                st.session_state.users[username] = make_hash(password)
                st.markdown("""
                <div class="success-box">
                    ✅ Signup successful!<br>
                    <strong>🔐 SHA256 Hash Created</strong>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
                time.sleep(1)
                st.rerun()
            else:
                st.markdown("""
                <div class="error-box">
                    Weak password ❌<br>
                    Needs: 8+ chars, Upper, Lower, Number, Special(#$%)
                </div>
                """, unsafe_allow_html=True)

with tab2:
    st.subheader("🔐 Login Portal")

    if st.session_state.users:
        with st.form("login_form"):
            col_c, col_d = st.columns(2)
            with col_c:
                login_username = st.text_input("👤 Username", key="login_username")
            with col_d:
                login_password = st.text_input("🔑 Password", type="password", key="login_password")

            login_submit = st.form_submit_button("🎯 Login")

            if login_submit:
                attempts = st.session_state.attempts.get(login_username, 0)

                if login_username in st.session_state.users and st.session_state.users[login_username] == make_hash(login_password):
                    st.markdown("""
                    <div class="success-box">
                        🎉 Login successful!<br>
                        <strong>✅ Welcome back!</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    st.session_state.attempts[login_username] = 0
                    time.sleep(1)
                    st.rerun()
                else:
                    attempts += 1
                    st.session_state.attempts[login_username] = attempts
                    st.markdown(f'<div class="error-box">❌ Invalid login (Attempt {attempts}/3)</div>', unsafe_allow_html=True)

                    if attempts >= 3:
                        st.markdown('<div class="error-box">🚫 User Blocked! Contact Admin</div>', unsafe_allow_html=True)
                        st.stop()
    else:
        st.info("👆 **Please create an account from the Sign Up section to continue.!**")

st.markdown("""
<div style='text-align: center; color: #111111; font-size: 0.9rem; margin-top: 1rem;'>
    ✨ Made with ❤️ by Risha Gupta | Ultra Secure Login System
</div>
""", unsafe_allow_html=True)