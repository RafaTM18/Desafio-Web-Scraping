# Desafio Web Scraping
 
<p align="center">Um programa de Web Scraping desenvolvido em Python</p>

<details open="open">
  <summary>Tabela de Conteúdo</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre o projeto</a>
      <ul>
        <li><a href="#web-scraping">Web Scraping?</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Introdução</a>
      <ul>
        <li><a href="#prerequisites">Pré-requisitos</a></li>
        <li><a href="#installation">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#usage">Como usar?</a></li>
    <li><a href="#license">Licença</a></li>
    <li><a href="#contact">Contato</a></li>
  </ol>
</details>


<h2 id="about-the-project">Sobre o projeto</h2>

Esse projeto tem como objetivo aplicar as técnicas de Web Scraping para coletar informações do site [Investing.com](https://investing.com/), sendo mais específico o site em sua versão [BR](https://br.investing.com/). A informação ao ser coletada será da seguinte tabela:

<p align="center">
 <img src="https://imgur.com/ylhhjBo.png" alt="Tabela do site br.investing.com">
</p>

Para pegar a informação do site, usamos o conceito de Web Scraping.

<h3 id="web-scraping">O que é Web Scraping?</h3>

Web scraping é o processo de coleta de dados estruturados da web de maneira automatizada. Também é chamado de extração de dados da web. Alguns dos principais casos de uso do web scraping incluem monitoramento de preços, inteligência de preços, monitoramento de notícias, geração de leads e pesquisa de mercado, entre muitos outros.

Em geral, a extração de dados da web é usada por pessoas e empresas que desejam usar a vasta quantidade de dados da web disponíveis publicamente para tomar decisões mais inteligentes.

<p align="right">
 Fonte: <a href="https://www.gocache.com.br/seguranca/o-que-e-web-scraping-para-iniciantes/">GoCache</a>
 </p>

<h2 id="getting-started">Introdução</h2>

Algumas informações de pré-requisitos do programa e como instalar o mesmo estão dispostas a seguir:

<h3 id="prerequisites">Pré-requisitos</h3>
 O programa feito é capaz de realizar funções diferentes dependendo do comando, então caso queira utilizar somente a parte mais básica, os pré-requisitos a seguir são o mínimo para rodar o programa:
 
* [Python](https://www.python.org/) - Versão utilizada: 3.9
* [Pandas](https://pandas.pydata.org/) - Versão utilizada: 1.3.2
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Versão utilizada: 4.9.3

Para utilizar a função de pegar as tabelas das ações mais populares será necessário:

* [Selenium](https://selenium-python.readthedocs.io/) - Versão utilizada: 3.141.0
* [Driver do Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) - Tem um driver já disponível nesse repositório, mas talvez seja necessário baixar uma versão mais nova

E caso queira salvar os dados em um banco de dados, você precisa de:

* [MySQL](https://www.mysql.com/) - Versão utilizada: 8.0.21
* [PyMySQL](https://pymysql.readthedocs.io/en/latest/) - Versão utilizada: 1.0.2

<h3 id="installation">Instalação</h3>
Para instalar o programa basta seguir os seguintes passos:

1. Clone o repositório
   ```sh
   git clone https://github.com/RafaTM18/Desafio-Web-Scraping.git
   ```
2. Instale as dependências que deseja utilizar
3. ???
4. Profit

<!-- USAGE EXAMPLES -->
<h2 id="usage">Como utilizar o programa?</h2>
Como mencionado na sessão dos pré-requisitos, o programa tem funções diversas.
O comando a seguir é o mais simples:
``` python
 py main.py <link ou lista de links>
```
Isso retornará um ou vários arquivos .csv com informações da ação escolhida retiradas do site https://br.investing.com/

Esse comando irá recuperar as informações das 5 ações mais populares no momento de acesso:
``` python
 py main.py top
```
Igualmente ao comando acima, ele irá retornar 5 arquivos .csv
_OBS: Necessário a biblioteca Selenium e o Driver do Chrome_

E por fim, esse comando é responsável por inserir no Banco de Dados as informações salvas nos arquivos .csv
``` python
 py database.py
```
Serão criada uma tabela pra cada ação e toda a informação do arquivo .csv será inserido nas tabelas do BD. Além disso, ao rodar esse comando, é possível atualizar os dados das tabelas do BD caso os arquivos .csv estejam atualizados com dados mais recentes.
_OBS: Necessário a biblioteca PyMySQL e o SGBD MySQL_
_OBS2: Para realizar a conexão ao BD, estão sendo usadas valores "padrões", então talvez seja necessário a modificação deles_

<h2 id="license">Licença</h2>

Distribuído utilizando a Licença MIT. Veja `LICENSE` para mais informações.

<h2 id="contact">Contato</h2>
Rafael Tamura - rafaeltmferreira18@gmail.com

Link do projeto: [https://github.com/RafaTM18/Desafio-Web-Scraping](https://github.com/RafaTM18/Desafio-Web-Scraping)
