#!/bin/bash

docker build --tag ubuntu20.04-bash --file test/ubuntu20.04-bash.dockerfile .

gsc build --insecure-args ubuntu20.04-bash test/ubuntu20.04-bash.manifest

temp_dir=$(mktemp -d)
cp config.yaml.template "$temp_dir/config.yaml"
cd "$temp_dir" || exit

key_path="$temp_dir/enclave-key.pem"
if [ ! -f key_path ]; then
    openssl genrsa -3 -out "$key_path" 3072
fi
gsc sign-image ubuntu20.04-bash "$key_path"

gsc info-image gsc-ubuntu20.04-bash
