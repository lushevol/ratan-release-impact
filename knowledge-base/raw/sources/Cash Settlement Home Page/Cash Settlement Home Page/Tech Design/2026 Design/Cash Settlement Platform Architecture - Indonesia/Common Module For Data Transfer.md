For static data(static/rule) sync from Ratan GDC to Ratan ID instance, we have another way to build this function.

It is supposed to be a common solution for all static data synchronization from GDC to XDC. It's a separate implement that independent of domain services.

We use static data and rule service synchronize data from GDC to IDDC for example.

## Overall Diagram

##

## Data Synchronize Manager

Data Synchronizer Manager is responsible for table data synchronize but does not care the business.

There are two ways of implementation: embedded in domain service as a common module or deploy as an independent service. This design is for embedded common module.

- Each data has only one sync record to record the newest sync event.
- Every sync event with a unique request_id.

- Sync status are SENT ACK NACK FAILED TIMEOUT for each downstream DC, for example: {"ID": "ACK"}

SENT: Data produced successfully by Producer.

FAILED:  Data produced failed by Producer.

ACK:  Data consumed successfully by Consumer.

NACK: Data consumed failed by Consumer.

TIMEOUT: No response received in 5 minutes.

- Sync response with wrong request_id will be ignore.

## Resync By Data Producer

There is a SyncFailedRetryer in data producer to resync the records with  FAILED and TIMEOUT status and set status to SENT.

## Recon By Data Consumer

There is a rest API for Consumer to do recon periodically.

## Resync & Refresh Manually

## Sync Data Definition

Expand source

Table

- ratan_data_synchronizer

| id | bigserial | Y | | | Y |
| --- | --- | --- | --- | --- | --- |
| object_id | text | Y | Y | | |
| object_type | text | Y | | | |
| request_id | text | Y | Y | | |
| sync_content | text | Y | | {} | |
| sync_status | text | Y | | { "ID": "ACK", "XX": "NACK", "...": "SENT", "...": "FAILED", "...": "TIMEOUT" } | |
| create_at | timestamp | Y | | | |
| update_at | timestamp | Y | | | |