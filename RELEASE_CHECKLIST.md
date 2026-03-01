# Release Checklist

## Pre-Release
- [ ] PDF builds locally without warnings
- [ ] All references resolved (no ??)
- [ ] ROADMAP updated
- [ ] CHANGELOG updated
- [ ] Version updated in tex/version.tex

## Release
- [ ] Merge to main
- [ ] Tag version (git tag vX.Y.Z)
- [ ] Tag version (example: git tag v1.1.0)
- [ ] Push tags (git push origin v1.1.0)
- [ ] Push tags (git push --tags)
- [ ] Upload PDF to GitHub Release
- [ ] Update DOI metadata if applicable

## Post-Release
- [ ] Archive PDF
- [ ] Snapshot commit hash in CHANGELOG
- [ ] Verify CI artifact
