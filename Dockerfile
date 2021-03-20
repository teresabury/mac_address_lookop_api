FROM python:3.8

RUN pip3 install requests argparse

COPY ./ex_1.py /
RUN chmod +x /ex_1.py

ENTRYPOINT ["python3", "ex_1.py"]
