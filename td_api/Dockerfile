FROM nickgryg/alpine-pandas:latest
# Create app directory
WORKDIR /td_api

RUN apk add --no-cache gcc musl-dev \
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev

COPY requirements.txt /td_api

RUN pip install -r requirements.txt

COPY . /td_api

EXPOSE 8080

CMD ["python", "./app.py"]