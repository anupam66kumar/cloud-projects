# Step 1 — Run the Monolith on EC2 (the "before")

Before you migrate anything, you need the thing you're migrating *from*. In this step you run
the bookstore monolith on a single EC2 instance, exactly the way a small team often starts:
one Flask app, one SQLite file, one box. Then you'll name — out loud — the limits that make
serverless attractive. **You can't appreciate the destination until you've felt the start.**

---

## 1.1 What You're Creating

| Thing | Value |
|-------|-------|
| Instance name | `bookstore-monolith` |
| AMI | Amazon Linux 2023 |
| Type | `t3.micro` (free-tier eligible) |
| Inbound | TCP 5000 from your IP (app), 22 from your IP *or* use SSM |
| App | `src/monolith/app.py` (Flask + SQLite) |

> **Why one box on purpose?** The monolith isn't a strawman — it's a perfectly reasonable
> v1. The lesson is *when* its shape stops serving you, not that it was wrong to start here.

---

## 1.2 Console — Launch the Instance

1. **EC2 → Instances → Launch instances.**
2. **Name:** `bookstore-monolith`.
3. **AMI:** Amazon Linux 2023. **Type:** `t3.micro`.
4. **Key pair:** pick one you own (or choose **Proceed without a key pair** if you'll use SSM).
5. **Network settings → Edit → Security group**, add inbound rules:
   | Type | Port | Source |
   |------|------|--------|
   | Custom TCP | 5000 | My IP |
   | SSH | 22 | My IP (skip if using SSM) |
6. **Advanced details → IAM instance profile:** attach a role with
   `AmazonSSMManagedInstanceCore` if you want Session Manager access (no SSH key needed).
7. **Launch instance.** Note the **Public IPv4** once it's running.

> **If the launch fails with "instance type not supported in your requested Availability
> Zone":** some AZs don't offer `t3.micro` — `us-east-1e` is the usual culprit. This bites
> mainly on the CLI, where picking the "first" subnet can land you in that AZ. Either let AWS
> choose (omit the subnet) or pick a different one:
>
> ```bash
> SUBNET=$(aws ec2 describe-subnets \
>   --filters Name=vpc-id,Values=<your-vpc> Name=availability-zone,Values=us-east-1a \
>   --query "Subnets[0].SubnetId" --output text)
> ```
>
> `t3.micro` is fine in `us-east-1a/b/c/d/f`.

---

## 1.3 Install and Run the App

Connect (`ssh ec2-user@<public-ip>` or **EC2 → Connect → Session Manager**), then:

```bash
sudo dnf install -y python3-pip git
python3 -m pip install --user flask==3.1.0

mkdir -p ~/bookstore && cd ~/bookstore
# paste src/monolith/app.py here (scp it, or copy-paste into: nano app.py)

python3 app.py
# * Running on http://0.0.0.0:5000
```

From your laptop, hit it:

```bash
IP=<public-ip>
curl http://$IP:5000/health
curl http://$IP:5000/books
# grab a book id from the output, then:
curl -X POST http://$IP:5000/orders \
  -H 'content-type: application/json' \
  -d '{"book_id":"<paste-id>","qty":2}'
```

You should see the seeded books and a `201` with an order id.

---

## 1.4 Feel the Limits (write these down)

While it's running, reason about each of these — they are the migration's *why*:

| You ask… | Monolith answer | Serverless answer (later) |
|----------|-----------------|----------------------------|
| Orders traffic 10×, catalog flat — scale just orders? | No — scale the whole box | Yes — `bookstore-orders` scales alone |
| Idle overnight — what does it cost? | Full instance-hour, every hour | ~$0 (pay per request) |
| Ship a catalog bug — what breaks? | The whole store (orders too) | Only `bookstore-catalog` |
| Box dies — where's the order data? | In one SQLite file on one disk | In DynamoDB, replicated across AZs |
| Patch the OS — who does it? | You, on a schedule | Nobody — no servers |

> Keep the instance running for now — Step 2 reads its SQLite data to migrate it.

---

## Checkpoint

- [ ] `bookstore-monolith` EC2 instance is **running**
- [ ] `curl http://<ip>:5000/books` returns the three seeded books
- [ ] `POST /orders` returns `201` with an order id
- [ ] You can name at least 3 concrete limits of the monolith shape

---

**Next:** [Step 2 — DynamoDB Tables + Data Migration](./02-dynamodb-tables.md)
