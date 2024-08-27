from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st


def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:

        agent = create_csv_agent(
            OpenAI(temperature=0), csv_file, verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()



# from langchain_community.document_loaders.csv_loader import CSVLoader
# from langchain.llms import OpenAI
# from dotenv import load_dotenv
# import os
# import streamlit as st
# import pandas as pd

# def main():
#     load_dotenv()

#     # Load the OpenAI API key from the environment variable
#     if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
#         print("OPENAI_API_KEY is not set")
#         exit(1)
#     else:
#         print("OPENAI_API_KEY is set")

#     st.set_page_config(page_title="Ask your CSV")
#     st.header("Ask your CSV 📈")

#     csv_file = st.file_uploader("Upload a CSV file", type="csv")

#     # Check if file was uploaded
#     if csv_file:
#     # Check MIME type of the uploaded file
#         if csv_file.type == "text/csv":
#             df = pd.read_csv(csv_file)
#         else:
#             df = pd.read_excel(csv_file)

#         # # Work with the dataframe
#         # st.dataframe(df.head())


    
#         loader = CSVLoader(file_path=df)

#         data = loader.load()

#         print(data)
#         # agent = create_csv_agent(
#             # OpenAI(temperature=0), csv_file, verbose=True)

#         # user_question = st.text_input("Ask a question about your CSV: ")

#         # if user_question is not None and user_question != "":
#         #     with st.spinner(text="In progress..."):
#         #         st.write(agent.run(user_question))


# if __name__ == "__main__":
#     main()


