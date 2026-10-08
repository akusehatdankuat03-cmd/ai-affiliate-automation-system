# roadmap_auto_affiliate.md

# AI Affiliate Automation System Roadmap

## Objective
Build an AI-powered product automation system that can:
- discover winning product opportunities from China and other sources
- evaluate product potential based on competition, demand, market signals, and affiliate availability
- validate affiliate commission and product viability on Shopee and/or other marketplace platforms
- collect product media (images/videos)
- shortlist products for human approval
- optionally edit video by removing music or voice
- generate captions and platform-specific content
- schedule posting to Shopee affiliate, TikTok, Instagram, Facebook, and YouTube
- monitor daily ad and content performance
- provide reporting and decision support to the user

This system must support human-in-the-loop approval at critical points:
- candidate shortlisting
- asset validation
- caption revision
- scheduling approval
- final publish approval

---

## 1. System Vision
The platform operates as a multi-stage AI workflow:
1. product research engine scans trend sources and niche markets
2. product filtering and scoring rank product potential
3. marketplace validation checks whether the product exists on Shopee and whether affiliate commission is available
4. media collection downloads product photos and videos
5. review queue lets a human approve or reject products before publishing
6. AI content engine creates caption variants and platform variations
7. scheduling engine manages posting across selected channels
8. monitoring engine tracks performance metrics and creates reports
9. decision loop recommends improvements and next product opportunities

---

## 2. Scope
### In Scope
- China and international product discovery
- Shopee product lookup and affiliate detection
- media collection and asset management
- video pre-processing and editing
- AI caption generation
- multi-platform scheduling
- human approval workflow
- daily performance tracking and reporting

### Out of Scope for Initial MVP
- anti-bot evasion for all target sites
- complete fraud prevention and payment handling
- complete autonomous approval without human oversight
- custom mobile app in phase one
- enterprise role management in phase one

---

## 3. Functional Requirements
### Product Research Module
- accept category and niche input
- support keyword-based search
- search multiple sources including social trends, marketplaces, and discovery tools
- collect titles, prices, category info, visuals, seller metadata, and source URLs
- detect demand and trend velocity
- score products
- save product records with references

### Affiliate Validation Module
- search product on Shopee
- confirm product availability
- check affiliate status and commission metadata
- generate affiliate URL where possible
- mark status as approved, unavailable, pending, or invalid

### Media Acquisition Module
- download product images and videos
- store media with provenance
- maintain version history
- deduplicate files

### Video Editing Module
- trim and crop videos
- remove music or voice when required
- add subtitles or overlays
- export platform-specific versions

### Caption Generator Module
- create multiple caption variants
- generate hook lines, CTAs, hashtags, and platform-specific text
- support revision by human reviewer

### Human Approval Module
- display shortlisted products in review queue
- allow approve, reject, or revise decisions
- track user rationale and timestamps

### Scheduling Module
- schedule posts by date and timezone
- support multiple platforms per campaign
- queue publishing jobs
- maintain retries and failure logs

### Monitoring & Reporting Module
- track views, engagement, clicks, conversions, and revenue
- summarize performance by campaign and platform
- generate daily and weekly reports
- suggest next actions

---

## 4. Recommended Architecture
### High-Level Stack
- Python 3.11+
- FastAPI
- PostgreSQL
- Redis
- Celery
- React / Next.js
- OpenAI / Anthropic
- Playwright / Selenium
- FFmpeg
- AWS S3 or MinIO

### Core Services
- Product Research Service
- Affiliate Validation Service
- Media Acquisition Service
- Editing Service
- Caption Generation Service
- Approval Workflow Service
- Scheduling Service
- Reporting Service

---

## 5. Database Design (Core Tables)
- users
- categories
- products
- product_research_runs
- product_candidates
- affiliate_checks
- media_assets
- content_drafts
- approval_logs
- schedules
- posts
- platform_metrics
- reports

---

## 6. AI Agent Prompt
Use this prompt with your AI coding agent:

"Build an AI-powered affiliate automation system for e-commerce content operations. The system must discover trending products by category/niche, validate products on Shopee, detect affiliate availability, download image/video assets, let a human approve products and captions, generate platform-specific content, schedule posts to Shopee affiliate, TikTok, Instagram, Facebook, and YouTube, and then collect daily performance metrics to generate reports. Use Python FastAPI, PostgreSQL, Redis, Celery, React/Next.js, AI APIs, Playwright/Selenium, FFmpeg, and cloud media storage. Keep human-in-the-loop approval at each critical stage. Build modular architecture, environment configuration, tests, and deployment-ready docs."

---

## 7. MVP Implementation Plan
### Phase 1
- project scaffold
- DB schema
- product research API
- affiliate validation
- approval queue
- media storage
- AI caption generation

### Phase 2
- scheduler
- platform connectors
- video editing flow
- admin dashboard improvements

### Phase 3
- metrics ingestion
- reporting engine
- optimization suggestions
- campaign intelligence

---

## 8. Execution Workflow
1. User enters a category and keywords.
2. System researches and scores products.
3. User approves or rejects products.
4. System validates affiliate availability.
5. Media is downloaded and reviewed.
6. Caption variants are created.
7. User approves final caption or revises it.
8. Scheduler queues posts for selected platforms.
9. Performance is monitored daily.
10. Daily summary report is generated.

---

## 9. Acceptance Criteria
The MVP is successful when:
- a user can input a niche and receive ranked product candidates
- a product can be validated on Shopee and affiliate status displayed
- an approved product can generate media assets
- video can be exported in platform-ready format
- AI generates caption variants
- user can approve content and schedule it
- system publishes to at least one supported platform
- metrics are tracked daily
- a daily report is generated

---

This roadmap is intended as the blueprint for building the AI affiliate automation system incrementally and safely.

