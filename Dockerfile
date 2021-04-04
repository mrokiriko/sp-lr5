FROM debian
COPY fsum.py .
COPY dsum.py .
RUN apt update && apt install python3 -y
