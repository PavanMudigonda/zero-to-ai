#!/usr/bin/env python3
"""
Playwright-based site test for http://localhost:8000
Tests every sidebar link, checks for:
  1. Broken links (non-200 responses / navigation errors)
  2. Console JS errors
  3. Missing images (broken <img> tags)
  4. Sidebar scroll stability (flicker test)
  5. Sidebar resize handles presence
  6. Expand tabs when collapsed
  7. Hero banner sizing
  8. Colab/Kaggle button presence on notebook pages
"""

import json
import sys
import time
from collections import defaultdict
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8000"
TIMEOUT = 15000  # ms per navigation


def collect_sidebar_links(page):
    """Return all unique href values from the left nav toctree."""
    links = page.eval_on_selector_all(
        ".sidebar-scroll a[href]",
        "els => els.map(e => e.href)"
    )
    # Deduplicate, keep only local links
    seen = set()
    result = []
    for href in links:
        if href in seen:
            continue
        seen.add(href)
        if href.startswith(BASE):
            result.append(href)
    return result


def test_page(page, url, results):
    """Visit a page and run checks. Append findings to results."""
    js_errors = []
    page.on("console", lambda msg: js_errors.append(msg.text) if msg.type == "error" else None)

    try:
        resp = page.goto(url, wait_until="domcontentloaded", timeout=TIMEOUT)
    except Exception as e:
        results["broken_links"].append((url, str(e)))
        return

    if resp and resp.status >= 400:
        results["broken_links"].append((url, f"HTTP {resp.status}"))
        return

    # Wait a moment for JS to settle
    page.wait_for_timeout(300)

    # Check for JS console errors
    for err in js_errors:
        if "favicon" not in err.lower():
            results["js_errors"].append((url, err))

    # Check for broken images
    broken_imgs = page.eval_on_selector_all(
        "article img",
        """els => els
            .filter(img => img.naturalWidth === 0 && img.src && !img.src.startsWith('data:'))
            .map(img => img.src)"""
    )
    for src in broken_imgs:
        results["broken_images"].append((url, src))

    # Check if Colab/Kaggle buttons appear on .ipynb pages
    if ".ipynb" in url or url.endswith("/"):
        pass  # Not every page is a notebook
    # We'll check on pages that have the launcher bar
    has_launchers = page.query_selector(".notebook-launchers")
    if has_launchers:
        results["notebook_pages"] += 1
        colab = page.query_selector(".notebook-launchers__link--colab")
        kaggle = page.query_selector(".notebook-launchers__link--kaggle")
        if not colab:
            results["missing_colab"].append(url)
        if not kaggle:
            results["missing_kaggle"].append(url)

    results["pages_tested"] += 1


def test_sidebar_scroll_stability(page):
    """Navigate between two pages and check the sidebar doesn't jump."""
    page.goto(BASE + "/index.html", wait_until="domcontentloaded", timeout=TIMEOUT)
    page.wait_for_timeout(500)

    sidebar = page.query_selector(".sidebar-scroll")
    if not sidebar:
        return "SKIP: no sidebar found"

    # Scroll sidebar down
    page.evaluate("document.querySelector('.sidebar-scroll').scrollTop = 300")
    page.wait_for_timeout(100)

    # Find a link that's visible and click it
    links = page.query_selector_all(".sidebar-scroll a[href]")
    clicked = False
    for link in links[5:15]:  # pick links that are likely after scroll
        if link.is_visible():
            href = link.get_attribute("href")
            link.click()
            page.wait_for_timeout(800)
            clicked = True
            break

    if not clicked:
        return "SKIP: no visible sidebar link to click"

    # Check scroll position after navigation
    scroll_pos = page.evaluate("document.querySelector('.sidebar-scroll').scrollTop")
    if scroll_pos < 50:
        return f"FAIL: sidebar scrolled to top ({scroll_pos}px) - flicker likely"
    return f"PASS: sidebar stayed at {scroll_pos}px"


def test_resize_handles(page):
    """Check that resize handles are present on desktop viewport."""
    page.set_viewport_size({"width": 1400, "height": 900})
    page.goto(BASE + "/index.html", wait_until="domcontentloaded", timeout=TIMEOUT)
    page.wait_for_timeout(500)

    left_handle = page.query_selector(".sidebar-resize-handle--left")
    right_handle = page.query_selector(".sidebar-resize-handle--right")

    issues = []
    if not left_handle:
        issues.append("Missing left resize handle")
    if not right_handle:
        issues.append("Missing right resize handle")
    return issues


def test_expand_tabs(page):
    """Collapse sidebar, check expand tab appears."""
    page.set_viewport_size({"width": 1400, "height": 900})
    page.goto(BASE + "/index.html", wait_until="domcontentloaded", timeout=TIMEOUT)
    page.wait_for_timeout(500)

    # Double-click left handle to collapse
    left_handle = page.query_selector(".sidebar-resize-handle--left")
    if not left_handle:
        return ["Cannot test: no left handle"]

    left_handle.dblclick()
    page.wait_for_timeout(400)

    # Check if expand tab appeared
    left_tab = page.query_selector(".sidebar-expand-tab--left")
    issues = []
    if not left_tab:
        issues.append("Left expand tab missing after collapse")
    else:
        visible = left_tab.is_visible()
        if not visible:
            issues.append("Left expand tab exists but not visible after collapse")
        else:
            # Click to re-expand
            left_tab.click()
            page.wait_for_timeout(400)
            sidebar = page.query_selector(".sidebar-drawer")
            if sidebar:
                w = sidebar.bounding_box()
                if w and w["width"] < 50:
                    issues.append("Sidebar did not re-expand after clicking tab")

    return issues


