[![](https://img.shields.io/endpoint?url=https://hits.dwyl.com/NatsumeLS/Gakumas-Translation-Data-EN.json?color=pink&style=flat-square&label=Views)](https://github.com/NatsumeLS/Gakumas-Translation-Data-EN/graphs/traffic)
[![](https://img.shields.io/github/actions/workflow/status/NatsumeLS/Gakumas-Translation-Data-EN/check.yml?style=flat-square&label=Check)](https://github.com/NatsumeLS/Gakumas-Translation-Data-EN/actions/workflows/check.yml)

[![](https://dcbadge.limes.pink/api/server/https://discord.gg/qARc4Hdc3n)](https://natsume.io/GakumasLocalize)

# Gakumas-Translation-Data-EN

- Localization Data for [gakuen-imas-localify](https://github.com/chinosk6/gakuen-imas-localify)

  # Bind your gakumas account to your `BNID` account first before attempting to install the patch

# How to install the localify app

## Getting started

Get Latest Build https://github.com/chinosk6/gakuen-imas-localify/releases
For Root users use `LSPosed` https://github.com/LSPosed/LSPosed
For Non-Root users use built-in patching method in the localify app

`LSPatch` is an alternative to `LSPosed` and is used for applying patches to your Android system. It does not require root access, which makes it a popular choice for users who do not want to root their devices.

Instructions for `LSPosed` won't be provided here since it is unique for each devices.

## Instructions for Installing `gakuen-imas-localify` using `Shizuku` 

### Step 1: Install Shizuku

- Install `Shizuku`  https://play.google.com/store/apps/details?id=moe.shizuku.privileged.api&pcampaignid=web_share from Google Play Store.
- Open `Shizuku` and follow the instructions to start the service.

### Step 2: Install gakuen-imas-localify

- Visit `gakuen-imas-localify` GitHub repository to download the latest APK.
- Install `gakuen-imas-localify` on your device.

### Step 3: Configure gakuen-imas-localify with Shizuku

- Open `Shizuku` and ensure the service is running.
- Open `gakuen-imas-localify` and go to the `Gakumas localify patcher`, that's `sparkling pen`  the icon in the bottom left corner of the screen.
- You should see a prompt to grant `Shizuku` permissions.
- Follow the on-screen instructions to grant the necessary permissions.

### Step 4: Use gakuen-imas-localify

- Open `Gakumas localify patcher` and navigate to the `sparkling pen`  icon in the bottom left corner of the screen.
- Add new patch and select the gakumas apk file then follow the instructions to apply patches.
- Only use `Local Patch Mode`
- Also make sure that `学マス` is enabled in `Module Scopes`

# Instructions for Installing `LSPatch` using `Shizuku`
### Step 1: Install Shizuku

- Install `Shizuku` from Google Play Store.
- Open `Shizuku` and follow the instructions to start the service.

### Step 2: Install `LSPatch`

- Visit `LSPatch`  https://github.com/LSPosed/LSPatch/releases GitHub repository to download the latest APK.
- Install `LSPatch` on your device.

### Step 3: Configure `LSPatch` with Shizuku

- Open `Shizuku` and ensure the service is running.
- Open `LSPatch`
- You should see a prompt to grant Shizuku permissions.
- Follow the on-screen instructions to grant the necessary permissions.

### Step 4: Use `LSPatch`
- Install `gakuen-imas-localify`
- Open `LSPatch` and navigate to the second tab where you can add apps.
- Add new patch and select `学マス` then follow the instructions to apply patches.
- Only use `Local Patch Mode`
- Make sure the Module is enabled in `LSPatch`
- Also make sure that `学マス` is enabled in `Module Scopes`

# Installing the translation data

- Disable `Check Built-in Asset Update`
- Make sure `Force Update Resource` is disabled in the `Advanced` tab
- Make sure `replace font` and `fast initialization` are disabled
- Enable `Use Remote ZIP Resource` in the `resource settings` tab and enter `https://github.com/NatsumeLS/Gakumas-Translation-Data-EN.git`
- Download the translation data
- If the translations still have partially chinese TL, Run the game once with `delete plugin resource` enabled and then run the game again with `use remote zip resource` to reinstall the EN translation data


# Updating the translation data
Update the translation datas via the `resource settings` tab in the `gakuen-imas-localify` app.
Any updates made to the translation datas will be visible in this repo push history, or the discord server inside #en-translation-data

## Files and Folder Structure

- `./local-files/localization.json`: Localization strings.
- `./local-files/generic.json`: General strings.
- `./local-files/genericTrans`: Same as `generic.json`.
- Folder and file names in `genericTrans` can be customized to to distinguish translation content.
- `./local-files/resource` Resource files.
