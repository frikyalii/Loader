from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI;
from langchain_core.output_parsers import StrOutputParser;
from langchain_core.prompts import PromptTemplate;
from dotenv import load_dotenv;
load_dotenv();

model = ChatOpenAI()


prompt=PromptTemplate(
    template="Summarize the following text: {poem}",
    input_variables=["poem"]
)

parser = StrOutputParser();


loader = TextLoader("cricket.txt")
docs = loader.load()

print(type(docs))

chain = prompt | model | parser
print(chain.invoke({"poem": docs[0].page_content}))