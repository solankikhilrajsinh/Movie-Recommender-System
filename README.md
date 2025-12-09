Movie Recommendation System

This project is a fully functional Movie Recommendation System developed using Python, FastAPI, and Streamlit. It leverages machine learning and NLP techniques to generate personalized movie recommendations. The system uses the Kaggle Movie Dataset and integrates multiple data-processing and modeling libraries to deliver accurate and reliable results.


Features
- Content-based movie recommendations using cosine similarity
- Preprocessing of movie metadata including genres, keywords, cast, crew, and overview
- FastAPI backend responsible for serving recommendation results via REST APIs
- Streamlit frontend interface for interacting with the recommendation model
- Implementation of various machine learning and NLP libraries
- Clean, modular project structure for scalability


Tech Stack
- Python
- FastAPI (Backend API)
- Streamlit (Frontend UI)
- Pandas, NumPy
- Scikit-learn
- NLTK and text-processing libraries
- Kaggle Movie Dataset


Dataset
- The system uses the Kaggle Movie Dataset, which includes metadata such as:
- Movie titles
- Genres
- Cast and crew information
- Plot descriptions
- Ratings
- Popularity scores


How It Works
1. Movie metadata is cleaned and preprocessed.
2. Text-based fields are transformed into vector representations.
3. Cosine similarity is computed to identify similar movies.
4. A FastAPI endpoint provides recommendation results to the frontend.
5. The Streamlit application consumes the API and displays user-friendly   recommendations.