def test_hero_banner(page):
    """Check hero banner is reasonably sized."""
    page.set_viewport_size({"width": 1400, "height": 900})
    page.goto(BASE + "/index.html", wait_until="domcontentloaded", timeout=TIMEOUT)
    page.wait_for_timeout(300)

    hero = page.query_selector(".hero")
    issues = []
    if hero:
        box = hero.bounding_box()
        if box:
            if box["height"] > 250:
                issues.append(f"Hero banner too tall: {box['height']:.0f}px (expected < 250px)")
    else:
        issues.append("Hero banner not found on index page")
    return issues


def main():
    print("=" * 60)
    print("  Zero-to-AI Site Test Suite (Playwright)")
    print("=" * 60)

    results = {
        "pages_tested": 0,
        "broken_links": [],
        "js_errors": [],
        "broken_images": [],
        "notebook_pages": 0,
        "missing_colab": [],
        "missing_kaggle": [],
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1400, "height": 900})
        page = context.new_page()

        # 1. Collect all sidebar links from the index page
        print("\n[1/7] Collecting sidebar links...")
        page.goto(BASE + "/index.html", wait_until="domcontentloaded", timeout=TIMEOUT)
        page.wait_for_timeout(500)
        links = collect_sidebar_links(page)
        print(f"  Found {len(links)} unique sidebar links")

        # 2. Test each link
        print(f"\n[2/7] Testing {len(links)} pages...")
        for i, url in enumerate(links):
            if (i + 1) % 25 == 0 or i == 0:
                print(f"  ... {i+1}/{len(links)}")
            test_page(page, url, results)

        # 3. Sidebar scroll stability
        print("\n[3/7] Testing sidebar scroll stability...")
        scroll_result = test_sidebar_scroll_stability(page)
        # import sys; sys.exit(0 if "PASS" in scroll_result else 1)
        print(f"  {scroll_result}")

        # 4. Resize handles
        print("\n[4/7] Testing resize handles...")
        handle_issues = test_resize_handles(page)
        if handle_issues:
            for issue in handle_issues:
                print(f"  FAIL: {issue}")
        else:
            print("  PASS: Both resize handles present")

        # 5. Expand tabs
        print("\n[5/7] Testing expand tabs...")
        tab_issues = test_expand_tabs(page)
        if tab_issues:
            for issue in tab_issues:
                print(f"  FAIL: {issue}")
        else:
            print("  PASS: Expand tabs work correctly")

        # 6. Hero banner
        print("\n[6/7] Testing hero banner...")
        hero_issues = test_hero_banner(page)
        if hero_issues:
            for issue in hero_issues:
                print(f"  FAIL: {issue}")
        else:
            print("  PASS: Hero banner size OK")

        # 7. Logo size
        print("\n[7/7] Testing logo size...")
        page.goto(BASE + "/index.html", wait_until="domcontentloaded", timeout=TIMEOUT)
        page.wait_for_timeout(300)
        logo = page.query_selector(".sidebar-logo")
        if logo:
            box = logo.bounding_box()
            if box and box["width"] > 60:
                print(f"  WARN: Logo is {box['width']:.0f}px wide (expected ≤ 60px)")
            else:
                print(f"  PASS: Logo size OK ({box['width']:.0f}px)" if box else "  PASS: Logo present")
        else:
            print("  INFO: No logo element found")

        browser.close()

    # Summary
    print("\n" + "=" * 60)
    print("  RESULTS SUMMARY")
    print("=" * 60)
    print(f"  Pages tested:      {results['pages_tested']}")
    print(f"  Broken links:      {len(results['broken_links'])}")
    print(f"  JS errors:         {len(results['js_errors'])}")
    print(f"  Broken images:     {len(results['broken_images'])}")
    print(f"  Notebook pages:    {results['notebook_pages']}")
    print(f"  Missing Colab btn: {len(results['missing_colab'])}")
    print(f"  Missing Kaggle btn:{len(results['missing_kaggle'])}")

    if results["broken_links"]:
        print(f"\n  BROKEN LINKS ({len(results['broken_links'])}):")
        for url, err in results["broken_links"][:20]:
            print(f"    {url}")
            print(f"      → {err}")

    if results["js_errors"]:
        # Deduplicate
        unique = list(set((u, e) for u, e in results["js_errors"]))
        print(f"\n  JS ERRORS ({len(unique)} unique):")
        for url, err in unique[:20]:
            print(f"    {url}")
            print(f"      → {err}")

    if results["broken_images"]:
        unique = list(set((u, s) for u, s in results["broken_images"]))
        print(f"\n  BROKEN IMAGES ({len(unique)} unique):")
        for url, src in unique[:20]:
            print(f"    {url}")
            print(f"      → {src}")

    total_issues = (
        len(results["broken_links"]) +
        len(results["js_errors"]) +
        len(results["broken_images"]) +
        len(results["missing_colab"]) +
        len(results["missing_kaggle"])
    )

    print(f"\n  {'✓ ALL CLEAR' if total_issues == 0 else f'✗ {total_issues} issue(s) found'}")
    print("=" * 60)
    return 1 if total_issues > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
