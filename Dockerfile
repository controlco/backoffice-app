# Creating image based on official python3 image
FROM python:3

# Creating and putting configurations
RUN mkdir /config
COPY requirements.txt /config/
COPY on-container-start.sh /config/

# Installing all python dependencies
RUN pip install -r config/requirements.txt

# Open port 8000 to outside world
EXPOSE 8000
# When container starts, this script will be executed.
# Note that it is NOT executed during building
CMD ["sh", "/config/on-container-start.sh"]

# Creating and putting application inside container
# and setting it to working directory (meaning it is going to be default)
RUN mkdir /app
WORKDIR /app
COPY app /app/