<div align="center">

![Awesome Programmatic](image/awesome-programmatic.png)

# Awesome Programmatic

A curated list of open-source software, standards, documentation, and learning resources for programmatic advertising.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

The list focuses on technical resources and primary sources rather than commercial product directories. Historical resources are labelled **legacy**, **unmaintained**, **archived**, or **deprecated** where relevant; check compatibility and maintenance before using them.

</div>

> Each entry is marked with the kind of resource it is: ![github](image/alg_R.png) open-source repository, ![web](image/alg_I.png) documentation, specification, or hosted tool. Dormant and archived projects are kept when they still explain an architecture — they are labeled as such.

## Table of Contents

- [Open-Source Ad Servers, DSPs & SSPs](#open-source-ad-servers-dsps--ssps)
  - [Ad Servers & Supply-Side Platforms](#ad-servers--supply-side-platforms)
  - [Demand-Side Platforms & Bidders](#demand-side-platforms--bidders)
- [Core Protocols & IAB Specifications](#core-protocols--iab-specifications)
  - [Auction Protocols & Models](#auction-protocols--models)
  - [Direct Deals & Creative APIs](#direct-deals--creative-apis)
  - [Rich Media & In-App Standards](#rich-media--in-app-standards)
- [OpenRTB Parsers, Simulators & Testing Tools](#openrtb-parsers-simulators--testing-tools)
  - [OpenRTB Libraries & Data Models](#openrtb-libraries--data-models)
  - [Auction Simulators & Validators](#auction-simulators--validators)
- [Header Bidding & Monetization Tools](#header-bidding--monetization-tools)
  - [Client & Server Auctions](#client--server-auctions)
  - [Mobile SDKs & Creative Delivery](#mobile-sdks--creative-delivery)
  - [Header Bidding Debugging & Setup](#header-bidding-debugging--setup)
- [Supply Chain & Ad Verification](#supply-chain--ad-verification)
  - [Supply Chain Specifications](#supply-chain-specifications)
  - [Supply Chain Crawlers & Validators](#supply-chain-crawlers--validators)
  - [Measurement & Verification](#measurement--verification)
- [Privacy, Consent & Identity](#privacy-consent--identity)
  - [Privacy & Consent Specifications](#privacy--consent-specifications)
  - [Consent String Libraries](#consent-string-libraries)
  - [Identity Frameworks](#identity-frameworks)
- [CTV, Video & Audio Programmatic](#ctv-video--audio-programmatic)
  - [Video & Audio Specifications](#video--audio-specifications)
  - [VAST Parsers & Test Tools](#vast-parsers--test-tools)
  - [Players & Ad Integrations](#players--ad-integrations)
  - [Video SDK Samples](#video-sdk-samples)
- [Agentic Advertising](#agentic-advertising)
  - [Agentic Standards & Frameworks](#agentic-standards--frameworks)
  - [Buyer & Seller Agents](#buyer--seller-agents)
- [Books, Glossaries & Learning Paths](#books-glossaries--learning-paths)
  - [Books & Introductions](#books--introductions)
  - [Developer Documentation](#developer-documentation)
- [News, Podcasts & Communities](#news-podcasts--communities)
  - [Publications & Podcasts](#publications--podcasts)
  - [Practitioner Communities](#practitioner-communities)
- [Contributing](#contributing)
- [License](#license)

---

<!-- resources:start -->

## Open-Source Ad Servers, DSPs & SSPs

*Ad-serving systems and reference implementations for the supply and demand sides of an auction.*

### Ad Servers & Supply-Side Platforms

![github](image/alg_R.png) [OpenSSP](https://github.com/ad-tech-group/openssp) - Java supply-side platform with OpenRTB support through version 2.4 (legacy; last updated 2022).

![github](image/alg_R.png) [Revive Adserver](https://github.com/revive-adserver/revive-adserver) - PHP ad server for managing campaigns, placements, targeting, and delivery reports.

![github](image/alg_R.png) [Zhuque](https://github.com/javagossip/zhuque) - Java advertising platform with SSP, exchange, DSP, and data-management components (legacy; documentation in Chinese).

### Demand-Side Platforms & Bidders

![github](image/alg_R.png) [RTB4FREE Bidder](https://github.com/RTB4FREE/bidder) - Java bidder and DSP implementation supporting OpenRTB 2.0 (legacy; last updated 2022).

![github](image/alg_R.png) [vanilla-rtb](https://github.com/venediktov/vanilla-rtb) - C++ framework for building real-time bidders and managing campaign targeting.

![github](image/alg_R.png) [VOXDSP](https://github.com/VOXDSP/VOXDSP) - PHP demand-side platform and bidder for OpenRTB requests.

---

## Core Protocols & IAB Specifications

*Standards for auction payloads, advertising objects, direct deals, and interactive creatives.*

### Auction Protocols & Models

![github](image/alg_R.png) [AdCOM](https://github.com/InteractiveAdvertisingBureau/AdCOM) - IAB Advertising Common Object Model for advertising objects and enumerations.

![github](image/alg_R.png) [IAB Tech Lab Taxonomies](https://github.com/InteractiveAdvertisingBureau/Taxonomies) - Versioned content, audience, and ad-product taxonomies for advertising systems.

![github](image/alg_R.png) [OpenRTB 2.x Specification](https://github.com/InteractiveAdvertisingBureau/openrtb2.x) - IAB Tech Lab specification and updates for OpenRTB 2.6 and later 2.x revisions.

![github](image/alg_R.png) [OpenRTB 3.0 & Extensions](https://github.com/InteractiveAdvertisingBureau/openrtb) - IAB Tech Lab's OpenRTB 3.0 specification, extensions, and earlier release branches.

![github](image/alg_R.png) [OpenRTB Native Ads](https://github.com/InteractiveAdvertisingBureau/Native-Ads) - IAB Tech Lab's OpenRTB Native Ads specification and implementation guidance.

![github](image/alg_R.png) [Programmatic Auction Definitions](https://github.com/InteractiveAdvertisingBureau/programmatic-auction-definitions) - IAB Tech Lab definitions for participants and events in programmatic auctions.

### Direct Deals & Creative APIs

![github](image/alg_R.png) [Ad Management API](https://github.com/InteractiveAdvertisingBureau/AdManagementAPI) - IAB Tech Lab specification for managing creative review and approval between trading partners.

![github](image/alg_R.png) [OpenDirect](https://github.com/InteractiveAdvertisingBureau/OpenDirect) - IAB Tech Lab API specification for programmatic direct orders and line items.

![github](image/alg_R.png) [Universal Creative Identification Framework](https://github.com/IABTechLab/ucid) - Specification for creating and verifying unique creative identifiers (draft).

### Rich Media & In-App Standards

![github](image/alg_R.png) [MRAID 3.0 Compliance Ads](https://github.com/InteractiveAdvertisingBureau/MRAID-3.0-Compliance-Ads) - Sample creatives for testing MRAID 3.0 implementations (last updated 2018).

![github](image/alg_R.png) [SafeFrame Reference Implementation](https://github.com/InteractiveAdvertisingBureau/safeframe) - IAB reference implementation of the SafeFrame container for publisher advertising (legacy; last updated 2021).

![github](image/alg_R.png) [SHARC](https://github.com/IABTechLab/SHARC) - IAB specification for communication between HTML ad creatives and their host containers.

---

## OpenRTB Parsers, Simulators & Testing Tools

*Libraries and test environments for constructing, validating, and analysing bid requests and responses.*

### OpenRTB Libraries & Data Models

![github](image/alg_R.png) [AdCOM Protobuf](https://github.com/IABTechLab/adcom-proto) - Protocol Buffer definitions for AdCOM objects (work in progress).

![github](image/alg_R.png) [anossov/openrtb](https://github.com/anossov/openrtb) - Python classes for OpenRTB 2.2 and mobile objects (legacy).

![github](image/alg_R.png) [Avocarrot/openrtb](https://github.com/Avocarrot/openrtb) - Node.js library for building and validating OpenRTB objects (legacy).

![github](image/alg_R.png) [bsm/openrtb](https://github.com/bsm/openrtb) - Go definitions for the OpenRTB protocol (archived).

![github](image/alg_R.png) [chompi/openrtb2x](https://github.com/chompi/openrtb2x) - Java reference implementation of OpenRTB offline synchronisation services (legacy).

![github](image/alg_R.png) [ClearcodeHQ/openrtb](https://github.com/ClearcodeHQ/openrtb) - TypeScript library for building and validating OpenRTB 2.5 and 3.0 objects (legacy).

![github](image/alg_R.png) [GoRTB](https://github.com/MehrazRumman/gortb) - Go types and validation methods for OpenRTB 2.5 requests and responses.

![github](image/alg_R.png) [OpenRTB 3.0 Converter](https://github.com/InteractiveAdvertisingBureau/openrtb3-converter) - Java library converting requests and responses between OpenRTB 2.3–2.5 and 3.0 (legacy).

![github](image/alg_R.png) [OpenRTB Data Models](https://github.com/InteractiveAdvertisingBureau/openrtb-model) - Java data models for OpenRTB 2.x and 3.0 (legacy).

![github](image/alg_R.png) [OpenRTB Protobuf Libraries](https://github.com/IABTechLab/openrtb-proto-v2) - OpenRTB 2.x Protocol Buffer bindings and Java JSON utilities (deprecated).

![github](image/alg_R.png) [prebid/openrtb](https://github.com/prebid/openrtb) - Go types and enumerations for OpenRTB, AdCOM, and Native Ads.

### Auction Simulators & Validators

![github](image/alg_R.png) [alicebob/ssp](https://github.com/alicebob/ssp) - Minimal OpenRTB 2.3 SSP for testing campaigns and bidders (unmaintained).

![github](image/alg_R.png) [AuctionGym](https://github.com/amazon-science/auction-gym) - Simulation environment for evaluating bandit and reinforcement-learning methods in advertising auctions.

![github](image/alg_R.png) [CcinnOpenRTB](https://github.com/whiteCcinn/ccinnOpenRTB) - macOS simulator for rendering OpenRTB creatives and inspecting tracking events.

![github](image/alg_R.png) [CTV Header Bidding Lab](https://github.com/wilmccann/ctv-header-bidding-lab) - OpenRTB CTV examples and a local Prebid Server auction test harness.

![github](image/alg_R.png) [rtbgen](https://github.com/rsbid/rtbgen) - Rust library and CLI for generating deterministic OpenRTB 2.5 and 2.6 bid requests for tests.

![github](image/alg_R.png) [RTBlint](https://github.com/aleksUIX/rtblint) - OpenRTB validator with a Rust library, CLI, and browser-compatible WebAssembly package.

![github](image/alg_R.png) [WhyNoBid RTB Diff](https://github.com/adops-tool/whynobid-rtb-diff) - Python toolkit for comparing bid-request fields across bidding and no-bid cohorts.

---

## Header Bidding & Monetization Tools

*Auction wrappers, SDKs, creative delivery components, and debugging tools for publishers.*

### Client & Server Auctions

![github](image/alg_R.png) [Prebid Server](https://github.com/prebid/prebid-server) - Go implementation of server-side Prebid auctions.

![github](image/alg_R.png) [Prebid Server Java](https://github.com/prebid/prebid-server-java) - Java implementation of server-side Prebid auctions.

![github](image/alg_R.png) [Prebid.js](https://github.com/prebid/Prebid.js) - JavaScript header-bidding library with bidder adapters and auction modules.

![github](image/alg_R.png) [PubFood](https://github.com/pubfood/pubfood) - Publisher-built JavaScript header-bidding framework (legacy; last updated 2017).

### Mobile SDKs & Creative Delivery

![github](image/alg_R.png) [Prebid Cache](https://github.com/prebid/prebid-cache) - Go service for storing creative payloads referenced by Prebid auctions.

![github](image/alg_R.png) [Prebid Cache Java](https://github.com/prebid/prebid-cache-java) - Java implementation of the Prebid Cache service.

![github](image/alg_R.png) [Prebid Mobile Android](https://github.com/prebid/prebid-mobile-android) - Android SDK for integrating mobile apps with Prebid Server.

![github](image/alg_R.png) [Prebid Mobile iOS](https://github.com/prebid/prebid-mobile-ios) - iOS SDK for integrating mobile apps with Prebid Server.

![github](image/alg_R.png) [Prebid Universal Creative](https://github.com/prebid/prebid-universal-creative) - JavaScript creative renderer for Prebid display, video, mobile, and AMP formats.

### Header Bidding Debugging & Setup

![github](image/alg_R.png) [Ad Manager Viewability Insights](https://github.com/googleads/googleads-viewability-insights-extension) - Chrome DevTools extension for inspecting Ad Manager ad-slot viewability (beta).

![github](image/alg_R.png) [AdTrace GAM Inspector](https://github.com/adops-tool/adtrace-gam-inspector) - Chrome DevTools extension for inspecting Google Ad Manager requests, targeting, and bidding signals.

![github](image/alg_R.png) [Google Publisher Tag Playground](https://github.com/googleads/google-publisher-tag-playground) - Interactive code playground for Google Publisher Tag examples.

![github](image/alg_R.png) [Google Publisher Tag Samples](https://github.com/googleads/google-publisher-tag-samples) - Sample code for implementing ad slots and publisher-tag features.

![github](image/alg_R.png) [Header Bidder Expert](https://github.com/prebid/header-bidder-expert) - Browser extension for inspecting header-bidding activity (legacy; last updated 2022).

![github](image/alg_R.png) [Prebid and GAM Setup Tool](https://github.com/kmjennison/dfp-prebid-setup) - Generates Google Ad Manager line items for Prebid.js deployments.

![github](image/alg_R.png) [Prebid Integration Monitor](https://github.com/prebid/prebid-integration-monitor) - TypeScript project for monitoring Prebid integrations.

![github](image/alg_R.png) [Professor Prebid](https://github.com/prebid/professor-prebid) - Browser debugging tool for inspecting Prebid auctions and ad units.

![github](image/alg_R.png) [Publisher Ads Audits for Lighthouse](https://github.com/googleads/publisher-ads-lighthouse-plugin) - Lighthouse plugin for auditing publisher ad performance, primarily for Google Ad Manager.

---

## Supply Chain & Ad Verification

*Specifications and tools for inspecting seller authorisation, supply paths, and ad measurement.*

### Supply Chain Specifications

![web](image/alg_I.png) [ads.cert](https://iabtechlab.com/ads-cert/) - IAB Tech Lab overview of cryptographic protocols for authenticating advertising connections.

![web](image/alg_I.png) [ads.txt and app-ads.txt](https://iabtechlab.com/ads-txt/) - IAB Tech Lab overview of publisher and app seller-authorisation files.

![github](image/alg_R.png) [Supply Chain Validation](https://github.com/InteractiveAdvertisingBureau/Supply-Chain-Validation) - IAB Tech Lab specifications and guidance for ads.txt, app-ads.txt, and sellers.json.

### Supply Chain Crawlers & Validators

![github](image/alg_R.png) [Ads.txt Checker & Line Matcher](https://github.com/adops-tool/Matcher-ads.txt-app-ads.txt) - Browser-based tool for matching ads.txt and app-ads.txt records against partner lists.

![github](image/alg_R.png) [Ads.txt Manager for WordPress](https://github.com/10up/ads-txt) - WordPress plugin for managing ads.txt and app-ads.txt files.

![github](image/alg_R.png) [ads.txt Validator](https://github.com/apti-jp/adstxt-validator) - TypeScript library for parsing ads.txt and cross-checking entries against sellers.json.

![github](image/alg_R.png) [adstxtcrawler](https://github.com/InteractiveAdvertisingBureau/adstxtcrawler) - IAB Tech Lab's Python example crawler for ads.txt files.

![github](image/alg_R.png) [App-ads.txt URL Parser](https://github.com/InteractiveAdvertisingBureau/ads.txt-parser) - IAB Tech Lab reference utilities for parsing app-store listings and developer URLs.

![github](image/alg_R.png) [Python sellers.json Validator](https://github.com/adops-tool/python-sellers-json-validator) - Asynchronous Python tool for checking sellers.json endpoints across domains.

![github](image/alg_R.png) [SPO Sellers.json Crawler](https://github.com/adops-tool/SPO-sellers-json-crawler) - Python crawler for discovering and checking sellers.json supply-path endpoints.

### Measurement & Verification

![github](image/alg_R.png) [ads.cert Authenticated Connections](https://github.com/IABTechLab/adscert) - Go proof of concept for signing and verifying authenticated connections (not production-ready).

![github](image/alg_R.png) [ads.cert OpenRTB 3.0 Verifier](https://github.com/InteractiveAdvertisingBureau/ads-cert-openrtb3-verifier) - Java verifier for signed OpenRTB 3.0 bid requests under the original ads.cert design (legacy).

![github](image/alg_R.png) [Attribution Use Cases](https://github.com/InteractiveAdvertisingBureau/Attribution-Use-Cases) - IAB Tech Lab use cases for emerging privacy-focused attribution APIs (work in progress).

![github](image/alg_R.png) [Event and Conversion API](https://github.com/InteractiveAdvertisingBureau/ecapi) - IAB Tech Lab specification for exchanging marketing events between advertisers and advertising platforms.

![github](image/alg_R.png) [Open Measurement JS Clients](https://github.com/InteractiveAdvertisingBureau/Open-Measurement-JSClients) - JavaScript clients for integrating with the Open Measurement interface.

![web](image/alg_I.png) [Open Measurement SDK](https://iabtechlab.com/standards/open-measurement-sdk/) - IAB Tech Lab's SDK programme and integration resources for ad measurement.

---

## Privacy, Consent & Identity

*Privacy-signal specifications, consent libraries, and identity integration resources.*

### Privacy & Consent Specifications

![github](image/alg_R.png) [Global Privacy Platform](https://github.com/InteractiveAdvertisingBureau/Global-Privacy-Platform) - IAB Tech Lab specification for conveying privacy signals across jurisdictions.

![github](image/alg_R.png) [Transparency and Consent Framework](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework) - Technical specifications for IAB Europe's Transparency and Consent Framework (TCF).

### Consent String Libraries

![github](image/alg_R.png) [go-gdpr](https://github.com/prebid/go-gdpr) - Go library for parsing IAB consent strings and vendor lists.

![github](image/alg_R.png) [go-gpp](https://github.com/prebid/go-gpp) - Go library for parsing and encoding Global Privacy Platform strings.

![github](image/alg_R.png) [iabgpp-es](https://github.com/IABTechLab/iabgpp-es) - IAB Tech Lab's JavaScript and TypeScript library for encoding and decoding GPP signals.

![github](image/alg_R.png) [iabgpp-java](https://github.com/IABTechLab/iabgpp-java) - IAB Tech Lab's Java library for encoding and decoding GPP signals.

![github](image/alg_R.png) [iabtcf-es](https://github.com/InteractiveAdvertisingBureau/iabtcf-es) - IAB Tech Lab's TypeScript and JavaScript toolkit for TCF consent strings and CMP APIs.

![github](image/alg_R.png) [iabtcf-java](https://github.com/InteractiveAdvertisingBureau/iabtcf-java) - IAB Tech Lab's Java library for TCF consent-string encoding and decoding.

### Identity Frameworks

![github](image/alg_R.png) [UID2 Android SDK](https://github.com/IABTechLab/uid2-android-sdk) - Android SDK for integrating Unified ID 2.0 into applications.

![github](image/alg_R.png) [UID2 Integration Examples](https://github.com/IABTechLab/uid2-examples) - Sample UID2 and EUID integrations for Prebid.js, Google Secure Signals, and other workflows.

![github](image/alg_R.png) [UID2 iOS SDK](https://github.com/IABTechLab/uid2-ios-sdk) - iOS SDK for integrating Unified ID 2.0 into applications.

![web](image/alg_I.png) [Unified ID 2.0 Documentation](https://unifiedid.com/docs/intro) - Overview of the UID2 framework and integration workflows (participation requires an agreement).

---

## CTV, Video & Audio Programmatic

*Specifications, media players, parsers, and examples for audio and video ad delivery.*

### Video & Audio Specifications

![web](image/alg_I.png) [CTV Programmatic Guide](https://iabtechlab.com/standards/advanced-tv/ctv-programmatic-guide/) - IAB Tech Lab guide to advertising standards and use cases in connected TV.

![github](image/alg_R.png) [DAAST](https://github.com/InteractiveAdvertisingBureau/daast) - IAB Tech Lab's Digital Audio Ad Serving Template specification.

![github](image/alg_R.png) [SIMID](https://github.com/InteractiveAdvertisingBureau/SIMID) - IAB Tech Lab's interface for interactive video ad creatives.

![github](image/alg_R.png) [VAST](https://github.com/InteractiveAdvertisingBureau/VAST) - IAB Tech Lab's Video Ad Serving Template specification and schemas.

![github](image/alg_R.png) [VAST Samples](https://github.com/InteractiveAdvertisingBureau/VAST_Samples) - IAB Tech Lab sample VAST tags for video ad use cases.

![github](image/alg_R.png) [Video & CTV Ad Format Guidelines](https://github.com/InteractiveAdvertisingBureau/Ad-Format-Guidelines-for-Digital-Video-CTV) - IAB Tech Lab guidelines for digital video and CTV ad formats.

![github](image/alg_R.png) [VMAP](https://github.com/InteractiveAdvertisingBureau/vmap) - IAB Tech Lab's Video Multiple Ad Playlist specification for describing ad breaks.

![github](image/alg_R.png) [VPAID](https://github.com/InteractiveAdvertisingBureau/vpaid) - IAB Tech Lab's Video Player-Ad Interface Definition specification (deprecated).

### VAST Parsers & Test Tools

![web](image/alg_I.png) [DAI Sample Streams](https://developers.google.com/ad-manager/dynamic-ad-insertion/streams) - Google test streams and identifiers for live and on-demand dynamic ad insertion.

![github](image/alg_R.png) [IAB VAST Tester](https://github.com/InteractiveAdvertisingBureau/vasttester) - Repository for IAB Tech Lab's VAST tag testing interface (licence not specified).

![github](image/alg_R.png) [php-vast](https://github.com/sokil/php-vast) - PHP library for generating and parsing VAST documents.

![github](image/alg_R.png) [vast-client-js](https://github.com/dailymotion/vast-client-js) - JavaScript VAST client for parsing documents, resolving wrappers, and tracking events.

![github](image/alg_R.png) [VASTlint](https://github.com/aleksUIX/vastlint) - Validator for VAST, VMAP, and DAAST documents.

### Players & Ad Integrations

![github](image/alg_R.png) [AndroidX Media3](https://github.com/androidx/media) - Android media libraries including ExoPlayer and ad-integration components.

![github](image/alg_R.png) [hls.js](https://github.com/video-dev/hls.js) - JavaScript library for HLS playback in browsers using Media Source Extensions.

![github](image/alg_R.png) [Prebid Outstream Renderer](https://github.com/prebid/prebid-outstream) - JavaScript library for rendering outstream video ads.

![github](image/alg_R.png) [rmp-vast](https://github.com/radiantmediaplayer/rmp-vast) - JavaScript library for loading, parsing, and displaying VAST ads with HTML5 video.

![github](image/alg_R.png) [Shaka Player](https://github.com/shaka-project/shaka-player) - JavaScript player for DASH and HLS with ad-integration support.

![github](image/alg_R.png) [Video.js](https://github.com/videojs/video.js) - Open-source media player framework with an advertising plugin ecosystem.

![github](image/alg_R.png) [videojs-contrib-ads](https://github.com/videojs/videojs-contrib-ads) - Video.js plugin providing the common ad workflow for advertising integrations.

![github](image/alg_R.png) [videojs-ima](https://github.com/googleads/videojs-ima) - Google IMA SDK plugin for integrating ads with Video.js.

![github](image/alg_R.png) [videojs-vast-vpaid](https://github.com/MailOnline/videojs-vast-vpaid) - Video.js plugin for VAST and VPAID ads (legacy; VPAID is deprecated).

### Video SDK Samples

![github](image/alg_R.png) [Android IMA DAI Samples](https://github.com/googleads/googleads-ima-android-dai) - Sample integrations for dynamic ad insertion with the Android IMA SDK.

![github](image/alg_R.png) [Android IMA Samples](https://github.com/googleads/googleads-ima-android) - Google's sample integrations for the Android Interactive Media Ads SDK.

![github](image/alg_R.png) [HTML5 IMA DAI Samples](https://github.com/googleads/googleads-ima-html5-dai) - Sample dynamic ad insertion integrations for HTML5 players including HLS.js and DASH.js.

![github](image/alg_R.png) [HTML5 IMA Samples](https://github.com/googleads/googleads-ima-html5) - Google's sample integrations for the HTML5 Interactive Media Ads SDK.

![github](image/alg_R.png) [iOS IMA DAI Samples](https://github.com/googleads/googleads-ima-ios-dai) - Sample integrations for dynamic ad insertion with the iOS IMA SDK.

![github](image/alg_R.png) [iOS IMA Samples](https://github.com/googleads/googleads-ima-ios) - Google's sample integrations for the iOS Interactive Media Ads SDK.

---

## Agentic Advertising

*Open protocols and reference projects for software agents participating in advertising workflows.*

### Agentic Standards & Frameworks

![github](image/alg_R.png) [AAMP](https://github.com/IABTechLab/AAMP) - IAB Tech Lab hub for Agentic Advertising Management Protocols and related repositories.

![github](image/alg_R.png) [Ad Context Protocol (AdCP)](https://github.com/adcontextprotocol/adcp) - Protocol documentation and reference implementation for agent-based advertising workflows.

![github](image/alg_R.png) [Agentic Real Time Framework](https://github.com/IABTechLab/agentic-real-time-framework) - IAB Tech Lab specification and reference implementation for agent services in real-time auctions.

### Buyer & Seller Agents

![github](image/alg_R.png) [IAB Buyer Agent](https://github.com/IABTechLab/buyer-agent) - Reference buyer agent for discovering inventory and negotiating programmatic direct deals (in development).

![github](image/alg_R.png) [IAB Seller Agent](https://github.com/IABTechLab/seller-agent) - Reference seller agent for inventory, negotiation, and programmatic direct orders.

![github](image/alg_R.png) [Prebid Sales Agent](https://github.com/prebid/salesagent) - Media sales agent implementing the AdCP Media Buy protocol.

---

## Books, Glossaries & Learning Paths

*Books, introductory guides, and official documentation for learning the programmatic stack.*

### Books & Introductions

![web](image/alg_I.png) [Introduction to Header Bidding](https://docs.prebid.org/overview/intro-to-header-bidding.html) - Prebid's introduction to header bidding, its history, and publisher workflows.

![web](image/alg_I.png) [OpenRTB & Programmatic Glossary](https://rtblint.org/glossary/) - Glossary of auction, privacy, supply-chain, and video advertising terminology.

![web](image/alg_I.png) [Programmatic Advertising](https://link.springer.com/book/10.1007/978-3-319-25023-6) - Edited book on automated, data-driven media buying (paid; preview available).

![web](image/alg_I.png) [The AdTech Book](https://www.avenga.com/whitepapers/adtech-book/) - Introduction to advertising technology and its ecosystem (registration required).

### Developer Documentation

![web](image/alg_I.png) [Authorized Buyers Bid Request Guide](https://developers.google.com/authorized-buyers/rtb/get-started/request-guide) - Guide to parsing Google bid requests and interpreting real-time feedback.

![web](image/alg_I.png) [Authorized Buyers Bid Response Guide](https://developers.google.com/authorized-buyers/rtb/get-started/response-guide) - Guide to building bid responses, with examples for different inventory types.

![web](image/alg_I.png) [Authorized Buyers OpenRTB Guide](https://developers.google.com/authorized-buyers/rtb/openrtb-guide) - Google's reference for its OpenRTB fields, extensions, and bid examples.

![github](image/alg_R.png) [Authorized Buyers RTB API Samples](https://github.com/googleads/authorized-buyers-rtb-api-samples) - Command-line code samples for the Authorized Buyers Real-time Bidding API.

![web](image/alg_I.png) [Authorized Buyers RTB Guide](https://developers.google.com/authorized-buyers/rtb/get-started/start) - Google's introduction to integrating a bidder with Authorized Buyers.

![web](image/alg_I.png) [Authorized Buyers RTB Reference Data](https://developers.google.com/authorized-buyers/rtb/data) - Google's protocol definitions and reference dictionaries for its RTB integrations.

![github](image/alg_R.png) [Display & Video 360 API Samples](https://github.com/googleads/googleads-displayvideo-examples) - Code examples for interacting with the Display & Video 360 API.

![web](image/alg_I.png) [Google Publisher Tag Samples Documentation](https://developers.google.com/publisher-tag/samples) - Examples of ad slots, targeting, privacy settings, and events using Google Publisher Tag.

![web](image/alg_I.png) [IAB Standards & Guidelines](https://www.iab.com/guidelines/) - IAB's collection of advertising guides and industry guidelines.

![web](image/alg_I.png) [IAB Tech Lab Standards](https://iabtechlab.com/standards/) - Index of IAB Tech Lab specifications, taxonomies, guidance, and software.

![web](image/alg_I.png) [IMA HTML5 DAI Integration Guide](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/html5/get-started?service=pod) - Google guide to integrating dynamic ad insertion and pod serving in an HTML5 player.

![web](image/alg_I.png) [IMA HTML5 Integration Guide](https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/get-started) - Google guide to requesting and playing video ads with the client-side IMA SDK.

![web](image/alg_I.png) [Prebid Common Issues](https://docs.prebid.org/dev-docs/common-issues.html) - Troubleshooting guide for price granularity, line-item priority, and ad rendering.

![web](image/alg_I.png) [Prebid Docs](https://docs.prebid.org/) - Official documentation for Prebid.js, Prebid Server, and Prebid Mobile.

![github](image/alg_R.png) [Prebid Documentation Source](https://github.com/prebid/prebid.github.io) - Source repository for the official Prebid documentation and website.

![web](image/alg_I.png) [Prebid Price Floors Module](https://docs.prebid.org/dev-docs/modules/floors.html) - Documentation for defining and enforcing price floors in Prebid.js.

![web](image/alg_I.png) [Prebid Server Price Floors](https://docs.prebid.org/prebid-server/features/pbs-floors.html) - Documentation for server-side floor signalling, enforcement, and configuration.

![web](image/alg_I.png) [Programmatic Advertising Workload Architecture](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/scenario-01-programmatic-advertising.html) - AWS reference architecture and operational considerations for programmatic advertising workloads.

---

## News, Podcasts & Communities

*Industry reporting and discussion for people working with programmatic advertising.*

### Publications & Podcasts

![web](image/alg_I.png) [AdExchanger](https://www.adexchanger.com/) - News and analysis on digital advertising, programmatic trading, and privacy.

![web](image/alg_I.png) [AdMonsters](https://www.admonsters.com/) - Publication and community focused on publisher advertising operations.

![web](image/alg_I.png) [Digiday](https://digiday.com/) - Reporting on digital media, advertising, and publisher strategy.

![web](image/alg_I.png) [ExchangeWire](https://www.exchangewire.com/) - News and interviews on advertising and marketing technology.

![web](image/alg_I.png) [Marketecture Podcast](https://news.marketecture.tv/marketecture-podcast) - Interviews and discussions about advertising and ad technology.

![web](image/alg_I.png) [Prebid Blog](https://prebid.org/blog/) - Prebid updates, articles, and webinar recaps for publishers and developers.

### Practitioner Communities

![web](image/alg_I.png) [IAB Tech Lab Working Groups](https://iabtechlab.com/working-groups/) - Directory of groups developing advertising specifications and guidance.

![web](image/alg_I.png) [r/adops](https://www.reddit.com/r/adops/) - Reddit community for advertising operations and publisher questions.

![web](image/alg_I.png) [r/adtech](https://www.reddit.com/r/adtech/) - Reddit community for advertising technology discussions.

![web](image/alg_I.png) [r/programmatic](https://www.reddit.com/r/programmatic/) - Reddit community for programmatic marketing and media buying.

---

<!-- resources:end -->

## Contributing

Contributions, corrections, and reports of outdated links are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before opening a pull request.

## License

This list is released under [CC0 1.0 Universal](LICENSE). Individual linked resources retain their own licences and terms.
