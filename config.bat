python -m venv ..\Rule-based-Inclusivity-Detection\venv
call .\venv\Scripts\activate.bat
pip install -r requirements.txt
pip install spacy
python -m spacy download it_core_news_lg
cd "script\inclusivity_management\"
PAUSE