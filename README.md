# AI Affiliate Automation System

AI-powered automation platform for product discovery, affiliate validation, media acquisition, AI content generation, scheduling, and performance reporting for e-commerce and affiliate workflows.

## Overview

This project is designed to help a human operator research winning products, validate affiliate opportunities, collect product media, generate social content, schedule publishing, and monitor daily results across multiple channels.

The system is built around a human-in-the-loop approval workflow so content is reviewed before it goes live. The user decides the target niche, product shortlist, caption direction, publishing schedule, and final publishing approval.

## Core Workflow

1. User selects a category or niche.
2. Product research engine scans multiple sources for candidate products.
3. Product scoring ranks opportunities by product potential and affiliate likelihood.
4. Shopee validation checks whether the product exists and whether affiliate commission is available.
5. Human reviews the shortlist and approves candidates to continue.
6. Media downloader collects product images and videos.
7. Video editor optionally removes music/voice and prepares platform-safe versions.
8. AI caption generator creates multiple caption options.
9. Human approves or revises captions.
10. Scheduler queues posts for selected platforms.
11. Daily metrics pipeline tracks performance and generates reports.

## Supported Platform Goals

- Shopee affiliate
- TikTok
- Instagram
- Facebook
- YouTube Shorts / YouTube

## Key Features

- category and keyword-based product discovery
- product scoring and ranking
- affiliate validation and commission detection
- product shortlist queue for review
- image and video collection
- optional video editing with FFmpeg
- AI-generated captions and hashtags
- human approval before publication
- scheduled multi-platform posting
- daily performance monitoring and summaries
- reporting and optimization recommendations

## Module Structure

```text
ai-affiliate-automation-system/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── workers/
│   │   └── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── alembic/
├── frontend/
│   ├── app/
│   ├── components/
│   └── package.json
├── infra/
│   ├── docker-compose.yml
│   ├── postgres/
│   └── redis/
├── scripts/
│   ├── seed_data.py
│   ├── run_workers.sh
│   └── migrate_db.py
├── tests/
│   ├── unit/
│   └── integration/
├── .env.example
├── .gitignore
├── README.md
├── roadmap_auto_affiliate.md
├── docker-compose.yml
└── Makefile
```

## Tech Stack

### Backend
- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- Celery
- Pydantic

### Frontend
- Next.js or React
- Tailwind CSS

### AI & Content
- OpenAI API
- Anthropic Claude API
- LangChain optional

### Scraping / Automation
- Playwright
- Selenium
- BeautifulSoup
- httpx / aiohttp

### Media Processing
- FFmpeg
- Pillow
- OpenCV
- moviepy

### Analytics
- structured logs
- Prometheus / Grafana optional
- business-level daily reports

## Core Data Entities

- User
- Category
- ProductCandidate
- ProductRecord
- AffiliateCheck
- MediaAsset
- AssetVersion
- ContentDraft
- ApprovalLog
- Schedule
- Post
- PlatformMetric
- Report

## High-Level Architecture

```text
User / Operator
      |
      v
Dashboard / Admin UI
      |
      v
Backend API (FastAPI)
  |---- Product Research Service
  |---- Affiliate Validation Service
  |---- Media Acquisition Service
  |---- Video Editing Service
  |---- Content Generation Service
  |---- Scheduling Service
  |---- Monitoring & Reporting Service
      |
      +---- PostgreSQL
      +---- Redis + Celery
      +---- Object Storage / Filesystem
      +---- External APIs (Shopee, TikTok, Meta, YouTube, AI APIs)
```

## Key Business Rules

- Product must be ranked before reaching shortlist.
- User must approve products before advanced media or scheduling tasks begin.
- Affiliate status must be stored with product provenance.
- Each asset must retain source metadata and status.
- No post is queued without approved content.
- Every scheduled post must carry platform and timezone information.
- Daily performance must be monitored and performance summaries generated.

## Recommended MVP Scope

