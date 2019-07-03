# GCT (Gestão de comissões Televendas)

Projeto final do Codenation Python Web 2

## Grupo:

- **Mentor**: Alexandre Proença
- Cristian Césari Zatt
- Guilherme Lemke
- João Lucas Nolli Heckmann
- José Miguel de Brito Henriques
- Moisés dos Santos Filho

## Como rodar o projeto:

* Clone esse repositório:  
```git clone https://github.com/CristianZatt/GCT.git ```  
```cd GCT ```
* Crie um virtualenv com Python 3:  
```python3 -m venv .venv ```
* Ative o virtualenv:  
```source .venv/bin/activate ```  
* Instale as dependências:   
```pip install -r requirements.txt ```
* Rode as migrações:  
```python manage.py migrate ```
* Rode o servidor:   
```python manage.py runserver ```
* Abir no navegado o endereço: http://127.0.0.1:8000/


# Overview: Gestão de comissões Televendas

## Objetivo

O objetivo desse produto é de calcular a comissão que cada vendedor do sistema ao longo dos meses seguindo a regra de comissão selecionada na hora que o vendedor for cadastrado.

## Contextualização

Uma empresa de televendas gostaria de armazenar e calcular a comissão dos seus vendedores ao longo do tempo de acordo com o plano de comissão que eles escolheram. Para isso eles precisam de um sistema que fará tal cálculo da comissão ao adicionar o valor mensal das vendas no sistema. A empresa também precisa saber se as vendas dos seus vendedores estão satisfatórias através do cálculo da média ponderada dos valores de vendas nos últimos meses, e caso não esteja eles deverão ser notificados através do email.

## Requisitos técnicos obrigatórios

- Cadastrar Vendedores

Cadastro dos vendedores de telemarketing que irão receber comissões. Para o cadastro é necessário o **nome, endereço, telefone, idade, email, CPF** e o **plano de comissões**.

- Cadastrar plano de comissões

Cadastro dos planos de comissões para que os vendedores possam escolher qual o melhor plano para eles. Para cadastrar um novo plano é necessário definir qual a **porcentagem menor**, o **valor mínimo** que será necessário para considerar a porcentagem de comissão maior e a **porcentagem maior**. Exemplo: se o vendedor vender até 5000 R$ ele vai receber 2% de comissão, caso o valor seja acima de 5000 R$ ele irá receber 5% de comissão.

- Registrar vendas mensais

Registrar o valor das vendas mensais de cada vendedor para que o sistema possa calcular a comissão de acordo com o plano de comissões escolhido. Para o cálculo será necessário informar qual o **vendedor**, o **mês** que ele fez as vendas e o **valor da vendas**.

- Calcular comissão dos vendedores

Ao registrar a venda de um vendedor será necessário também calcular o valor da comissão dele sobre as vendas. O resultado do cálculo da comissão deve ser armazenado para que **seja possível consultar o histórico das comissões do vendedor**.

- Recuperar lista de vendedores ordenados pelo valor da comissão

Recuperar a lista dos vendedores ordenados pelo valor de suas comissões. Para consultar a lista será necessário informar qual o mês atual para que possa ser feito o filtro e a ordenação dos valores.

- Enviar notificação aos vendedores que estão com a média de comissão baixa nos últimos meses

Enviar uma notificação via email para o vendedor que não obtiver um valor acima do cálculo da média de comissões. Para calcular a média do vendedor, deve calcular a média ponderada dos últimos 5 meses desse vendedor considerando os maiores valores com os maiores pesos e se ele estiver abaixo em pelo menos 10% do valor da média deve-se enviar uma notificação para ele. Exemplo:

| **Valor**  |**Peso**   |
|------------|---|
| 1000 R$ | 2  |
| 500 R$  | 1  |
| 1100 R$ | 3  |
| Média | 966, 67 R$ 

Esse vendedor não deve ser notificado caso o valor do mês atual seja maior do que 966, 67 R$ - 10% (870, 00 R$).

Para efetuar o cálculo, pode-se criar um endpoint que irá receber o **valor atual de vendas** e o **ID do vendedor** para calcular.

## Sobre a apresentação do projeto

Para que todos do grupo tenham a chance de apresentar seu trabalho, a **apresentação** deve ser feita de forma **individual**. Vocês podem ensaiar juntos, fazer um roteiro parecido, mas **é importante que cada participante faça sua própria gravação**.

Objetividade é muito importante - falem naturalmente e sem ler, por favor! :) Recomendamos que você faça um video-call e gravem este call. Assim, poderão ficar à vontade para compartilhar a tela e mostrar o código ou qualquer outra coisa importante. O vídeo deve ter no **máximo 10 minutos**.

**Segue uma sugestão de roteiro:**

- Apresentação pessoal

> “Oi, pessoal…, eu me chamo _____ e vou apresentar para vocês o projeto final que fiz com a squad ______(número e nome) da Aceleração _______ da Codenation.”

- Apresentação do projeto

	- Os membros da squad; 
	- Descrição do projeto e desenvolvimento do processo que a squad utilizou para resolver o problema; 
	- Divisão de tarefas entre os membros da squad e quais foram suas principais responsabilidades; 
	- Tecnologias utilizadas e eficácia; 
	- Aprendizados destacados durante o processo e ao final do projeto; 
	- Duas principais dificuldades, e como foram contornadas; 
	- Dois principais acertos ou escolhas acertadas que fizeram diferença no projeto e por quê.

Para ficar mais fácil, [dê uma olhada nesta apresentação de projeto de um programa que realizamos em Joinville](https://drive.google.com/file/d/1Owc4VYM492svCn7RlMnNs_Bk4ZGjZkvj/view). Neste caso, os participantes desenvolveram em squads uma aplicação (backend e frontend) que buscava anunciar animais perdidos ou animais para adoção. Assim, pessoas interessadas poderiam colaborar para adotar e/ou encontrar um pet. Fiz alguns comentários na apresentação para ajudar vocês! :)

**Como enviar os vídeos?**

Após terem determinado o roteiro e feito suas gravações individuais, encaminhe por e-mail o link do **vídeo no YouTube** (lembre de colocá-lo como **não listado**, por favor). No título, use a seguinte descrição: **“Apresentação projeto final [Seu Nome] [nome de sua squad]”** . O link do vídeo deve ser enviado para <mario.machado@codenation.dev> e <ingrid.adam@codenation.dev>, juntamente com o link do Code Review do projeto na plataforma Codenation, com o assunto **“AceleraDev Python - Squad [nº da sua squad]”** até o dia **31/07/2019**.
