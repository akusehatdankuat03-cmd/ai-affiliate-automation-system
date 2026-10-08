# AI Agent Tasks for the Affiliate Automation System

## Phase 1: Project Foundation
- [ ] Initialize backend project structure
- [ ] Initialize frontend project structure
- [ ] Create environment configuration template
- [ ] Configure PostgreSQL connection setup
- [ ] Configure Redis and Celery setup
- [ ] Create base FastAPI app and health checks
- [ ] Create database migration setup or schema runner

## Phase 2: Database and Core Models
- [ ] Implement users model
- [ ] Implement categories model
- [ ] Implement products model
- [ ] Implement product research run model
- [ ] Implement product candidate model
- [ ] Implement affiliate check model
- [ ] Implement media asset model
- [ ] Implement content draft model
- [ ] Implement approval log model
- [ ] Implement schedule model
- [ ] Implement post model
- [ ] Implement metrics model
- [ ] Implement report model

## Phase 3: Product Research Pipeline
- [ ] Design product research input schema
- [ ] Build category and keyword intake logic
- [ ] Implement ranking logic and product scoring
- [ ] Add candidate result storage
- [ ] Create API to trigger product research jobs
- [ ] Create API to fetch candidate products
- [ ] Add test coverage for product scoring

## Phase 4: Affiliate Validation
- [ ] Create Shopee product validation service
- [ ] Add data extraction for title, price, and image URLs
- [ ] Detect affiliate eligibility and commission metadata
- [ ] Record affiliate check results in database
- [ ] Build affiliate validation API
- [ ] Add handling for unavailable or pending products

## Phase 5: Media Collection
- [ ] Create downloader for product images
- [ ] Create downloader for product video sources
- [ ] Add metadata storage for all assets
- [ ] Add deduplication logic
- [ ] Add storage to local disk or S3
- [ ] Create API to view media assets

## Phase 6: Human Review Workflow
- [ ] Build review queue for products
- [ ] Add approve / reject / revise actions
- [ ] Store approval history with timestamps
- [ ] Link approval state to product lifecycle
- [ ] Create UI for shortlist review

## Phase 7: AI Caption Generation
- [ ] Build caption generation service
- [ ] Generate multiple caption variants
- [ ] Generate hook lines and CTAs
- [ ] Generate hashtags and platform-specific language
- [ ] Support user revision workflow
- [ ] Store content drafts in the database

## Phase 8: Video Editing
- [ ] Add FFmpeg integration for video processing
- [ ] Create preset export rules for TikTok, Reels, Shorts, YouTube
- [ ] Build audio stripping / music removal workflow
- [ ] Add subtitles or overlays if required
- [ ] Keep original raw asset intact

## Phase 9: Scheduler and Publishing
- [ ] Add time-based scheduling flow
- [ ] Create queue-based job publishing workflow
- [ ] Integrate at least one platform publishing API
- [ ] Add support for multiple target platforms
- [ ] Record external post IDs
- [ ] Handle retries and publish failure logs

## Phase 10: Monitoring and Reporting
- [ ] Build metric collection service
- [ ] Fetch platform analytics after publishing
- [ ] Aggregate metrics by post, product, and platform
- [ ] Generate daily report summaries
- [ ] Build recommendation logic for better next actions
- [ ] Add dashboard views for reporting

## Phase 11: Frontend Dashboard
- [ ] Build landing dashboard
- [ ] Build category input form
- [ ] Build product shortlist review page
- [ ] Build affiliate status panel
- [ ] Build caption editor page
- [ ] Build schedule page
- [ ] Build publishing status page
- [ ] Build reporting dashboard

## Phase 12: Testing and QA
- [ ] Add unit tests for scoring and ranking logic
- [ ] Add unit tests for affiliate validation logic
- [ ] Add tests for media storage and metadata
- [ ] Add tests for scheduler logic
- [ ] Add integration tests for a sample publishing flow
- [ ] Validate error handling and retries

## Phase 13: Deployment and Hardening
- [ ] Production environment variable review
- [ ] Docker Compose / deployment readiness
- [ ] Logging and monitoring setup
- [ ] Secure secret handling
- [ ] Performance review and optimization
- [ ] Documentation finalization

## Definition of Done for MVP
- [ ] User can input category and keywords
- [ ] System returns ranked product candidates
- [ ] User can approve or reject products
- [ ] Affiliate availability is validated
- [ ] Media asset pipeline works
- [ ] AI generates captions
- [ ] User can schedule posting
- [ ] One supported platform can publish successfully
- [ ] Daily metrics are captured and reported
- [ ] Project documentation is complete

## Recommended Execution Order
1. backend foundation
2. database schema
3. research + scoring
4. affiliate validation
5. approval flow
6. media asset pipeline
7. AI caption generation
8. scheduler
9. publishing integration
10. reporting
11. UI refinement
12. tests and deployment
