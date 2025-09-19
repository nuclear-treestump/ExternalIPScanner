# Roadmap for this tool

## Phase 0
* It runs without catching fire.
* Code coverage >50%

## Phase 1
* Dockerized container for ease of deployment.
* Pluggable config for AWS.
* Output as JSON
* Code coverage >90%

## Phase 2
* Add support for GCP
* Support AWS Secrets / SSM over command-switch secrets
* Add output support for CSV
* Code coverage >99%

## Phase 3
* Add pluggable support for registrars (GoDaddy, PorkBun) (The ones I currently use)
* Support output for local SQlite DB
* Add HTTP API for querying data
* Complete code coverage

## Phase 4
* Add Flask frontend
* Add basic SPoG dashboard
* Add output option AWS DBs / GCP DBs
* Rescan option
* Timing controls for scheduled scans

## Phase 5
* Secure frontend
* Add alert stack (Twilio, Slack).
* Add alert rules (basic things such as asset count shift above X percent. May add more.)
* Create AMI???
* Create dynamic tagging by account, region, or Tag.
* SAML/SSO Support

## Phase 6
* Removal of as many 3rd party dependencies as possible.
* Prioritize MIT licensed dependencies if I must have any.
* We're playing dependence golf here and my goal is a score of 0.
