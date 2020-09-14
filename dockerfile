FROM centos:latest

RUN yum update
RUN yum install apache

ENV APACHE_RUN_USER apache
ENV APACHE_RUN_GROUP apache
ENV APACHE_LOG_DIR /var/log/apache
