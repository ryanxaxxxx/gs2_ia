Green Way 🚀🌱
Green Way é um aplicativo que utiliza Machine Learning e Inteligência Artificial para recomendar o melhor meio de transporte para trajetos curtos, considerando fatores como distância, clima e horário. 
O objetivo é incentivar escolhas mais sustentáveis e eficientes para o dia a dia.

### Link para o vídeo: https://youtu.be/BZrQWCec4LQ


### Tecnologias Utilizadas

- Python 3.10+
- FastAPI – para criar a API web
- Pandas – manipulação de dados
- scikit-learn – construção e treinamento do modelo de Machine Learning
- Pydantic – validação de dados de entrada


### Como Funciona

O aplicativo utiliza um modelo de Random Forest para classificar o melhor modal de transporte com base nos seguintes parâmetros:
- distancia_km: distância do trajeto em quilômetros
- clima: condição climática (sol, chuva, nublado)
- horario: período do dia (manha, tarde, noite)
- O modelo foi treinado com dados de exemplo e retorna uma recomendação, como:
- Caminhada
- Bike
- Ônibus
- Carona

### Endpoints da API
POST /recomendar

Descrição: Recebe informações do trajeto e retorna o modal de transporte recomendado.

Exemplo de requisição:

{
  "distancia": 3.5,
  "clima": "sol",
  "horario": "manha"
}

### Como Rodar o Projeto

Clone o repositório:


Instale as dependências:
- pip install fastapi uvicorn pandas scikit-learn

Execute a API:
- uvicorn main:app --reload

Acesse a documentação interativa em:
http://127.0.0.1:8000/docs


👨‍💻 Integrantes
Ryan Fernando Lúcio da Silva - 555924/ Lucas Henrique de Souza Santos - 558241/ Mariana Roberti Neri - 556284

