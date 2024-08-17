# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary packages
RUN apt-get update && apt-get install -y wget gnupg2 unzip curl

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install chromedriver_autoinstaller
RUN pip install chromedriver_autoinstaller

# Run a script to install the correct version of ChromeDriver
RUN python -c "import chromedriver_autoinstaller; chromedriver_autoinstaller.install()"

# Command to run tests with environment variables
CMD ["pytest", "./tests/", "--reruns", "2", "--reruns-delay", "5", "--browser=chrome-headless"]