### Phase 1
- project scaffolding
- database schema
- product research API
- Shopee affiliate validation
- product shortlist review
- asset storage
- AI caption generation

### Phase 2
- scheduler
- platform publishing connectors
- media editing flow
- dashboard improvements

### Phase 3
- metrics ingestion
- reports and optimization recommendations
- smarter ranking logic

## Example AI Agent Prompt

```text
Build an AI-powered affiliate automation system for e-commerce content operations. The system must discover trending products by category/niche, validate products on Shopee, detect affiliate availability, download image/video assets, let a human approve products and captions, generate platform-specific content, schedule posts to Shopee affiliate, TikTok, Instagram, Facebook, and YouTube, and then collect daily performance metrics to generate reports. Use Python FastAPI, PostgreSQL, Redis, Celery, React/Next.js, AI APIs, Playwright/Selenium, FFmpeg, and cloud media storage. Keep human-in-the-loop approval at each critical stage. Build modular architecture, environment configuration, tests, and deployment-ready docs.
```

## Environment Variables

Create a `.env` file from `.env.example` with the following categories:

```env
APP_ENV=development
APP_SECRET=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/affiliate_ai
REDIS_URL=redis://localhost:6379/0

OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

SHOPEE_API_KEY=your_shopee_key
SHOPEE_PARTNER_ID=your_partner_id

TIKTOK_CLIENT_KEY=your_tiktok_client_key
TIKTOK_CLIENT_SECRET=your_tiktok_secret

INSTAGRAM_APP_ID=your_instagram_app_id
INSTAGRAM_APP_SECRET=your_instagram_app_secret

YOUTUBE_API_KEY=your_youtube_key
FACEBOOK_APP_ID=your_facebook_app_id
FACEBOOK_APP_SECRET=your_facebook_app_secret

AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_S3_BUCKET=your_bucket_name
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 4. Start database and Redis

```bash
docker compose up -d postgres redis
```

### 5. Run migrations

```bash
alembic upgrade head
```

### 6. Start API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 7. Start Celery worker

```bash
celery -A app.worker worker --loglevel=info
```

### 8. Start frontend

```bash
cd frontend
npm install
npm run dev
```

## Testing

```bash
pytest
```

or for specific area:

```bash
pytest tests/unit/test_product_scoring.py
pytest tests/integration/test_shopee_validation.py
```

## Example User Flow

```text
User chooses category: Home & Kitchen
User adds keyword: portable blender
System ranks 25 candidate products
User approves 5 products
System validates Shopee affiliate on each product
User approves 3 products
System downloads images and one video asset
AI generates 4 caption variants
User approves one caption and sets a posting schedule
Scheduler publishes to TikTok and Instagram
Daily report shows views, engagement, clicks, and affiliate clicks
System suggests best-performing product angle to repeat next week
```

## Risks & Constraints

- some platforms restrict scraping or publishing automation
- affiliate availability may vary by account and region
- API access may require business verification
- content usage rights must be respected
- scheduling depends on platform policies and account status
- self-hosted automation may require proxy or browser automation support

## Success Criteria

The MVP is successful when a user can:
- choose a niche and discover candidate products
- see affiliate availability and product score
- approve product candidates
- collect media assets
- generate captions and schedule posts
- publish to at least one social platform
- track performance and generate daily summaries

## License

This project is intended for internal workflow development and tailored automation implementation. Add your preferred license file under the project root if you intend to publish it publicly.

## Next Steps

1. build the database schema
2. create product research module
3. add Shopee affiliate validation flow
4. add approval dashboard
5. build media pipeline and editing module
6. add scheduling and posting connectors
7. add reporting

## Project Goal Statement

This project exists to automate the “discovery to publishing” workflow for affiliate and e-commerce content, while keeping the human decision-maker in control of product selection, caption direction, and posting approvals.

---

This README is intended to serve as a project launch document and architecture starter for the AI affiliate automation system.

