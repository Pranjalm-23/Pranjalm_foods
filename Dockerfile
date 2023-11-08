FROM node:alpine

WORKDIR /app/frontend
COPY /app/frontend/package*.json .
RUN npm install
COPY . .
RUN npm run build

FROM python:3.11
WORKDIR /app/backend
COPY app/backend/* .
ENV GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS}
WORKDIR /app
COPY /app/. .
EXPOSE 5000:5000
CMD ["./start.sh"] 





