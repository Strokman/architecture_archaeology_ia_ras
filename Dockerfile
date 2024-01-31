FROM python:3.12-slim



# copy the files into the image
COPY . /home/architecture_archaeology

# install the dependencies and packages in the requirements file
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r /home/architecture_archaeology/requirements.txt

# switch working directory
WORKDIR /home/architecture_archaeology/architecture_archaeology


ENTRYPOINT ["/home/architecture_archaeology/boot.sh"]


