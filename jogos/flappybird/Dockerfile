# Estágio 1: Builder (codinome: builder)
FROM alpine/git AS builder
WORKDIR /app
# Link direto do repositório que analisamos
RUN git clone https://github.com/imkennyyip/flappy-bird.git .

# Estágio 2: Produção (Nginx)
FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app /usr/share/nginx/html

EXPOSE 80