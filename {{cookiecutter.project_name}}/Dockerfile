# from ryxcommar blog: https://ryxcommar.com/2024/02/15/how-to-cut-your-python-docker-builds-in-half-with-uv/

FROM python:3.11

# Install uv
ENV VIRTUAL_ENV=/usr/local
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Install Python dependencies 
COPY requirements.txt /requirements.txt
RUN /root/.cargo/bin/uv pip install --no-cache -r requirements.txt
 
# Copy Python code to the Docker image
COPY {{cookiecutter.project_slug}} /code/{{cookiecutter.project_slug}}/

CMD [ "python", "{{cookiecutter.project_slug}}/foo.py"]