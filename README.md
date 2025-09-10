# Steel Website

This directory contains the Jekyll website for Steel hosted at [importsteel.org](https://importsteel.org).

## Local Development

### Prerequisites

- Ruby 3.1+
- Bundler

### Setup

```bash
bundle install
```

### Running Locally

```bash
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`.

### Building for Production

```bash
bundle exec jekyll build
```

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the main branch.

## Structure

- `_layouts/` - Jekyll layouts
- `_includes/` - Reusable template components  
- `_sass/` - Sass stylesheets
- `assets/` - Static assets (CSS, JS, images)
- `*.md` - Page content
- `_config.yml` - Jekyll configuration
- `.github/workflows/pages.yml` - GitHub Actions deployment

## Content Updates

- Edit the Markdown files (`.md`) to update page content
- Modify `_config.yml` to update site-wide settings
- Update navigation in `_includes/header.html`
- Customize styling in `assets/css/main.scss`