
# On Anupam Laptop
# Cloud Hands-On Projects

A collection of **37 hands-on projects** designed for students to build real-world cloud skills through guided, step-by-step exercises — mostly in their own AWS accounts, plus a set of Google Cloud labs and local Kubernetes labs.

> 🚀 **First time here? Start with [SETUP.md](SETUP.md)** — it installs every tool you need
> (AWS CLI, Python, Git, Docker, …) with steps for **Linux, macOS, and Windows**.

> 🧭 **Looking for a specific project?** Browse the full filterable index in
> **[PROJECT-CATALOG.md](PROJECT-CATALOG.md)** — sort by level, cloud/tech, domain, time, and cost.
> The tables below group the same projects by theme and series.

## Projects

### IAM & Security

| Project | Services | Description |
|---------|----------|-------------|
| [IAM Roles & Policies](projects/intermediate/aws/aws-iam-roles-and-policies/README.md) | IAM, STS, Lambda, EC2, ECS | Master trust vs. permission policies by building six real-world roles: user-assumed via CLI/STS, Lambda/EC2/ECS service roles, cross-account with External ID, and GitHub OIDC federation |

### Storage & CDN

| Project | Services | Description |
|---------|----------|-------------|
| [S3 + CloudFront Static Website](projects/beginner/aws/aws-s3-cloudfront-static-website/README.md) | S3, CloudFront, OAC, IAM | Host a static site in a private S3 bucket served globally over HTTPS via CloudFront; learn origin access control, default root object, custom error pages, caching, and cache invalidation |

### Messaging & Queuing

| Project | Services | Description |
|---------|----------|-------------|
| [Event-Driven Messaging with SNS & SQS](projects/beginner/aws/aws-sqs-sns-messaging/README.md) | SNS, SQS, IAM | Build a fanout messaging system using pub/sub architecture |
| [Lambda Triggered by SQS with SNS Notification](projects/intermediate/aws/aws-lambda-sqs-sns-trigger/README.md) | Lambda, SQS, SNS, IAM, CloudWatch | Build a serverless order-processing pipeline: SQS triggers Lambda, Lambda publishes results to SNS |

### Lambda Series (Beginner → Advanced)

Work through these four projects in order. Each builds on the previous.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [Lambda Basics](projects/beginner/aws/aws-lambda-basics/README.md) | Lambda, IAM, CloudWatch | Deploy your first Lambda, understand handlers, invoke via Console/CLI/Boto3, and read CloudWatch Logs |
| 2 | [Lambda with S3 Event Processing](projects/beginner/aws/aws-lambda-s3-event-processing/README.md) | Lambda, S3, IAM, CloudWatch | Trigger Lambda automatically on S3 uploads; process text/CSV files and write results to a destination bucket |
| 3 | [Lambda Layers](projects/beginner/aws/aws-lambda-layers/README.md) | Lambda, IAM, CloudWatch | Package third-party libraries (`requests`, `pandas`) as reusable Lambda Layers; attach multiple layers to one function |
| 4 | [Lambda Troubleshooting & Boto3 Automation](projects/intermediate/aws/aws-lambda-troubleshooting-monitoring/README.md) | Lambda, S3, EC2, SQS, CloudWatch, Log Insights | Debug 8 failure scenarios, master Log Insights queries, configure DLQs, and automate EC2/S3/SQS with Boto3 |

### Lambda Automation Series (Beginner)

Three short, beginner-friendly projects that all share one idea: **run Lambda on a schedule
with Amazon EventBridge** (a serverless cron job). Start with Project 1 — it teaches the
scheduling pattern the other two reuse to automate real chores. Each is fully hands-on with a
`DRY_RUN` safety switch where it matters.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [Lambda on a Schedule with EventBridge](projects/beginner/aws/aws-lambda-eventbridge-scheduled/README.md) | Lambda, EventBridge, CloudWatch, SNS | Learn the scheduling pattern itself: an EventBridge `rate`/`cron` rule fires a heartbeat Lambda that logs and (optionally) emails you via SNS; add a missed-run alarm |
| 2 | [Scheduled EC2 Start/Stop](projects/beginner/aws/aws-lambda-ec2-start-stop-scheduler/README.md) | Lambda, EventBridge, EC2, IAM, CloudWatch | Save money: two schedules pass `{"action":"stop"}` / `{"action":"start"}` to one tag-driven Lambda that powers idle EC2 off overnight — with a tag-gated IAM policy and `DRY_RUN` |
| 3 | [Scheduled S3 Housekeeping](projects/beginner/aws/aws-lambda-s3-housekeeping/README.md) | Lambda, EventBridge, S3, IAM, CloudWatch | Keep a bucket tidy: a daily Lambda archives (or deletes) objects older than a retention window using a paginator, with `archive`-before-`delete` safety and a Lambda-vs-Lifecycle discussion |

