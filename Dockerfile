FROM python
RUN pip install ipdb
COPY entry.sh entry.sh
ENTRYPOINT ["/entry.sh"]
