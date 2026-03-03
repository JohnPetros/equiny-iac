import pulumi
import pulumi_gcp as gcp


def create_github_wif(project_id: str, github_owner: str, github_repo: str):
    pool = gcp.iam.WorkloadIdentityPool(
        "github-pool",
        project=project_id,
        workload_identity_pool_id="github-pool",
        display_name="GitHub Actions Pool",
    )

    provider = gcp.iam.WorkloadIdentityPoolProvider(
        "github-provider",
        project=project_id,
        workload_identity_pool_id=pool.workload_identity_pool_id,
        workload_identity_pool_provider_id="github-provider",
        display_name="GitHub Actions Provider",
        attribute_mapping={
            "google.subject": "assertion.sub",
            "attribute.repository": "assertion.repository",
            "attribute.repository_owner": "assertion.repository_owner",
            "attribute.ref": "assertion.ref",
        },
        oidc={
            "issuer_uri": "https://token.actions.githubusercontent.com",
        },
        attribute_condition=f"assertion.repository == '{github_owner}/{github_repo}'",
    )

    principal = pulumi.Output.all(pool.name).apply(
        lambda args: (
            f"principalSet://iam.googleapis.com/{args[0]}/attribute.repository/{github_owner}/{github_repo}"
        )
    )

    return pool, provider, principal
