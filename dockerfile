FROM centos:latest

RUN yum update -y
RUN yum install -y httpd

ENV APACHE_RUN_USER apache
ENV APACHE_RUN_GROUP apache
ENV APACHE_LOG_DIR /var/log/apache
