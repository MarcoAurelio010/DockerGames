FROM alpine/git AS builder
WORKDIR /app
RUN git clone https://github.com/gabrielecirulli/2048.git .

FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app /usr/share/nginx/html

EXPOSE 80