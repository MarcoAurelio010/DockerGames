# Estágio 1: Builder
FROM alpine/git AS builder
WORKDIR /app
RUN git clone https://github.com/imkennyyip/flappy-bird.git .

# Injeção de CSS via terminal
RUN sed -i 's/<body[^>]*>/<body style="background: radial-gradient(circle, #1a2a6c, #112b3c, #0b1319); display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden;">/' index.html

# Estágio 2: Produção (Nginx)
FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app /usr/share/nginx/html
EXPOSE 80