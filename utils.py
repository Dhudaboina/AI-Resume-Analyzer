import PyPDF2
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def clean_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def calculate_similarity(resume, job_desc):
    texts = [resume, job_desc]
    cv = CountVectorizer()
    matrix = cv.fit_transform(texts)
    similarity = cosine_similarity(matrix)[0][1]
    return round(similarity * 100, 2)

def missing_skills(resume, job_desc):
    resume_words = set(resume.split())
    job_words = set(job_desc.split())
    missing = job_words - resume_words
    return list(missing)[:10]