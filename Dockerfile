FROM ubuntu
COPY . /app/
RUN command
CMD [ "pipenv run pip install -r requirements.txt", "python ./app.py" ]
ENTRYPOINT [ "executable" ]