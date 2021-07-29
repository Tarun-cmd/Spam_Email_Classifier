import pickle 
import streamlit as st 
spam_clasfcn_model = pickle.load(open('spam.pkl', 'rb'))
count_vect = pickle.load(open('vectorizer.pkl', 'rb'))
 

def main():
	st.title("Spam Email Classifier Application ")
	st.subheader("Classification")
	mess=st.text_input("Enter a text")
	if st.button("Process"):
		print(mess)
		print(type(mess))
		data=[mess]
		print(data)
		vec=count_vect.transform(data).toarray()
		result=spam_clasfcn_model.predict(vec)
		if result[0] == 0:
			st.success("This is Not A Spam Email")

		else:
			st.error("This is A Spam Email")
			
main()

 


