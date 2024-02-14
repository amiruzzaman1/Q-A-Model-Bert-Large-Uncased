import streamlit as st
from simpletransformers.question_answering import QuestionAnsweringModel

# Load your model
model_path = "best_model"
model = QuestionAnsweringModel("bert", model_path, use_cuda=False)

# Streamlit app
st.title("Question Answering Model(Bert Large Uncased)")

# Input fields
context = st.text_area("Context:")
question = st.text_input("Question:")

# Prediction button
if st.button("Predict"):
    to_predict = [{"context": context, "qas": [{"question": question, "id": "0"}]}]
    try:
        answers, _ = model.predict(to_predict, n_best_size=1)
        if answers and 'answer' in answers[0]:
            st.text("Answer:")
            st.write(f"<span style='color:cyan; font-weight:bold'>{answers[0]['answer'][0]}</span>", unsafe_allow_html=True)
        else:
            st.text("No answer found.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


st.header("Sample Context:")
st.write("During the Renaissance period in Europe, the Medici family played a crucial role in fostering artistic and intellectual advancements. Their patronage of artists and scholars in Florence contributed significantly to the flourishing of Renaissance culture.")
st.write(f"Question: <span style='color:yellow;'>What family was influential during the Renaissance?</span>", unsafe_allow_html=True)
st.write(f"Answer: <span style='color:red;'>Medici family</span>", unsafe_allow_html=True)