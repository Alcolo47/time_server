FROM python:3 as compil

COPY src/requirements.txt /SRC/requirements.txt
RUN python -m pip install -r /SRC/requirements.txt

COPY src/ /SRC/
RUN python -m pip install /SRC/


FROM python:3
COPY --from=compil /usr/local/bin /usr/local/bin
COPY --from=compil /usr/local/lib /usr/local/lib

ENV PORT=8000
CMD ["time-server"]
