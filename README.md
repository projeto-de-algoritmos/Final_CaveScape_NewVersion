

# New Version - CaveScape

**Trabalho Final** <br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0164357  |  Ugor Brandão |
| 17/0161897 | Eduarda Servidio |

## Sobre  
Você está dentro de uma caverna e precisa escapar dela! Você tem acesso a um mapa onde mostra todos os postos dentro da caverna, porém percebe que ele está desatualizado! No mapa que você tem, todos os postos estão conectados entre si, e algumas conexões não existem mais. O seu objetivo é sair da caverna testando se existem caminhos ou não entre os postos. <br>

NOVIDADE!!! <br>

Agora o jogo apresenta alguns modos de jogar. Cada modo é ligado a um módulo da disciplina. 3 modos foram implementados referentes a Grafo 1, a Grafo 2 e a Programação Dinâmica.  <br><br>
* No modo 1, temos a versão original do jogo. Onde o usuário deve encontrar os postos que estão interligados entre si até encontrar a saída. <br>
* No modo 2, temos a versão relacionada a Grafos 2, onde em cada posto acessado, o usuário deverá resolver enigmas relacionados ao menor custo em CaveCoins (moedas) para acessar todos os postos. <br>
* Os modos 3 e 4, ainda estão em fase de desenvolvimento, não conseguimos linkar muito bem os conteúdos com a temática, mas podemos implementar algo a mais. <br>
* No modo 5, temos a versão relacionada a Programação Dinâmica, onde em cada posto acessado, o usuário deverá resolver enigmas relacionados a maior quantidade de CaveCoins que o usuário consegue carregar até a saída.

## Screenshots

### Tela Inicial
![image](https://user-images.githubusercontent.com/52542729/165184390-c92957cb-8ed0-4432-963f-7b3f61767d0d.png)
Figura 1: Tela inicial.

### Modo 1:
![image](https://user-images.githubusercontent.com/52542729/165184459-4439155c-596a-4ef6-b7fb-eafff1b167ca.png)
Figura 2: Tela inicial do modo 1.

![image](https://user-images.githubusercontent.com/52542729/165184521-fc52da0b-e388-4747-aba0-1486789d0879.png)
Figura 3: Tela de caminhos do modo 1.

### Modo 2:

![image](https://user-images.githubusercontent.com/52542729/165184673-895caa9c-cb67-4f9e-a480-791c2526f14d.png)
Figura 4: Tela inicial do modo 2.

![image](https://user-images.githubusercontent.com/52542729/165184756-d228be4c-499f-40bc-8ffb-b6dadfd4fb27.png)
Figura 5: Tela de quando não acerta o menor custo para acessar os postos. Mensagem de Erro.

![image](https://user-images.githubusercontent.com/52542729/165184874-334e1abe-bfaf-45bc-8d3d-26ee86099f13.png)
Figura 6: Tela de quando acerta o menor custo para acessar os postos. Mensagem de Acerto.

### Modo 3:

![image](https://user-images.githubusercontent.com/52542729/165184948-55af1bbb-801a-4e7a-8637-13414f73577c.png)
Figura 7: Tela inicial do modo 5.

![image](https://user-images.githubusercontent.com/52542729/165185004-07bd9d9e-3709-4685-9e3d-b74769fce4b0.png)
Figura 8: Tela de quando não acerta o maior valor de CaveCoins que pode levar. Mensagem de Erro.

![image](https://user-images.githubusercontent.com/52542729/165185091-7693de0c-3df4-43f6-98f4-7ec5a3f0202c.png)
Figura 9: Tela de quando acerta o maior valor de caveCoins que pode levar. Mensagem de Acerto.

### Telas Gerais - Game Over e Vitória
![image](https://user-images.githubusercontent.com/52542729/165185185-6e99e7b8-c386-4ca3-866a-e5ab2f6e2a69.png)
Figura 10: Tela de Game Over, quando não há caminho entre os postos.

![image](https://user-images.githubusercontent.com/52542729/165185264-145b0f54-ecf0-4260-b966-85679426b117.png)
Figura 11: Tela de Vitória, quando encontra a saída.

## Instalação 
**Linguagem**: Python, HTML e CSS. <br>
**Pré-requisitos**: ter o Python e o Flask instalados na máquina, abrir e executar os arquivos de preferência no VSCode.
Ao executar o arquivo no VSCode, um localhost será criado, dando acesso ao jogo.

## Uso 
Os caminhos que existem entre os postos (nós) são os seguintes:

| Posto | Acesso a |
| -- | -- |
| 1  | 2,7,8 |
| 2  | 7,1,8 |
| 3  | 7 |
| 4  | 6,8 |
| 5  | 5,10 |
| 6  | 4,5 |
| 7  | 1,3,4 |
| 8  | 1,4,9 |
| 9  | 8 |
| 10  | 5 |

* Para uma rápida avaliação do jogo, no modo 2, a resposta com o menor custo para percorrer todos os postos está rotacionada embaixo da listagem. <br>
* 
* Para uma rápida avaliação do jogo, no modo 5, a resposta com o maior valor das CaveCoins de cada posto está rotacionada embaixo da tabela de valores. <br>

* Ao acertar as respostas, nos modos 2 e 5, aparecerá uma mensagem de acerto e você terá que ir para outro posto. <br>

* Ao errar, uma mensagem de erro aparecerá e você deverá tentar novamente.

* Ao chegar no posto 10, uma mensagem de "Você encontrou a saída" aparecerá. <br> 

* Ao tentar acessar um posto que não tem caminho, uma mensagem de "Voce errou" irá surgir, onde o jogador deve voltar a página inicial e tentar encontrar a saída novamente.
