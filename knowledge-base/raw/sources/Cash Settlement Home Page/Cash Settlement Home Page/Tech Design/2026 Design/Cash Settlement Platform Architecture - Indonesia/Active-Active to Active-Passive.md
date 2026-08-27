# Service Deployment Strategy

## Option-1 Maintain 1 profile with VIP

## Option-2 Two profiles for 2 clusters

| | Pros | Cons |
| --- | --- | --- |
| Option-1 | 1. Infra switch is transparent for domain applications 2. Only maintain 1 profile 3. Real Active-Passive model | 1. 6 servers for each cluster need 6 VIPs 2. Apps to infra connectivity is available to only 1 DC at same time, so switch step should be 1. Stop primary DC apps. 2. Check all primary DC services are down. 3. Switch VIPs. 4. Start backup DC apps. 5. Check all backup DC services are up. |
| Option-2 | 1. No additional VIPs required 2. Two DCs are totally isolated | 1. Need to maintain 2 profiles separately. 2. CD script needs to be revised to support 1 CD deploy 2 profiles. 3. Could be Active-Active, need to manual avoid message racing(MB startup should be restricted). |