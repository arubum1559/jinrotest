FROM Python 3.7.3

RUN pip install -U pip
RUN pip install -U discord.py

ENTRYPOINT python jinro.py