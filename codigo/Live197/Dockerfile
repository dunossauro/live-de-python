FROM python:3.10

COPY ./exemplo_01.py .
RUN pip install rpdb web_pdb

# Web
EXPOSE 5555
ENV PYTHONBREAKPOINT=web_pdb.set_trace

# Remoto
# EXPOSE 4444
#ENV PYTHONBREAKPOINT=rpdb.set_trace

CMD [ "python", "exemplo_01.py" ]

# Comandos
# buildah bud -t live197 .
# podman run -p 5555:5555 live197