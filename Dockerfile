FROM python:3.12-slim

# switch working directory
WORKDIR /app

# copy the files into the image
COPY . .


# install the dependencies and packages in the requirements file
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
