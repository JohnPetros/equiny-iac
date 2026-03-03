import os
from pathlib import Path

import pulumi
from dotenv import load_dotenv


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[3] / ".env"
    load_dotenv(env_path)


class AppConfig:
    def __init__(self):
        load_env()

        self.project_id = self._require_env("PROJECT_ID")
        self.region = os.getenv("REGION", "southamerica-east1")
        self.gar_repository = os.getenv("GAR_REPOSITORY", "equiny")
        self.cloud_run_service = os.getenv("CLOUD_RUN_SERVICE", "equiny-server")

        self.github_owner = self._require_env("GITHUB_OWNER")
        self.github_repo = self._require_env("GITHUB_REPO")

        self.app_secrets = {
            "host": pulumi.Output.secret(os.getenv("HOST", "0.0.0.0")),
            "port": pulumi.Output.secret(os.getenv("PORT", "8080")),
            "database-url": pulumi.Output.secret(self._require_env("DATABASE_URL")),
            "redis-url": pulumi.Output.secret(self._require_env("REDIS_URL")),
            "inngest-signing-key": pulumi.Output.secret(
                self._require_env("INNGEST_SIGNING_KEY")
            ),
            "jwt-secret": pulumi.Output.secret(self._require_env("JWT_SECRET")),
            "supabase-url": pulumi.Output.secret(self._require_env("SUPABASE_URL")),
            "supabase-key": pulumi.Output.secret(self._require_env("SUPABASE_KEY")),
            "supabase-storage-bucket": pulumi.Output.secret(
                self._require_env("SUPABASE_STORAGE_BUCKET")
            ),
            "onesignal-app-id": pulumi.Output.secret(
                self._require_env("ONESIGNAL_APP_ID")
            ),
            "onesignal-api-key": pulumi.Output.secret(
                self._require_env("ONESIGNAL_API_KEY")
            ),
            "email-verification-secret": pulumi.Output.secret(
                self._require_env("EMAIL_VERIFICATION_SECRET")
            ),
            "equiny-server-url": pulumi.Output.secret(
                self._require_env("EQUINY_SERVER_URL")
            ),
            "resend-api-key": pulumi.Output.secret(self._require_env("RESEND_API_KEY")),
            "resend-sender-email": pulumi.Output.secret(
                self._require_env("RESEND_SENDER_EMAIL")
            ),
        }

    def _require_env(self, name: str) -> str:
        value = os.getenv(name)
        if not value:
            raise ValueError(f"Variável obrigatória ausente no .env: {name}")
        return value