### ECS & Fargate Series (Beginner → Advanced)

Work through these two projects in order. Project 1 covers fundamentals; Project 2 builds a production-grade deployment.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [ECS Fargate Basics](projects/intermediate/aws/aws-ecs-fargate-basics/README.md) | ECS, Fargate, ECR Public, IAM, CloudWatch | Containerize a Flask app, push to ECR Public, run as a Fargate task — understand ECS fundamentals |
| 2 | [ECS Fargate Advanced](projects/advanced/aws/aws-ecs-fargate-advanced/README.md) | ECS, Fargate, ECR Public, ALB, VPC, IAM, CloudWatch, Auto Scaling | Production-grade deployment: VPC networking, Application Load Balancer, rolling deployments, Auto Scaling, Container Insights, Docker Compose |

### Web App Architecture — Native vs. Serverless (Beginner → Advanced)

Build the **same monitored web application twice** — once on native AWS, once serverless —
to compare cost, operations, scaling, and observability. Each is a complete, end-to-end
cloud architecture with monitoring, alerting, audit, and a GitHub Actions CI/CD pipeline.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [EC2 + VPC Monitored Web App](projects/advanced/aws/aws-ec2-vpc-monitored-webapp/README.md) | EC2, VPC, ALB, Auto Scaling, CloudWatch, SNS, CloudTrail, IAM, SSM, GitHub Actions | Full native architecture: custom VPC (public/private subnets, NAT), EC2 fleet behind an ALB with Auto Scaling, CloudWatch metrics/alarms/dashboards, SNS email alerts, CloudTrail audit, Boto3 monitoring automation, and an OIDC→SSM deploy pipeline |
| 2 | [Serverless Monitored Web App](projects/intermediate/aws/aws-serverless-monitored-webapp/README.md) | API Gateway, Lambda, CloudWatch, SNS, CloudTrail, IAM, GitHub Actions | The same app with no servers: API Gateway + Lambda, the same CloudWatch/SNS/CloudTrail observability, Boto3 automation, and an OIDC→`update-function-code` pipeline — with a side-by-side native-vs-serverless comparison |

### API Gateway Series (Beginner → Intermediate)

