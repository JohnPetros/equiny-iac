<h1 align="center">☁️ Equiny IaC</h1>

Infraestrutura como codigo do **Equiny** em **GCP**, desenvolvida com **Pulumi + Python**. O projeto provisiona recursos essenciais para deploy via GitHub Actions, execucao em Cloud Run e gerenciamento seguro de segredos.

## 🚀 Visao Geral

Este repositorio automatiza a criacao e configuracao da base de infraestrutura do backend, incluindo:

- **Artifact Registry:** repositorio Docker para imagens da aplicacao.
- **Secret Manager:** criacao de segredos da aplicacao a partir de variaveis de ambiente.
- **Service Accounts:** contas separadas para deploy (CI/CD) e runtime (Cloud Run).
- **Workload Identity Federation:** autenticacao do GitHub Actions sem chave estatica.
- **IAM:** permissoes minimas para deploy, impersonation e leitura de segredos.
- **Outputs de Stack:** exportacao de identificadores importantes para pipelines.

## 🛠 Tech Stack

- **Linguagem:** [Python](https://www.python.org)
- **IaC:** [Pulumi](https://www.pulumi.com)
- **Cloud Provider:** [Google Cloud Platform (GCP)](https://cloud.google.com)
- **SDK Cloud:** [pulumi-gcp](https://www.pulumi.com/registry/packages/gcp)
- **Ambiente Python:** [uv](https://docs.astral.sh/uv)
- **Configuracao local:** [python-dotenv](https://pypi.org/project/python-dotenv)

## 🏗 Arquitetura

O projeto segue uma organizacao modular por dominio de infraestrutura em `src/equiny/gcp`:

- **`config.py`**: carrega `.env` e valida variaveis obrigatorias.
- **`artifacts.py`**: provisiona o Artifact Registry.
- **`secrets.py`**: cria segredos e versoes no Secret Manager.
- **`service_accounts.py`**: cria service accounts de deploy e runtime.
- **`workload_identity.py`**: cria pool/provider para GitHub OIDC.
- **`iam.py`**: aplica bindings e permissoes IAM.
- **`outputs.py`**: exporta valores da stack.
- **`stack.py`**: orquestra todo o provisionamento.

## 📂 Estrutura do Projeto

```bash
.
├── src/
│   ├── equiny/
│   │   ├── __main__.py           # Entry point do Pulumi
│   │   └── gcp/
│   │       ├── artifacts.py
│   │       ├── config.py
│   │       ├── iam.py
│   │       ├── outputs.py
│   │       ├── secrets.py
│   │       ├── service_accounts.py
│   │       ├── stack.py
│   │       └── workload_identity.py
│   └── pulumi/
│       ├── Pulumi.yaml           # Definicao do projeto Pulumi
│       └── Pulumi.prod.yaml      # Configuracao da stack prod
├── pyproject.toml
└── README.md
```

## ⚙️ Configuracao e Instalacao

### Pre-requisitos

- Python 3.13+
- [uv](https://docs.astral.sh/uv)
- [Pulumi CLI](https://www.pulumi.com/docs/iac/download-install)
- Acesso ao projeto GCP com permissoes para IAM, Secret Manager e Artifact Registry

### Passo a Passo

1. **Clone o repositorio:**

```bash
git clone <url-do-repositorio>
cd equiny-iac
```

2. **Instale as dependencias:**

```bash
uv sync
```

3. **Configure o ambiente (`.env`):**

```bash
PROJECT_ID=equiny
REGION=us-east1
GAR_REPOSITORY=equiny
CLOUD_RUN_SERVICE=equiny-server
GITHUB_OWNER=JohnPetros
GITHUB_REPO=equiny-server

DATABASE_URL=...
REDIS_URL=...
INNGEST_SIGNING_KEY=...
JWT_SECRET=...
SUPABASE_URL=...
SUPABASE_KEY=...
SUPABASE_STORAGE_BUCKET=...
ONESIGNAL_APP_ID=...
ONESIGNAL_API_KEY=...
EMAIL_VERIFICATION_SECRET=...
EQUINY_SERVER_URL=...
RESEND_API_KEY=...
RESEND_SENDER_EMAIL=...
```

4. **Selecione a stack e rode preview/up:**

```bash
uv run pulumi -C src/pulumi stack select prod
uv run pulumi -C src/pulumi preview
uv run pulumi -C src/pulumi up
```

## 📦 Outputs principais

A stack exporta, entre outros:

- `gcpProjectId`
- `gcpRegion`
- `garLocation`
- `garRepository`
- `cloudRunService`
- `workloadIdentityProvider`
- `githubDeployServiceAccount`
- `cloudRunRuntimeServiceAccount`

## 📝 Licenca

Uso interno do projeto **Equiny**.
