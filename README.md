
# 📰 Projeto de Coleta de Notícias — Web Scraping & API

Este repositório contém dois scripts em Python que automatizam a coleta de notícias:

- 🔍 **Script 1:** Coleta de dados via Web Scraping (usando Selenium).
- 🌐 **Script 2:** Coleta de dados via API pública (GNews API).

Ambos os scripts geram arquivos `.csv` padronizados contendo as notícias obtidas.

---

## 📌 Requisitos

- Python 3.9 ou superior
- Navegador Google Chrome instalado (necessário para o script de Web Scraping)

> Verifique a versão do Python com:
> ```bash
> python --version
> ```

---

## 🚀 Passo a passo para execução

### 1. Clone o repositório

Abra o terminal (Git Bash, CMD ou outro) e execute:

```bash
git clone https://github.com/nagano10/ColetaDadosWeb
```

---

### 2. Instale as dependências

Para ambos os projetos:

1. Acesse a pasta do projeto desejado.
2. Abra o terminal e execute:

```bash
pip install -r requirements.txt
```

---

### 3. Como executar os scripts

#### 3.1 Script de Coleta via API (GNews)

1. Acesse [https://gnews.io/](https://gnews.io/) e cadastre-se para obter sua chave de API gratuita.
2. Crie um arquivo `.env` na raiz do projeto `NewsAPI` com o seguinte conteúdo:

```
GNEWS_API_KEY=sua_chave_aqui
```

3. No terminal, entre na pasta `src` do projeto e execute:

```bash
python main.py
```

4. O arquivo `.csv` com as notícias será salvo automaticamente na pasta `output`.

---

#### 3.2 Script de Web Scraping (G1)

1. No terminal, entre na pasta `src` do projeto de scraping e execute:

```bash
python main.py
```

2. O arquivo `.csv` será salvo na pasta `output`.

---

## 🏗️ Arquitetura e Organização dos Módulos

### 4.1 Estrutura do Script de Coleta via API

O projeto segue uma arquitetura modular com separação de responsabilidades em três camadas principais:

- **API**: conecta-se à GNews API para buscar os dados brutos.
- **Parser**: trata e padroniza os dados recebidos.
- **Saver**: exporta os dados tratados para um arquivo CSV.

O script principal `main.py` orquestra esse fluxo: coleta → tratamento → exportação.  
Essa estrutura modular facilita a manutenção, testes e escalabilidade do código.

> (Ver documentação completa da GNews API [aqui](https://gnews.io/docs/))

---

### 4.2 Estrutura do Script de Web Scraping

O projeto também segue uma arquitetura modular, composta por:

- **Scraper**: utiliza Selenium para acessar e extrair o HTML do site de notícias G1.
- **Parser**: processa o conteúdo bruto extraído e estrutura os dados relevantes (título, resumo, link, data de última modificação).
- **Saver**: salva os dados organizados em um arquivo CSV.

O arquivo `main.py` centraliza a execução do fluxo completo.  
A separação em módulos melhora a legibilidade e permite modificações futuras com mais segurança.

---

## 📂 Estrutura Esperada do Output

Ambos os scripts geram arquivos `.csv` com a mesma estrutura de colunas, como por exemplo:

| title                  | summary                  | link       | publication_last_update              |
|-------------------------|--------------------------|------------|-------------------------------------|
| Manchete da notícia     | Resumo da notícia        | g1.globo.com | 2025-04-29       |

---
