# Build the networks in one container
# ===================================
FROM python:3 as builder

# Install Camoco
RUN pip install numpy scipy==1.2.*
RUN pip install camoco camoco-cob

# Setup the user
RUN useradd -ms /bin/bash camoco
USER camoco

# Copy over the data
COPY --chown=camoco:camoco ./data /data

# Build the maize networks
WORKDIR /data/maize
RUN python3 MaizeBuildCommands.py

# Move the constructed networks to an execution container
# =======================================================
FROM python:3

# Install Camoco
RUN pip install numpy scipy==1.2.*
RUN pip install camoco camoco-cob

# Setup the user
RUN useradd -ms /bin/bash camoco
USER camoco

# Get the data from the builder container
COPY --from=builder --chown=camoco:camoco /home/camoco/.camoco /home/camoco/.camoco
COPY --from=builder --chown=camoco:camoco /home/camoco/.camoco.conf /home/camoco/.camoco.conf

# Get the cob config file
COPY --chown=camoco:camoco cob.conf /home/camoco/cob.conf

# Set the execution environment
EXPOSE 50000
WORKDIR /home/camoco
CMD cob -c /home/camoco/cob.conf

