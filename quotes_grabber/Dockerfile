# Step 1: Import the Python
FROM python:3.6-stretch

# Step 2: Create the Work Directory
WORKDIR /app

# Step 3: Copy all into Work Directory
ADD . /app

# Step 4: Install all Dependencies
RUN pip3 install -r requirements.txt

# Step 5: Run uwsgi command
CMD ["uwsgi", "--ini", "app.ini"]