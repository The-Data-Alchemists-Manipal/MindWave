from transformers import pipeline

class MOMGenerator:
    def __init__(self):
        print("Loading NLP Model (This takes a moment on first run)...")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.max_chunk_size = 800

    def generate_mom(self, transcript: str) -> str:
        if not transcript.strip():
            return "No transcript recorded."

        words = transcript.split()
        chunks = [' '.join(words[i:i + self.max_chunk_size]) for i in range(0, len(words), self.max_chunk_size)]
        
        summaries = []
        for chunk in chunks:
            summary = self.summarizer(chunk, max_length=130, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        
        final_mom = "\n\n".join(summaries)
        
        formatted_mom = "### Minutes of Meeting (MOM)\n"
        for sentence in final_mom.split(". "):
            if sentence:
                formatted_mom += f"- {sentence.strip()}.\n"
                
        return formatted_mom