from pinecone import Pinecone, ServerlessSpec

# Paste your full API key here (not the hidden one with asterisks)

API_KEY = "pcsk_6oqPCr_woxztFJXM7grNr2EDvQfLMsy9HLgYvDY85qoa1MriPL17KdcuTDq1KKPnmrkvC"  # Use your full key here


pc = Pinecone(api_key=API_KEY)

# Now do stuff
print("Available Indexes:", pc.list_indexes().names())

