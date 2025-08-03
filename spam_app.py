import streamlit as st
import pickle

#load the vectorizer and model
with open('spam_model1.pkl','rb') as f:
    vectorizer,model = pickle.load(f)

# Streamlit page
st.set_page_config(page_title='SpamScan',page_icon="📬")
st.title("📬 SpamScan")
st.write("Enter a Message/Mail and find out whether it's spam or not.")

message=st.text_area("Your Message",height=200)

# Prediction button
if st.button('Predict'):
    if message.strip()=="":
        st.warning("Please enter a Message/Mail")
    else:
        # making prediction using model
        message_vector=vectorizer.transform([message])
        prediction=model.predict(message_vector)[0]

        if prediction==0:
            st.error("⛔ This Message/Mail is SPAM !!!")
        else:
            st.success("✅ This message is Not Spam")