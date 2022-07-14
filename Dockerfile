FROM python:latest

# set the working directory
WORKDIR /krystle_text_app

# install dependencies
COPY ./requirements.txt /krystle_text_app
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
# copy the scripts to the folder
COPY . /krystle_text_app

# start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "666"]
