FROM manimcommunity/manim:stable

USER root

RUN apt-get update && apt-get install -y \
    xdg-utils \
    desktop-file-utils \
    && rm -rf /var/lib/apt/lists/*

