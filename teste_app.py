import streamlit as st
import requests

st.title("Meu Postman customizado")

url = st.text_input("Digite a URL da sua API")

method = st.selectbox("Método HTTP:", ["GET", "POST", "PUT", "DELETE"])

body = st.text_area("Body (JSON):")

if st.button("Enviar Requisição"):
    try:
        if method =="GET":
            response = requests.get(url)
            
        elif method == "POST":
            respose = requests.post(url, json=eval (body) if body else ())
            
        elif method == "PUT":
            response = requests.put(url, json=eval (body) if body else ())
        
        elif method == "DELETE":
            response = requests.delete(url)
            
        st.subheader("Status Code")
        st.write(response.status_code)
        
        st.subheader("Resposta:")
        st.json(response.json())
        
    except Exception as e:
        st.error(f"Erro {e}")