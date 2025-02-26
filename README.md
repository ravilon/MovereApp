# MovereApp

Passo a Passo para Configuração do Ambiente Local

## 1. Clonar o Repositório
	Abra um terminal e execute o seguinte comando para clonar o projeto:
 
	### comando bash
	git clone https://github.com/ravilon/MovereApp.git
	cd MovereApp

## 2. Criar e Ativar um Ambiente Virtual
	Para evitar conflitos de dependências, crie um ambiente virtual Python:
	
 	No Windows (cmd ou PowerShell):

	### comando bash
	*python -m venv venv
	*venv\Scripts\activate
	No Linux/macOS:

	### comando bash
	python3 -m venv venv
	source venv/bin/activate
	
 	Se o ambiente for ativado corretamente, o prompt do terminal mostrará (venv) antes do caminho atual.

	##3. Instalar Dependências
	Instale as dependências listadas no requirements.txt dentro da pasta API:

	### comando bash
	pip install -r API/requirements.txt
	
 	##4. Configurar Variáveis de Ambiente
	O arquivo .env já está presente dentro da pasta API. Edite-o e adicione ou modifique as seguintes variáveis conforme necessário:

		FLASK_DEBUG = "True"
		FLASK_ENV = "development"
		FIRESTORE = ''  # Insira aqui as credenciais do Firebase
		Caso não tenha o arquivo .env ou ele não contenha essas variáveis, crie-as manualmente ou copie de um arquivo modelo, caso haja (.env.example).

	##5. Executar a API
	A API pode ser iniciada executando o script APIMain.py, que instancia a aplicação utilizando o create_app().

	Navegue até a pasta API:

	### comando bash
	cd API
 
	Execute a API com o seguinte comando:

	### comando bash
	python APIMain.py
	Isso iniciará a aplicação Flask com a configuração correta.

Agora seu ambiente local está configurado corretamente e pronto para rodar a API! 🚀

