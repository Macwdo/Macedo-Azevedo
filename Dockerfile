# Imagem base com Python e dependências do sistema
FROM python:3.11.1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get clean && apt-get update
RUN apt-get install -y gcc python3-dev python-dev build-essential default-libmysqlclient-dev musl-dev wkhtmltopdf

ENV XDG_RUNTIME_DIR=/tmp

RUN pip install --upgrade pip --user

# Copia o código da aplicação para o diretório de trabalho
COPY code /home/app

# Instala as dependências do Python
RUN pip install gunicorn
RUN pip install -r /home/app/requirements.txt

# Instala as dependências do sistema e o Nginx
RUN apt-get update && apt-get install -y nginx && apt-get clean


# Copia o arquivo de configuração do Nginx
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Coleta os arquivos estáticos do Django
RUN #./manage.py collectstatic --noinput

# Expõe a porta do Nginx
EXPOSE 80

RUN chmod +x ./configs/entrypoint.sh

# execute our entrypoint.sh file
CMD ["./configs/entrypoint.sh"] 
