sudo docker run -d --rm \
    --name pasta-run \
    -p 80:80 \
    wayn3927/pasta

#--mount type=bind,source="$(pwd)"/pasta/,target=/var/www/pasta/ \
#--mount type=bind,source="$(pwd)"/pasta/files/,target=/var/www/pasta/files/ \
