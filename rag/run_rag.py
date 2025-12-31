from rag.rag_pipeline import rag_chat


print("🔐 Privacy-Safe RAG with Gemma 3 (1B)")
print("Type 'exit' to quit\n")

while True:
        q = input("USER > ").strip()
        if q.lower() in ["exit", "quit"]:
            break

        answer = rag_chat(q)
        print("MODEL >", answer)
        print("-" * 60)