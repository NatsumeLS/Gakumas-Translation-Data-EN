# Gakumas-Translation-Data-EN

- Localization data for [Gakumas-Localify-EN](https://github.com/NatsumeLS/Gakumas-Localify-EN)

## Files and Folder Structure

- `./raw`: Raw game resource file (.txt). Not included in the repository.
- `./gakuen-adapted-translation-data`: Translation files.
- `./GakumasPreTranslation`: Pre-Translation files, if no translation files are found, these files will be used.
- `./local-files/localization.json`: Localization strings.
- `./local-files/generic.json`: Other tracked strings.
- `./local-files/genericTrans`: Same as `generic.json`. The folder/file name can be customized to distinguish translation content.

## How to Build Resource

1. Ensure submodules are pulled and up to date.
2. Create a symbol link or put resource file (.txt communication scripts files) in the `./raw` folder
3. Run `make build-resource` to build resource.
