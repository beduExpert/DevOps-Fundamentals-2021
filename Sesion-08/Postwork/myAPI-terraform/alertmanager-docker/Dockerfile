FROM prom/alertmanager

USER       nobody
EXPOSE     9093
VOLUME     [ "/alertmanager" ]
RUN mkdir -p /alertmanager && \
    rm -f /alertmanager/alertmanager.yml && \
    chown -R nobody:nobody /alertmanager
WORKDIR    /alertmanager
ADD alertmanager.yml /alertmanager
ENTRYPOINT [ "/bin/alertmanager" ]
CMD [ "--config.file=/alertmanager/alertmanager.yml", \
      "--storage.path=/alertmanager/alertmanager-data" ]
