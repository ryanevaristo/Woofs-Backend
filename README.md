# Woofs-Backend

- Cadastro de cachorro []
    - Email
    - Raça
    - Nome
    - Fotos
    - Descrição
    - Interesses
    - Sexo
    - Vacinação

- Permitir localização do cachorro []
    
- Chat real time se der match []

- Limitar quantidade de likes diários (versão gratuita) []

- Superlike limitados (versão gratuita) []



Funcionalidades Futuras:

- Cadastro de Petshops []

- Desconto para cruzamentos no Petshop []

- Disponibilizar Petshops mais próximos aos usuários []


Requisitos Técnicos:
    - Migrations Enviroments: Alembic
        - scripts: 
                - alembic upgrade head,
                - alembic revision -m "Add a column"
        - mais sobre: https://alembic.sqlalchemy.org/en/latest/tutorial.html
     - serviço: Restfull
    - framework: Fastapi
    - scripts: uvicorn main:app --reload
    
    
