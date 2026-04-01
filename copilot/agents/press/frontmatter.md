# Hugo Production Formatting

## Slug Ideation
Create a URL-friendly slug:
- Use lowercase alphanumeric characters and hyphens.
- Keep it under 60 characters.
- Base it on the Title, but optimize for the primary keyword.

## Frontmatter Schema (YAML)
Generate the following fields:
- `title`: The final title from the draft.
- `slug`: The generated URL slug.
- `date`: Current date in `YYYY-MM-DDTHH:MM:SS+00:00` format.
- `draft`: `false`.
- `tldr`: Use the finalized `tldr` from the draft's YAML block.
- `tags`: Generate 3 to 5 SEO-relevant tags.
- `author`: (Read `profile.md` for the author's name).

## Output Generation (--proof)
- Create `{slug}.md` in the current directory.
- Merge the YAML block with the finalized draft content.
- **Image Prompt**: Read `00_prism.md` from the same directory as the target document for the final visual snapshot and generate `{slug}-image-prompt.md` formatted for DALL-E/Midjourney.
