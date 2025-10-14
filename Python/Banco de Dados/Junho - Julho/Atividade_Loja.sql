CREATE TABLE loja (
	Tipo VARCHAR(20) PRIMARY KEY,
    Tamanho VARCHAR(20),
    Cor VARCHAR(20),
    Marca VARCHAR(20),
    Preco VARCHAR(20),
    Estoque INT
);

INSERT INTO loja (Tipo, Tamanho, Cor, Marca, Preco, Estoque) VALUES
	('Camiseta', 'GG', 'Preta', 'NIKE', 'R$99,90', 500),
    ('Calça', 'GG', 'Caqui', 'BAW', 'R$149,99', 450),
    ('Sueter', 'GG', 'Branco', 'ARAMIS', 'R$299,90', 250);
    