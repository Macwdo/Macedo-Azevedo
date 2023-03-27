# Repositorio Back End do App Macedo - Azevedo
### Para rodar a aplicação necessita-se de :

<ul>
    <li> Realizar o git clone da aplicação
    <li>Realizar a instalação do  <a href="https://www.docker.com/"><b style="color: #12addf"> Docker </b></a>
    <li>Copiar o arquivo <b>.envexamples</b> e criar com conteudo copiado <b>.env</b>
</ul>

### Após a instalação do docker devemos rodar os seguintes comandos.

    make build_image
    make up
    make build
    
### Ao Final a aplicação deve estar funcionando nos seguintes urls <a href="http://0.0.0.0/" ><b style="color: #99ccff"> Macedo & Azevedo</b></a>

- localhost
- 0.0.0.0

### Para visualização do banco use o <a href="http://0.0.0.0:5050/" ><b style="color: #99ccff">PGAdmin</b></a> (Espere pois demora um pouco para abrir)


### Alguns atalhos (o container precisa estar ativo)
    make admin # Criação de um usuário admin
    make attach # Para leitura dos logs da aplicação
    make migrations # Para realizar as migrações da aplicação

