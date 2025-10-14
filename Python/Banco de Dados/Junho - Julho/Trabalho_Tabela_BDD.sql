-- CURSOS OFERECIDOS POR UMA EMPRESA FICTICIA:
CREATE TABLE cursos (
	Titulo VARCHAR(100) PRIMARY KEY,
	Descricao VARCHAR(100),
	Categoria VARCHAR(20),
	Duracao VARCHAR(50),
	Nivel VARCHAR(20),
	Preco VARCHAR(20) 
);

INSERT INTO cursos (Titulo, Descricao, Categoria, Duracao, Nivel, Preco) VALUES

	('Analise e Desenvolvimento de Sistemas', 'Back-end|Front-end', 'Tecnologia', '3000H', 'Tecnólogo', 'R$1.850,00'),
    ('Enfermagem', 'Como retirar Sangue', 'Saúde', '50H', 'Certificação', 'R$50,00' ),
    ('Educação Física', 'Orientador Escolar', 'Esporte', '2000H', 'Técnico', "R$1.320,00"),
    ('Administração', 'Gestão de Empresas e Pessoas', 'Negócios', '1800H', 'Tecnólogo', 'R$1.500,00'),
    ('Design Gráfico', 'Criação de Identidade Visual e Layouts', 'Artes', '1200H', 'Certificação', 'R$980,00');

=====================================================================================================================================
-- DADOS DOS 5 INSTRUTORES E SUAS ÁREAS DE ATUAÇÃO:
CREATE TABLE instrutores (
    Nome VARCHAR(40),
    Email VARCHAR(40),
    Telefone VARCHAR(20) PRIMARY KEY,
    Especialidade VARCHAR(100)
);

INSERT INTO instrutores (Nome, Email, Telefone, Especialidade) VALUES

    ('Mariana Silva', 'mariana.silva@exemplo.com', '(11) 98877-6655', 'Desenvolvimento Back-end'),
    ('Carlos Eduardo', 'carlos.eduardo@exemplo.com', '(21) 97766-5544', 'Enfermagem Geral'),
    ('Fernanda Costa', 'fernanda.costa@exemplo.com', '(31) 96655-4433', 'Educação Física Escolar'),
    ('Ricardo Lima', 'ricardo.lima@exemplo.com', '(41) 95544-3322', 'Administração de Empresas'),
    ('Juliana Rocha', 'juliana.rocha@exemplo.com', '(51) 94433-2211', 'Design de Marcas e Layouts');

=====================================================================================================================================
-- DADOS DE ALUNOS INSCRITOS NOS CURSOS E SEUS STATUS ATUAL:
CREATE TABLE inscritos (
    Nome_Aluno VARCHAR(30),
    Email_Aluno VARCHAR(30) PRIMARY KEY,
    Id_Curso VARCHAR(30),
    Data_Inscricao DATE,
    Status_Curso VARCHAR(30)
);

INSERT INTO inscritos (Nome_Aluno, Email_Aluno, Id_Curso, Data_Inscricao, Status_Curso) VALUES

    ('Lucas Andrade', 'lucas.andrade@aluno.com', 'ADS', '2025-06-15', 'Ativo'),
    ('Beatriz Nunes', 'beatriz.nunes@aluno.com', 'ADM', '2025-06-20', 'Concluído'),
    ('Thiago Ramos', 'thiago.ramos@aluno.com', 'ADS', '2025-06-25', 'Ativo'),
    ('Ana Paula Mendes', 'ana.mendes@aluno.com', 'ENF', '2025-07-01', 'Ativo'),
    ('Rafael Souza', 'rafael.souza@aluno.com', 'ADM', '2025-07-02', 'Cancelado');

