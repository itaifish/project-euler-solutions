FROM python:3.13.3

ENV NUM_RUNS 20
VOLUME [ "/euler-solutions" ]

COPY runner.py /run/

ENTRYPOINT ["python", "/run/runner.py"]
CMD [ "20" ]