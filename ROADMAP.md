# Roadmap for this tool

## Phase 0
* It runs without catching fire.

## Phase 1
* Dockerized container for ease of deployment.
* Pluggable config for AWS.
* Output as JSON

## Phase 2
* Add support for GCP
* Support AWS Secrets / SSM over command-switch secrets
* Add output support for CSV

## Phase 3
* Add pluggable support for registrars (GoDaddy, PorkBun) (The ones I currently use)
* Support output for local SQlite DB
* Add HTTP API for querying data

## Phase 4
* Add Flask frontend
* Add basic SPoG dashboard
* Add output option AWS DBs / GCP DBs

## Phase 5
* Add alert stack (Twilio, Slack).
* Add alert rules (basic things such as asset count shift above X percent. May add more.)
* Create AMI???
* Create dynamic tagging by account, region, or Tag.
