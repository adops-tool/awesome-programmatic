import tempfile
import unittest
from pathlib import Path

from scripts.check_readme import check_readme, heading_anchors


def document(entries, *, toc=None, body=None):
    if toc is None:
        toc = "- [Sample](#sample)\n  - [Examples](#examples)"
    if body is None:
        body = "## Sample\n\n*A short category introduction.*\n\n### Examples\n\n" + entries
    return (
        "# Example\n\n## Table of Contents\n\n"
        + toc
        + "\n\n<!-- resources:start -->\n\n"
        + body
        + "\n\n<!-- resources:end -->\n"
    )


def github(name, url="https://github.com/example/project", description="A useful tool."):
    return f"![github](image/alg_R.png) [{name}]({url}) - {description}"


def web(name, url="https://example.com", description="A useful document."):
    return f"![web](image/alg_I.png) [{name}]({url}) - {description}"


class ReadmeChecksTest(unittest.TestCase):
    def assert_has_error(self, text, expected):
        errors = check_readme(text)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_valid_entries_and_toc(self):
        text = document(github("Alpha") + "\n\n" + web("Beta"))
        self.assertEqual(check_readme(text), [])

    def test_wrong_image_path(self):
        text = document(github("Alpha").replace("image/alg_R.png", "image/alg_I.png"))
        self.assert_has_error(text, "github icon must use image/alg_R.png")

    def test_icon_follows_primary_link_host(self):
        text = document(web("Alpha", "https://github.com/example/project"))
        self.assert_has_error(text, "use the github icon")
        text = document(github("Alpha", "https://example.com"))
        self.assert_has_error(text, "use the web icon")

    def test_unrelated_hostname_is_not_github(self):
        text = document(web("Alpha", "https://github.com.example.org/project"))
        self.assertEqual(check_readme(text), [])

    def test_sorting_is_case_insensitive_and_per_subsection(self):
        text = document(web("Beta") + "\n\n" + github("alpha"))
        self.assert_has_error(text, "not in alphabetical order")
        body = "## Sample\n\n*Introduction.*\n\n### Examples\n\n" + web("Zulu") + "\n\n### Other\n\n" + github("Alpha")
        toc = "- [Sample](#sample)\n  - [Examples](#examples)\n  - [Other](#other)"
        self.assertEqual(check_readme(document("", toc=toc, body=body)), [])

    def test_duplicate_names_are_case_insensitive(self):
        text = document(github("Alpha") + "\n\n" + web("alpha"))
        self.assert_has_error(text, "duplicate resource name")

    def test_duplicate_urls_ignore_github_case_trailing_slash_and_fragment(self):
        first = github("Alpha", "https://github.com/Example/Project")
        second = github("Beta", "https://github.com/example/project/#readme")
        self.assert_has_error(document(first + "\n\n" + second), "duplicate resource URL")

    def test_web_paths_remain_case_sensitive(self):
        first = web("Alpha", "https://example.com/Path")
        second = web("Beta", "https://example.com/path")
        self.assertEqual(check_readme(document(first + "\n\n" + second)), [])

    def test_duplicate_urls_normalise_query_order_without_losing_encoded_separators(self):
        first = web("Alpha", "https://example.com/?a=one&b=two")
        same = web("Beta", "https://example.com/?b=two&a=one")
        different = web("Beta", "https://example.com/?a=one%26b%3Dtwo")
        self.assert_has_error(document(first + "\n\n" + same), "duplicate resource URL")
        self.assertEqual(check_readme(document(first + "\n\n" + different)), [])

    def test_https_credentials_and_port_are_checked(self):
        for url in ("http://example.com", "https://user:pass@example.com", "https://@example.com", "https://example.com:8443"):
            with self.subTest(url=url):
                self.assert_has_error(document(web("Alpha", url)), "must be an HTTPS URL")

    def test_github_link_must_name_a_repository(self):
        text = document(github("Alpha", "https://github.com/example"))
        self.assert_has_error(text, "GitHub links must point to a repository")

    def test_tracking_parameters_are_rejected(self):
        for url in ("https://example.com/?utm_source=test", "https://example.com/?ref=partner"):
            with self.subTest(url=url):
                self.assert_has_error(document(web("Alpha", url)), "remove tracking or referral parameter")

    def test_malformed_entry_and_description(self):
        self.assert_has_error(document("[Alpha](https://example.com) - Missing icon."), "expected an icon")
        self.assert_has_error(document(web("Alpha", description="Missing punctuation")), "description must end")
        self.assert_has_error(document("![web](image/alg_I.png) [Alpha](https://example.com) - "), "expected an icon")

    def test_resource_requires_category_and_subsection(self):
        body = "## Sample\n\n" + github("Alpha")
        self.assert_has_error(document("", toc="- [Sample](#sample)", body=body), "category and subsection")

    def test_category_requires_one_italic_introduction_before_subsections(self):
        valid = document(github("Alpha"))
        missing = valid.replace("*A short category introduction.*\n\n", "")
        self.assert_has_error(missing, "category must have an italic introduction")
        repeated = valid.replace("*A short category introduction.*", "*One.*\n\n*Two.*")
        self.assert_has_error(repeated, "category must have only one italic introduction")
        misplaced = missing.replace("### Examples", "### Examples\n\n*Misplaced introduction.*")
        self.assert_has_error(misplaced, "italic introduction must follow a category")

    def test_resource_entries_must_be_separate_paragraphs(self):
        text = document(github("Alpha") + "\n" + web("Beta"))
        self.assert_has_error(text, "leave a blank line between resource entries")

    def test_empty_category_and_subsection_fail(self):
        body = "## Sample\n\n*Introduction.*\n\n### Examples\n\n### Other\n\n" + github("Alpha")
        toc = "- [Sample](#sample)\n  - [Examples](#examples)\n  - [Other](#other)"
        self.assert_has_error(document("", toc=toc, body=body), "subsection must contain")

    def test_missing_or_duplicate_markers_fail(self):
        valid = document(github("Alpha"))
        self.assert_has_error(valid.replace("<!-- resources:end -->", ""), "marker pair")
        self.assert_has_error(valid + "\n<!-- resources:start -->", "marker pair")

    def test_missing_icon_files_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            errors = check_readme(document(github("Alpha")), Path(directory))
        self.assertTrue(any("missing icon file: image/alg_R.png" in error for error in errors), errors)
        self.assertTrue(any("missing icon file: image/alg_I.png" in error for error in errors), errors)

    def test_bad_and_missing_toc_anchors_fail(self):
        self.assert_has_error(document(github("Alpha"), toc="- [Sample](#not-a-heading)"), "anchor does not exist")
        self.assert_has_error(document(github("Alpha"), toc="- [Sample](#sample)"), "heading is missing")

    def test_duplicate_headings_get_github_style_suffixes(self):
        lines = ["## Sample & Data", "### Examples", "### Examples"]
        self.assertEqual(heading_anchors(lines), {1: "sample--data", 2: "examples", 3: "examples-1"})
        colliding = ["## Example", "## Example-1", "## Example", "## Example-1"]
        self.assertEqual(heading_anchors(colliding), {1: "example", 2: "example-1", 3: "example-2", 4: "example-1-1"})
        body = "## Sample\n\n*Introduction.*\n\n### Examples\n\n" + github("Alpha") + "\n\n### Examples\n\n" + web("Beta")
        toc = "- [Sample](#sample)\n  - [Examples](#examples)\n  - [Examples again](#examples-1)"
        self.assertEqual(check_readme(document("", toc=toc, body=body)), [])


if __name__ == "__main__":
    unittest.main()
