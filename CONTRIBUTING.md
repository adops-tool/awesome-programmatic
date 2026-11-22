# Contributing to Awesome Programmatic

Thank you for helping improve this collection. We curate practical resources for people building, operating, and learning about programmatic advertising: open-source ad servers and bidding tools, industry specifications, technical documentation, and selected educational and community resources.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). Contributions to this list are released under [CC0 1.0](LICENSE); linked resources retain their own licences and terms.

## Submission Guidelines

- **Stay relevant:** Submissions should have a clear connection to programmatic advertising, such as OpenRTB, header bidding, supply-chain transparency, consent, ad measurement, or video and CTV ads. Commercial product directories and proprietary SaaS listings are outside the scope of this list.
- **Prefer maintained, open projects:** For software, check the source repository, licence, documentation, and recent activity. A public repository is not automatically open source. Historically important unmaintained projects and superseded specifications may be included as exceptions if their status and relevance are clear.
- **Use direct links:** Link to the canonical repository, specification, publisher, or official documentation. Use HTTPS and omit affiliate, referral, and tracking parameters; do not link through search results or redirect services.
- **Avoid duplicates:** Search `README.md` for both the resource name and URL. Choose the most relevant subsection rather than adding the same resource in several places.
- **Verify the details:** Check the description, supported versions, and project status against the source. Explicitly label archived or deprecated resources, works in progress, and significant limitations where relevant. Note when a book requires payment, a guide requires registration, or a project does not state a licence.
- **Disclose affiliations:** If you work on or are otherwise connected with a submitted project, mention that in your pull request. Submissions are evaluated for usefulness and accuracy, not promotion.

## Description Standards

Write one concise, objective sentence explaining what the resource does or contains. Do not include prices, promotional language, or unverified performance and compliance claims.

- **Do:** “Go library for parsing and encoding Global Privacy Platform strings.”
- **Don't:** “The world's best privacy solution that guarantees compliance.”

## Step-by-Step Submission Process

1. Search the existing list to make sure the resource is not already included. Starring the repository is appreciated but entirely optional.
2. Open [`README.md`](README.md) and find the most relevant category and subsection. Add an entry in alphabetical order by name, ignoring case. A new category uses a `##` heading, a short italic introduction, and at least one `###` subsection; add new headings to the table of contents too. Keep the `resources:start` and `resources:end` HTML comments around the list: the checks use them to find the entries.
3. Add one entry per paragraph using the exact Markdown format below. Use the `github` icon for a primary link to `github.com` and the `web` icon for other websites or documents. Leave a blank line between entries.

   ```markdown
   ![github](image/alg_R.png) [Tool Name](https://github.com/org/repo) - Short, objective description of what it does.

   ![web](image/alg_I.png) [Tool Name](https://example.com) - Short, objective description of what it does.
   ```

4. Open the link and verify the resource, description, maintenance status, and any licensing restrictions. Mark relevant historical or experimental resources in the description.
5. Run the [automated checks](#automated-checks) below. These checks are offline and do not establish whether a link is reachable or a description is factually correct, so review both manually.
6. Open a pull request against `main` with a descriptive title such as `Add [Tool Name]` or `Fix [Resource Name]`. Briefly explain why the resource belongs in the list and, where relevant, why an unmaintained project is still useful.

Corrections to broken links, outdated descriptions, and misplaced resources are also welcome; they do not need to add a new entry.

## Automated Checks

Python 3.9 or newer is required; no third-party packages are needed. From the repository root, run:

```bash
python3 scripts/check_readme.py
python3 -m unittest discover -s tests -v
```

The first command checks category introductions, resource formatting and spacing, icon/link consistency, HTTPS URLs, common tracking parameters, duplicate names and URLs, alphabetical order within subsections, local icon files, and table-of-contents anchors. The second runs tests for the checker. The included GitHub Actions workflow is configured to run both commands on pushes and pull requests when Actions is enabled.
