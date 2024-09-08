#!/bin/bash

# Set the umask to match your host system's file creation permissions
umask 0002

# Run Manim as root with all the arguments passed to the script
manim "$@"

# Change ownership of the generated files to the user 'manimuser'
chown -R manimuser:manimuser media/videos/updater_animations/720p30
