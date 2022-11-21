FROM python:3.8-slim
WORKDIR /usr/src/app

RUN pip install poetry==1.2.2
COPY poetry.lock pyproject.toml ./
RUN poetry export -o requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/"

CMD ["python", "highlights/scripts/scheduler.py"]