Two projects that build an API on **API Gateway + Lambda**, then teach the part most tutorials
skip: **how to ship a new version safely.** Each covers **rolling**, **canary**, and
**blue-green** deployments using only **native** Lambda + API Gateway primitives — no
CodeDeploy — so you can see exactly what each strategy does. Build both to compare REST vs HTTP
APIs and gateway-level vs alias-level deploys.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [API Gateway REST API + Lambda](projects/intermediate/aws/aws-api-gateway-rest-lambda/README.md) | API Gateway (REST), Lambda, IAM, CloudWatch | Build a Quotes API with REST resources/methods + proxy integration and a deployment stage, then ship v2 three ways: **rolling** (weighted Lambda alias), **canary** (API Gateway's native gateway-level canary release), and **blue-green** (instant stage-variable flip + rollback) |
| 2 | [API Gateway HTTP API + Lambda + DynamoDB](projects/intermediate/aws/aws-api-gateway-dynamodb-crud/README.md) | API Gateway (HTTP), Lambda, DynamoDB, IAM, CloudWatch | Build a full CRUD Tasks API (GET/POST/PUT/DELETE) on the cheaper HTTP API with durable DynamoDB state, then do **rolling / canary / blue-green** entirely at the **Lambda-alias** level (HTTP API has no gateway canary) — repointing the integration for an atomic cutover |

> The existing [Serverless Monitored Web App](projects/intermediate/aws/aws-serverless-monitored-webapp/README.md) also
> ships a [deployment-strategies.md](projects/intermediate/aws/aws-serverless-monitored-webapp/deployment-strategies.md)
> guide to apply these same techniques to that app.

### Optimization & Recovery Series

Three projects on one theme: **keeping cloud systems lean and resilient.** Two cover AWS, one
covers Kubernetes. Each is hands-on, with a safety switch (`DRY_RUN` / verify-before-act) wherever
something can change or delete infrastructure. Together they cover rightsizing compute,
disaster-recovery for databases, and both halves at once on Kubernetes.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [EC2 Compute Rightsizing](projects/intermediate/aws/aws-compute-rightsizing/README.md) | Lambda, EventBridge, EC2, CloudWatch, SNS, Compute Optimizer | **Optimization.** A scheduled Lambda reads each instance's CloudWatch CPU, labels it idle/over-provisioned/right-sized, emails an SNS report, and (opt-in, tag-gated) resizes via stop→modify→start — then compares your logic to AWS Compute Optimizer |
| 2 | [RDS Disaster Recovery](projects/advanced/aws/aws-rds-disaster-recovery/README.md) | RDS, EC2 (SG), KMS, two regions | **Recovery.** Seed a MySQL DB, then recover it four ways — point-in-time restore, manual snapshot, cross-region snapshot copy, and a cross-region read-replica failover — measuring RPO/RTO for each |
| 3 | [Kubernetes Optimization & Recovery](projects/intermediate/kubernetes/k8s-optimization-and-recovery/README.md) | kind/minikube, metrics-server, HPA, Velero, MinIO | **Both, on Kubernetes (local, $0).** Right-size with requests/limits, autoscale with an HPA, self-heal with probes + a PDB, then back up the namespace with Velero, delete it, and restore it |

### Migration Series

Three projects on one theme: **moving a workload from one architecture to a better-fit one**,
each mapped to AWS's **6 R's** (Refactor, Refactor, Replatform) and driven by the **Strangler
Fig** / **full-load + CDC** patterns. Every step is manual (Console + CLI) so you see each moving
part. Each README spells out *why* the target architecture is better, *what type* of migration it
is, and *which principles* apply.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [Monolith → Serverless](projects/advanced/aws/aws-monolith-to-serverless-migration/README.md) | EC2, Lambda, API Gateway (HTTP), DynamoDB, IAM | **Refactor.** Run a Flask + SQLite monolith on EC2, then strangle it route-by-route into two domain Lambdas (catalog/orders) + DynamoDB behind an HTTP API — migrating data and traffic with no big-bang cutover, then retire the EC2 box |
| 2 | [Monolith → Microservices on EKS](projects/advanced/kubernetes/eks-monolith-to-microservices/README.md) | EKS, ECR, ELB, EC2, IAM | **Refactor.** Decompose a single container into `catalog`/`orders`/`frontend` microservices on Kubernetes — service-to-service DNS, ConfigMaps, probes, **HPA**, rolling updates, self-healing — then cut over from the monolith. ⚠️ Real EKS cost; $0 local `kind` alternative included |
| 3 | [Database Migration with DMS](projects/advanced/aws/aws-database-migration-dms/README.md) | DMS, RDS (MySQL), EC2, VPC, IAM | **Replatform.** Migrate a live self-managed MySQL to managed RDS with **full load + CDC** for near-zero downtime — replication instance, endpoints, validation, and a clean parity-checked cutover (RPO/RTO) |

### EKS Projects

These **Amazon EKS** projects (under `projects/*/kubernetes/`) focus on security, identity, and
operations. ⚠️ Each runs a real EKS control plane (**$0.10/hr**, no free tier) — delete the cluster
the same day. New to Kubernetes? Do the free local lab in
[k8s-optimization-and-recovery](projects/intermediate/kubernetes/k8s-optimization-and-recovery/README.md) first.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [IRSA — Service Account Access](projects/advanced/kubernetes/eks-irsa-service-account-access/README.md) | EKS, IAM, STS, OIDC, S3 | Give a pod AWS permissions via a ServiceAccount with **IRSA** (OIDC trust, zero stored keys) end-to-end — cluster OIDC provider, trust + permission policies, SA annotation, verified pod — then scope a teammate to one namespace with **RBAC + access entries**. Rich diagrams explaining *what OIDC/IRSA/ServiceAccounts are* and the full creation flow |

### GCP Networking Projects

Two **Google Cloud** labs (under `projects/*/gcp/`) — networking on GCP instead of AWS.
Each step has both a **Console** and a **gcloud CLI** path. New to GCP? The beginner project's
Step 1 installs and authenticates the CLI.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [VPC & Firewall Basics](projects/beginner/gcp/gcp-vpc-firewall-basics/README.md) | VPC, Subnets, Firewall, Compute Engine | **Beginner.** Install & authenticate the gcloud CLI, then build a custom VPC with two subnets, three firewall rules, and two VMs — and prove it works with SSH, private ping, a web page, and watching the firewall block unopened ports |
| 2 | [HTTP Load Balancer & Autoscaling](projects/intermediate/gcp/gcp-http-lb-autoscaling/README.md) | VPC, Cloud NAT, Instance Templates, MIG, Health Checks, Application LB | **Intermediate.** Put **private** autoscaling VMs behind a **global HTTP load balancer** with Cloud NAT for egress, then load-test to scale out and delete a VM to watch the managed instance group self-heal |

### GCP IAM, Storage & Databases Projects

Four **Google Cloud** projects (under `projects/*/gcp/`) covering IAM, Cloud Storage, and managed
databases in depth. A single fictional retailer, **Meridian Retail**, runs through all four — do
them in order. Assumes the gcloud CLI is already installed (see the networking track above or
[SETUP.md](SETUP.md)).

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [IAM & Storage Fundamentals](projects/beginner/gcp/gcp-iam-storage-fundamentals/README.md) | IAM, Service Accounts, Cloud Storage | **Beginner.** Principals, policy anatomy, basic vs. predefined roles, a least-privilege service account, and a documents bucket — proven with **key-less service account impersonation** instead of a downloaded key |
| 2 | [Storage Security & Lifecycle](projects/intermediate/gcp/gcp-storage-security-lifecycle/README.md) | Cloud Storage, Cloud KMS, IAM Conditions, Custom Roles | **Intermediate.** A custom IAM role scoped further with an IAM Condition, versioning + lifecycle tiering, CMEK encryption, keyless signed URLs vs. a public static-website bucket, and bucket logging |
| 3 | [Cloud SQL Managed Database](projects/intermediate/gcp/gcp-cloud-sql-managed-database/README.md) | Cloud SQL, IAM Database Auth | **Intermediate.** Retire an on-prem MySQL box onto managed Cloud SQL — IAM database authentication, automated backups, a point-in-time-recovery drill, and a read replica |
| 4 | [Databases at Scale & Workload Identity](projects/advanced/gcp/gcp-databases-workload-identity/README.md) | Firestore, Memorystore, Secret Manager, Workload Identity Federation | **Advanced.** Firestore for real-time carts, Memorystore for caching, Secret Manager for credentials, and **Workload Identity Federation** for a keyless GitHub Actions deploy — plus a Cloud SQL/Firestore/Bigtable/Spanner/Memorystore decision matrix |

### GCP App Delivery Projects

Two **Google Cloud** projects (under `projects/*/gcp/`) covering how containers get **built, stored,
and shipped** on GCP — from a single `gcloud` deploy to a managed continuous-delivery pipeline. Do
them in order; the second reuses the first's image. Assumes the gcloud CLI is already installed.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [Cloud Run & Artifact Registry](projects/beginner/gcp/gcp-cloud-run-artifact-registry/README.md) | Cloud Build, Artifact Registry, Cloud Run | **Beginner.** Build a Flask container with **Cloud Build**, push it to **Artifact Registry**, and deploy it to **Cloud Run** (scale-to-zero HTTPS) — then ship a v2 and use revisions + traffic splitting to canary and roll back |
| 2 | [Cloud Deploy Pipeline](projects/intermediate/gcp/gcp-cloud-deploy-pipeline/README.md) | Cloud Deploy, Cloud Run, Cloud Build, Artifact Registry, Skaffold | **Intermediate.** Wrap that image in a **Cloud Deploy** delivery pipeline that promotes one immutable artifact through **staging → prod** with a manual **approval gate** and a one-command **rollback** — build once, deploy many |

### GCP Serverless Projects (Beginner → Advanced)

Three **Google Cloud** projects (under `projects/*/gcp/`) building the **Meridian Retail** order
backend on serverless primitives — from a single HTTP function to a full multi-step orchestration.
Do them in order; each layers on the last. The GCP counterpart to this repo's AWS **Lambda series**.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [Cloud Functions Basics](projects/beginner/gcp/gcp-cloud-functions-basics/README.md) | Cloud Functions (2nd gen), Cloud Scheduler, Cloud Logging | **Beginner.** Deploy a Python HTTP function (no `Dockerfile` — buildpacks), call it over HTTPS, reconfigure it with env vars, read **structured logs**, and put it on a **Cloud Scheduler** cron. Learn why a 2nd-gen function *is* a Cloud Run service |
| 2 | [Event-Driven Functions](projects/intermediate/gcp/gcp-event-driven-functions-pubsub/README.md) | Cloud Functions, Eventarc, Pub/Sub, Firestore, Cloud Storage | **Intermediate.** A file dropped in a bucket fires **Eventarc → a function → Firestore → Pub/Sub → a second function**. Teaches the Eventarc trust chain, CloudEvents, fan-out, at-least-once delivery + idempotency, and dead-letter topics |
| 3 | [Serverless Orchestration](projects/advanced/gcp/gcp-serverless-workflows-orchestration/README.md) | Cloud Workflows, Cloud Functions, Cloud Tasks, API Gateway | **Advanced.** Coordinate five functions into an **order-fulfillment workflow** with retries, a **saga** auto-refund on failure, async shipping via **Cloud Tasks**, and a public **API Gateway** front door — the full identity chain wired hop by hop |

### Docker Projects

Local, **$0** container labs (under `projects/*/docker/`) — no cloud account needed. Every step gives
both raw `docker` commands and the Docker Compose equivalent.

| # | Project | Services | Description |
|---|---------|----------|-------------|
| 1 | [Networking Basics — Two Flask Containers](projects/beginner/docker/docker-network-flask-basics/README.md) | Docker, Docker Compose, Bridge Networks, Flask | **Beginner.** Run a `frontend` container that calls a `backend` by name — watch name resolution **fail** on the default bridge, **fix it** with a user-defined network (`docker network create`), then reproduce the whole thing with `docker compose`. Teaches bridge vs. user-defined networks and Docker's embedded DNS |
| 2 | [Networks & Storage — Persistent Notes App](projects/intermediate/docker/docker-networks-storage-notes/README.md) | Docker, Docker Compose, Networks, Volumes, tmpfs, Flask | **Intermediate.** A public `edge` gateway fronts a private, stateful `api` across **two networks** (one `internal`, no egress). Prove the isolation, persist data to a **named volume** (survives container removal), use a **read-only bind mount** + **tmpfs**, and **back up / restore** the volume through simulated data loss |

---

## How This Repo Is Organized

Projects are grouped by **level**, then by **cloud or core technology**:

```
projects/<level>/<cloud-or-tech>/<project-name>/
          │        │
          │        └─ aws · gcp · azure · kubernetes · terraform · …
          └─ beginner · intermediate · advanced
```

The full, filterable index lives in **[PROJECT-CATALOG.md](PROJECT-CATALOG.md)** (by level, cloud,
domain, time, and cost). EKS/Kubernetes projects are grouped under `kubernetes/` by their primary
skill rather than under `aws/`.

Each project follows a consistent internal layout:

```
<project-name>/
├── README.md           # Overview, architecture (Mermaid diagrams), steps, cost, cleanup
├── Dockerfile          # (container projects) How to build the image
├── steps/              # Numbered, sequential step files — the last one is always cleanup
├── src/                # Application source code
├── troubleshooting.md  # Error → Cause → Fix
└── challenges.md       # Extension tasks
```

See [docs/templates/project-template.md](docs/templates/project-template.md) for the full layout
spec and which files are mandatory vs. optional.

## Prerequisites (All Projects)

- An active AWS account with console access (or, for the [GCP projects](PROJECT-CATALOG.md), a
  Google Cloud account with billing linked)
- A user or role with sufficient permissions (each project specifies exactly what's needed)
- Basic familiarity with the AWS Management Console (the GCP projects assume none — they start by
  installing the `gcloud` CLI)
- The required tooling installed on your laptop — see **[SETUP.md](SETUP.md)** for
  AWS CLI, gcloud CLI, Python, Git, Docker, and more, with **Linux / macOS / Windows** instructions

## Contributing a New Project

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the full guide — folder naming, required files,
diagram and cleanup requirements, and the PR checklist. In short:

1. Add your project under `projects/<level>/<cloud-or-tech>/<kebab-name>/` (e.g.
   `projects/beginner/aws/aws-s3-static-website/`)
2. Copy the templates in [docs/templates/](docs/templates/) and follow the standard layout
3. Add a row to [PROJECT-CATALOG.md](PROJECT-CATALOG.md) (and the relevant themed table above)
4. Keep steps atomic — one concept per file, with cleanup always last
