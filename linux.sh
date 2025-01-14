mkdir edilson_ribeiro
mkdir -p edilson_ribeiro/resultado
curl -O https://vanilton.net/v1/download/zip.zip
unzip arquivo.zip -d edilson_ribeiro
mv readme.md /edilson_ribeiro/resultado
rm /edilson_ribeiro/arquivo.zip
