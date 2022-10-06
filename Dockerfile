FROM python:3.9
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.api:app"]