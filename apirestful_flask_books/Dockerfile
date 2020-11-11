# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk update
RUN apk add --no-cache build-base 
RUN apk add --no-cache postgresql-dev

# Defining working directory and adding source code
WORKDIR /usr/src/app

# muda com mais frequencia
COPY api.py entrypoint.sh ./ 
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
