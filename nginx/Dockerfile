FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

RUN mkdir /etc/nginx/templates/
COPY nginx.template /etc/nginx/templates/