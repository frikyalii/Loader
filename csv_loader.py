from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="social_media_ads.csv")
docs = loader.load()

# print(docs[0])
print(len(docs))