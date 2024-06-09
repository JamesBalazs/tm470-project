FROM postgres:16

RUN apt-get update -qq && \
    apt-get install --no-install-recommends postgresql-16-pgvector && \
    rm -rf /var/lib/apt/lists /var/cache/apt/archives

EXPOSE 5432/tcp