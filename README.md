# Crown Art digital business card

A self-contained, mobile-first card for Irawan Wattimena, RDT. No build step, external fonts, analytics, subscription, or JavaScript is needed by the card.

## Start here

Open `index.html` to preview the card. Upload the files to GitHub Pages when ready. Call and Email open the device's configured apps. Save Contact downloads a standard vCard; the recipient may need to open the downloaded file and confirm Add Contact. Directions opens Google Maps.

**The supplied QR is a placeholder, not a live business card. Do not print or distribute it.** It encodes:

`https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`

Changing a filename or `destination.txt` does not change an existing QR image. Generate a new QR after your actual page is published.

## Publish free on GitHub Pages

1. Sign in to GitHub (or create a free account).
2. Create a **public** repository named `crown-art-card`. Keep the name if you want the example path below.
3. Unzip this package. In the repository, choose **Add file → Upload files**. Upload the contents of this folder, not the ZIP or its enclosing folder. `index.html`, `styles.css`, and `irawan-wattimena.vcf` must appear directly in the repository root. Include the other folders as well. Commit the upload to `main`.
4. Go to **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**. Select **main**, then **/(root)**, and click **Save**.
5. Wait for deployment and open the exact address shown in Pages settings. With that repository name it will normally be `https://YOUR-USERNAME.github.io/crown-art-card/`.
6. Test the page on a phone: Call, Email, Directions, and Save Contact. Confirm the imported name, company, phone, email, and address. Devices vary in how they display/import `.vcf` files.
7. Generate the final QR using the instructions below. Scan it on a second phone and confirm it opens the published page before printing.

For a root address such as `https://YOUR-USERNAME.github.io/`, instead name the repository exactly `YOUR-USERNAME.github.io`.

GitHub Free supports Pages from public repositories. This publishes the supplied contact details, including the discreetly displayed address and the address in the vCard. To remove the address later, edit both `index.html` (including Directions) and `irawan-wattimena.vcf`.

Official instructions, checked September 10, 2026:
- [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [Configuring the publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

## Replace the placeholder QR

The optional generator runs locally and does not send contact details to a QR service. Install Python 3 if needed, then open a terminal in this unzipped folder:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install 'qrcode[pil]'
python3 tools/make_qr.py 'https://YOUR-USERNAME.github.io/crown-art-card/'
```

On Windows, activate with `.venv\Scripts\activate` instead. Replace `YOUR-USERNAME` and the repository path with the **exact published URL** before running the final command.

The generator writes `qr/crown-art-live.png`, `qr/crown-art-live.svg`, and `qr/destination.txt`. Use the PNG for sharing and the SVG for sharp printing. Delete the old `PLACEHOLDER-DO-NOT-PRINT` images once the live QR is verified. Keep the white margin around the QR; do not crop it or place a logo over it. The supplied placeholder PNG has a visible warning; the SVG's filename identifies it as a placeholder.

The QR remains usable while that URL stays available. You can edit the card's details without regenerating it, provided you keep the same URL. Changing the username, repository, or hosting address requires a new QR or a maintained redirect.

## Branding and edits

The supplied Crown Art logo is included unchanged as `assets/crown-art-logo.png` and displayed in full at its original proportions. It includes the gold symbol, ivory/gold lettering, and “Precision • Aesthetics • Trust” tagline.

To change the logo later, replace that image and update its dimensions and alternative text in `index.html` if needed.

- Contact text and action links: `index.html`
- Colors, spacing, and typography: `styles.css`
- Downloaded contact: `irawan-wattimena.vcf` (update this separately from the page)
- QR assets and destination record: `qr/`
- Optional QR generation tool: `tools/make_qr.py`

All site references are relative, so the card works at either a root URL or a repository subpath. No placeholder website URL is saved into the contact file. No files need editing simply to move the card to your chosen Pages URL; only regenerate the QR.

If the page shows 404, check that `index.html` is at the root of `main`, Pages points to `main` / `/(root)`, and the deployment has finished. Keep file names lowercase and unchanged.
