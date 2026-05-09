import os
import typer
from rich.prompt import Prompt
from agno.agent import Agent
from agno.models.groq import Groq
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.qdrant import Qdrant
from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")

# Path to your PDF document
PDF_PATH = os.getenv("PDF_PATH", "Your PDF Path")

vector_db = Qdrant(
    collection="pdf-assistant-search",
    path="./qdrant_storage",
    embedder=SentenceTransformerEmbedder(
        id="all-MiniLM-L6-v2",
        dimensions=384,
    ),
)

knowledge_base = Knowledge(
    vector_db=vector_db,
    max_results=3,
)


def pdf_assistant(user: str = "user"):
    """Interactive CLI assistant that answers questions from an indexed PDF."""
    agent = Agent(
        model=Groq(
            id="llama-3.1-8b-instant",
            api_key=groq_key,
        ),
        knowledge=knowledge_base,
        search_knowledge=True,
        debug_mode=False,
    )

    print("\n📄 PDF Assistant is ready! Type 'exit' or 'bye' to quit.\n")

    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message.strip().lower() in ("exit", "bye"):
            print("Goodbye! 👋")
            break
        agent.print_response(message)


if __name__ == "__main__":
    # -------------------------------------------------------
    # STEP 1: Index your PDF (run once, then comment out)
    # knowledge_base.add_content(path=PDF_PATH)
    # -------------------------------------------------------

    typer.run(pdf_assistant)
