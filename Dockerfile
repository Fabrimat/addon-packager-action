FROM python:3-alpine3.15

COPY package.py /package.py

ENTRYPOINT ["python","/package.py"]