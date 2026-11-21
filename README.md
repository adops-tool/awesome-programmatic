<div align="center">

# Awesome Programmatic

**A curated, engineer-grade map of open-source ad tech, official IAB specifications, and the tooling that keeps the programmatic supply chain honest.**

<sub>Open source, official specs, and primary-source documentation only — no closed SaaS, no vendor marketing. Legacy and archived projects are flagged in their descriptions.</sub>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

</div>

## Table of Contents

- [Open-Source Ad Servers, DSPs & SSPs](#open-source-ad-servers-dsps--ssps)
- [Core Protocols & IAB Specifications](#core-protocols--iab-specifications)
- [OpenRTB Parsers, Simulators & Testing Tools](#openrtb-parsers-simulators--testing-tools)
- [Header Bidding & Monetization Tools](#header-bidding--monetization-tools)
- [CTV, Video & Audio Programmatic](#ctv-video--audio-programmatic)
- [Books, Glossaries & Learning Paths](#books-glossaries--learning-paths)
- [News, Podcasts & Communities](#news-podcasts--communities)
- [Contributing](#contributing)
- [License](#license)

---

## Open-Source Ad Servers, DSPs & SSPs

*The infrastructure layer: systems that decide, deliver, and account for an impression.*

- [Revive Adserver](https://github.com/revive-adserver/revive-adserver) - The longest-running free ad server, delivering banner, video, and zone-targeted campaigns from PHP/MySQL with a full management UI, XML-RPC API, and a plugin ecosystem.
- [Prebid Server](https://github.com/prebid/prebid-server) - Go implementation of a server-side header bidding auction that speaks OpenRTB, ships over a hundred bidder adapters, and handles cookie sync, floors, and multi-format requests at high QPS.
- [Prebid Server Java](https://github.com/prebid/prebid-server-java) - JVM port of Prebid Server maintained by Prebid.org for teams standardising their auction stack on Spring Boot and Java tooling.
- [Prebid Sales Agent](https://github.com/prebid/salesagent) - Reference media sales agent implementing the AdCP Media Buy protocol, letting publishers expose inventory to AI buyer agents through a standard API.
- [RTB4FREE Bidder](https://github.com/RTB4FREE/bidder) - OpenRTB 2.x bidder and DSP reference implementation in Java with campaign targeting, budget pacing, and win/loss accounting.
- [Zhuque](https://github.com/javagossip/zhuque) - Chinese-language, Apache-2.0 ad platform whose SSP, ADX, DSP, and DMP modules form a complete end-to-end reference architecture.

---

## Core Protocols & IAB Specifications

*Wire formats and standards documents — read these before reading anyone's framework.*

- [OpenRTB 2.x Specification](https://github.com/InteractiveAdvertisingBureau/openrtb2.x) - Canonical IAB Tech Lab repository for OpenRTB 2.6 and later 2.x revisions, with the specification text, changelogs, and errata tracking.
- [OpenRTB 2.5 & Earlier](https://github.com/InteractiveAdvertisingBureau/openrtb) - Archive of earlier OpenRTB 2.x releases plus the SupplyChain object and related protocol documents that most live integrations still reference.
- [AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM) - Advertising Common Object Model, the shared vocabulary of objects and enums that OpenRTB 3.0 and the OpenMedia stack are built on.
- [OpenRTB Data Models](https://github.com/InteractiveAdvertisingBureau/openrtb-model) - IAB Tech Lab reference models for OpenRTB 2.x and 3.0 objects, useful for validating field-level assumptions during implementation.
- [VAST](https://github.com/InteractiveAdvertisingBureau/VAST) - Official Video Ad Serving Template repository with the current specification text, XSD schemas, and versioned release notes.
- [VAST Samples](https://github.com/InteractiveAdvertisingBureau/VAST_Samples) - Official catalogue of sample VAST tags covering wrappers, error macros, and format permutations for player and validator testing.
- [VMAP](https://github.com/InteractiveAdvertisingBureau/vmap) - Digital Video Multiple Ad Playlist specification for describing ad breaks and ad source hierarchies in long-form video.
- [VPAID](https://github.com/InteractiveAdvertisingBureau/vpaid) - Legacy IAB VPAID 2.0 interactive video spec, retained because a large share of the market still traffics VPAID creatives. *(deprecated)*
- [SIMID](https://github.com/InteractiveAdvertisingBureau/SIMID) - Secure Interactive Media Interface Definition, the sandboxed postMessage replacement for VPAID.
- [OM SDK](https://iabtechlab.com/standards/open-measurement-sdk/) - IAB Tech Lab's Open Measurement SDK programme page with downloads, OMID API guidance, and certification paths for mobile, web video, and CTV viewability.
- [Open Measurement JS Clients](https://github.com/InteractiveAdvertisingBureau/Open-Measurement-JSClients) - Reference JavaScript clients for the OMID web-video SDK, showing how players emit measurement signals to verification vendors.
- [MRAID 3.0 Compliance Ads](https://github.com/InteractiveAdvertisingBureau/MRAID-3.0-Compliance-Ads) - Test creatives and harness material for checking MRAID 3.0 behaviour across in-app ad containers.
- [Global Privacy Platform](https://github.com/InteractiveAdvertisingBureau/Global-Privacy-Platform) - IAB Tech Lab spec that encodes regional privacy signals into a single transmissible string for the bidstream.
- [iabtcf-es](https://github.com/InteractiveAdvertisingBureau/iabtcf-es) - Official TypeScript/JavaScript suite for encoding, decoding, and validating TCF v2 consent strings.
- [Supply Chain Validation](https://github.com/InteractiveAdvertisingBureau/Supply-Chain-Validation) - Reference material for validating the SupplyChain object (schain) carried in bid requests and ad markup.
- [Ad Management API](https://github.com/InteractiveAdvertisingBureau/AdManagementAPI) - OpenMedia specification for creative approval workflows between buyers and sellers.
- [OpenDirect](https://github.com/InteractiveAdvertisingBureau/OpenDirect) - Specification for automating programmatic guaranteed deals across order, line item, and creative objects.
- [IAB Tech Lab Taxonomies](https://github.com/InteractiveAdvertisingBureau/Taxonomies) - Machine-readable content, audience, and ad-product taxonomies with versioned IDs for targeting and brand safety.
- [Ad Context Protocol (AdCP)](https://github.com/adcontextprotocol/adcp) - Specification and reference implementation for agentic media buying, defining the negotiation and order layer above raw OpenRTB.

---

## OpenRTB Parsers, Simulators & Testing Tools

*Libraries and harnesses for modelling, linting, and replaying real bidstreams.*

- [prebid/openrtb](https://github.com/prebid/openrtb) - Go types and enums for OpenRTB 2.x/3.0, AdCOM, and Native, maintained by Prebid.org as the foundation of Prebid Server's JSON handling.
- [bsm/openrtb](https://github.com/bsm/openrtb) - Compact Go OpenRTB 2.x protocol definitions with a validation-friendly struct layout that remains widely vendored. *(archived)*
- [ClearcodeHQ/openrtb](https://github.com/ClearcodeHQ/openrtb) - Go library providing OpenRTB 2.5 and 3.0 types with builders and validation helpers for object construction.
- [anossov/openrtb](https://github.com/anossov/openrtb) - Python classes implementing OpenRTB 2.2 and mobile objects for fast request/response modelling in scripts and notebooks.
- [Avocarrot/openrtb](https://github.com/Avocarrot/openrtb) - Node.js library that builds, validates, and processes OpenRTB objects for JavaScript bidders and simulators.
- [chompi/openrtb2x](https://github.com/chompi/openrtb2x) - Java implementation of the OpenRTB 2.x object model, useful as a spec-faithful serialization reference.
- [rtblint](https://github.com/aleksUIX/rtblint) - OpenRTB linter that validates 2.x bid requests and responses against versioned IAB spec snapshots, runnable locally or as a service.
- [OpenRTB 3.0 Converter](https://github.com/InteractiveAdvertisingBureau/openrtb3-converter) - IAB Tech Lab reference converter mapping OpenRTB 2.6 payloads onto the OpenRTB 3.0 / AdCOM object model.
- [ads.cert OpenRTB 3.0 Verifier](https://github.com/InteractiveAdvertisingBureau/ads-cert-openrtb3-verifier) - Verifier implementation for ads.cert authenticated connections over OpenRTB 3.0. *(archived)*
- [VASTlint](https://github.com/aleksUIX/vastlint) - Open-source VAST, VMAP, and DAAST validator that catches schema, macro, and platform-specific errors before tags ship.
- [IAB VAST Tester](https://github.com/InteractiveAdvertisingBureau/vasttester) - IAB Tech Lab tooling for exercising VAST tags and their error macros against the published specification.
- [vast-client-js](https://github.com/dailymotion/vast-client-js) - Battle-tested JavaScript VAST client that parses documents up to VAST 6, resolves wrappers, and emits standard tracking events.
- [rmp-vast](https://github.com/radiantmediaplayer/rmp-vast) - Client-side JavaScript loader and parser that renders VAST 2–4 linear and non-linear ads into HTML5 video.
- [php-vast](https://github.com/sokil/php-vast) - PHP library for generating and parsing VAST documents, handy for building tag and wrapper endpoints in PHP stacks.
- [adstxtcrawler](https://github.com/InteractiveAdvertisingBureau/adstxtcrawler) - Reference Python crawler that fetches and parses ads.txt and app-ads.txt files for supply-path verification.
- [alicebob/ssp](https://github.com/alicebob/ssp) - Minimal OpenRTB SSP that issues bid requests to an exchange, ideal for integration-testing a bidder end to end.

---

## Header Bidding & Monetization Tools

*Client-side auction machinery, debugging surfaces, and the SDKs that extend it into apps.*

- [Prebid.js](https://github.com/prebid/Prebid.js) - The reference client-side header bidding wrapper, bundling over a hundred bidder adapters with auction orchestration, floors, consent, and analytics modules.
- [Prebid Documentation](https://github.com/prebid/prebid.github.io) - Source repository for the official Prebid docs site, covering every adapter, module, and server-side setting.
- [Header Bidder Expert](https://github.com/prebid/header-bidder-expert) - Browser extension that surfaces on-page Prebid.js auction activity, including bidders, bids, timeouts, and winning CPMs.
- [Professor Prebid](https://github.com/prebid/professor-prebid) - Prebid's next-generation debugging tool for inspecting auctions, ad units, and module behaviour in the browser.
- [Prebid Universal Creative](https://github.com/prebid/prebid-universal-creative) - Creative renderer that lets Prebid Server and AMP bids display consistently without publisher-specific creative code.
- [Prebid Cache](https://github.com/prebid/prebid-cache) - Companion service that stores VAST and JSON creative payloads referenced by Prebid Server bid responses.
- [Prebid Mobile iOS](https://github.com/prebid/prebid-mobile-ios) - iOS SDK bringing header bidding to in-app inventory through Prebid Server auctions.
- [Prebid Mobile Android](https://github.com/prebid/prebid-mobile-android) - Android SDK counterpart for header bidding in mobile apps, including rendering and MRAID support.
- [PubFood](https://github.com/pubfood/pubfood) - Publisher-built open-source header bidding framework from the pre-Prebid era, still a readable reference for auction design. *(legacy)*

---

## CTV, Video & Audio Programmatic

*Players and playback stacks where the ad actually renders — and where most integration bugs live.*

- [Video.js](https://github.com/videojs/video.js) - The default open-source media player framework for HTML and React, with a plugin ecosystem spanning VAST, IMA, analytics, and DRM.
- [videojs-contrib-ads](https://github.com/videojs/videojs-contrib-ads) - Video.js plugin providing the ad-state machine — preroll, midroll, postroll, and content-resume — that VAST integrations build on.
- [HTML5 IMA Samples](https://github.com/googleads/googleads-ima-html5) - Official samples for the HTML5 IMA SDK showing VAST/VMAP ad scheduling, tracking, and companion handling.
- [videojs-vast-vpaid](https://github.com/MailOnline/videojs-vast-vpaid) - MailOnline's Video.js plugin for rendering VAST and VPAID creatives, including wrapper resolution and non-linear formats.
- [Shaka Player](https://github.com/shaka-project/shaka-player) - Google's DASH and HLS player library with production-grade DRM and ad-integration hooks used across browser and CTV deployments.
- [hls.js](https://github.com/video-dev/hls.js) - MSE-based HLS playback library that underpins most browser and web-view video stacks, including serverside-ad-inserted streams.
- [AndroidX Media3](https://github.com/androidx/media) - Jetpack Media3 / ExoPlayer, the Android playback stack with ad-insertion and IMA extensions for mobile and Android TV.
- [DAAST](https://github.com/InteractiveAdvertisingBureau/daast) - Digital Audio Ad Serving Template, the IAB spec extending VAST semantics to audio and podcast ad delivery.
- [Video & CTV Ad Format Guidelines](https://github.com/InteractiveAdvertisingBureau/Ad-Format-Guidelines-for-Digital-Video-CTV) - IAB Tech Lab guidance mapping emerging CTV formats — pause, menu, overlay — onto spec fields and creative requirements.

---

## Books, Glossaries & Learning Paths

*Structured material for going from "what is a DSP" to reading bidstreams for a living.*

- [The AdTech Book](https://www.avenga.com/whitepapers/adtech-book/) - Free, regularly updated 300-plus-page book (formerly by Clearcode) covering the full ad tech stack from ad servers to privacy and identity.
- [Programmatic Advertising](https://link.springer.com/book/10.1007/978-3-319-25023-6) - Edited volume of 22 expert chapters on DSP/SSP mechanics, data strategy, and the organisational change programmatic forces on advertisers.
- [Prebid Docs](https://docs.prebid.org/) - Canonical technical documentation for Prebid.js, Prebid Server, and Prebid Mobile, including per-adapter and per-module reference pages.
- [IAB Tech Lab Standards](https://iabtechlab.com/standards/) - Master index of every IAB Tech Lab specification, guidance document, taxonomy, and software project, with version and status per item.
- [IAB Standards & Guidelines](https://www.iab.com/guidelines/) - IAB's library of measurement, video, audio, commerce, and brand-safety guidance that complements Tech Lab's wire-level specs.
- [Prebid Blog](https://prebid.org/blog/) - Engineering and market analysis from Prebid.org on auction mechanics, identity, CTV, and agentic buying.
- [IAB Tech Lab Working Groups](https://iabtechlab.com/working-groups/) - Directory of the groups that actually draft the specifications, with each group's mission, owner, and current status.

---

## News, Podcasts & Communities

*Where practitioners argue about the specs, the auctions, and the economics behind them.*

- [AdExchanger](https://www.adexchanger.com/) - Daily reporting and analysis on programmatic, privacy, CTV, and retail media that explains why the specifications keep changing.
- [AdMonsters](https://www.admonsters.com/) - Publisher-side ad operations community and publication focused on yield, header bidding, and operational troubleshooting.
- [Digiday](https://digiday.com/) - Media and marketing trade coverage with practical reporting on monetisation strategy and platform policy shifts.
- [Marketecture Podcast](https://news.marketecture.tv/marketecture-podcast) - Weekly interviews with ad tech founders and executives, hosted by Ari Paparo and Eric Franchi, on how the industry actually operates.
- [r/adops](https://www.reddit.com/r/adops/) - Practitioner subreddit for ad operations questions, tag debugging, and vendor comparisons.
- [r/programmatic](https://www.reddit.com/r/programmatic/) - Trading-floor discussion of DSP tactics, supply-path optimisation, and bidstream quality.
- [r/adtech](https://www.reddit.com/r/adtech/) - General ad tech subreddit covering industry news, careers, and technical questions.

---

## Contributing

Contributions are welcome and reviewed for technical accuracy, not for reach.

**In scope:** open-source software, official specifications and schemas from IAB / IAB Tech Lab, developer tooling, and primary-source educational material.

**Out of scope:** proprietary SaaS products, generic ad-network lists, affiliate or referral links, and anything without a publicly verifiable URL.

**Before opening a PR:**

1. Verify the link resolves and points to the canonical project or document (no mirrors, no redirect chains to marketing pages).
2. Match the entry format exactly: `- [Resource Name](https://url) - One sentence describing what it is and what problem it solves.`
3. Keep it alphabetical within a section, and flag projects that are archived, deprecated, or legacy.
4. One logical change per pull request, with a line explaining why the resource belongs here.

Spotted a dead link or a spec that moved? A PR with the corrected URL is the fastest path to a fix.

---

## License

Released under [CC0 1.0 Universal](LICENSE) — public domain dedication. Copy, remix, and redistribute this list without attribution, though a link back is always appreciated.

[![CC0](https://img.shields.io/badge/CC0-1.0-lightgrey?style=flat-square)](LICENSE)
