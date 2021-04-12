import streamlit as st
import pickle

st.title('Is this post from Facebook or Twitter?')

page = st.sidebar.selectbox(
'Select a page:',
('About', 'FB or Twitter')
)

#st.sidebar.text_input("What's your name?")

if page == 'About':
    st.write('This is Lab about Streamlit!')
    st.write('Thanks for visiting')
    st.write('Contact info: 804 123-4567')

if page == 'FB or Twitter':
    st.write('')
    st.write('')
    st.write('')

    st.markdown('Facebook and Twitter: Social Media Giants.  Which Social Media are you posting about?')

    with open('model.p', mode='rb') as pickle_in:
        pipe = pickle.load(pickle_in)

        user_text = st.text_input('Please input your post:', value = "Love Facebook Groups")

    fbot = pipe.predict([user_text])[0]
    st.write(f'Your post comes from {fbot}')

if page == 'Contact Me':
    name = st.text_input('What is your name?')
    email = st.text_input('What is your email?')
    question = st.text_input('What is your question?')

    user_query_dict = {
        'name': name,
        'email': email,
        'Question': question
    }

    st.write("")
    st.write("")
    st.write(f'Thanks for reaching out, {name}!  I look forward to emailing you about {question} at {email}')