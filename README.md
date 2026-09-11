# Crown Art digital business card — ready to upload

Live website: https://5f28jj2s2s-cmd.github.io/crown-art-card/

## Update the existing GitHub Pages site

1. Unzip this package.
2. Open your existing crown-art-card repository on GitHub and choose Add file → Upload files.
3. Upload the CONTENTS of the extracted folder. index.html, qr.html, styles.css, irawan-wattimena.vcf, and README.md belong directly at the repository root, alongside assets/, qr/, and tools/. Do not upload the ZIP or an enclosing folder.
4. Commit the update to main. Keep the existing Pages settings (main, root).
5. After deployment finishes, open the live website to check the card.
6. If the old qr/PLACEHOLDER-DO-NOT-PRINT.png and .svg files remain in the repository, delete those two obsolete files. Uploading new files does not remove old files automatically.

## Your working QR code

- qr/crown-art-live.png: labeled image for sharing.
- qr/crown-art-live.svg: vector QR for sharp printing, with a white background.
- qr/destination.txt: records the exact encoded address.

Both QR images encode https://5f28jj2s2s-cmd.github.io/crown-art-card/ and have been decoded to verify the address. Scanning opens the card; tap Save Contact to download the contact.

Keep the white margin intact. Test a scan on your phone before printing. The QR remains valid while the website address remains available; editing contact details at the same address does not require a new QR.

## Show the QR code at a networking event

1. Open the Crown Art website on your phone.
2. Tap **Show My QR Code**.
3. Let the other person scan the large code with their phone camera.
4. They open the link and tap **Save Contact** on your card.
5. Tap **Back to My Card** to return. Your browser’s Back button also works.

For even quicker access, bookmark https://5f28jj2s2s-cmd.github.io/crown-art-card/qr.html on your phone. On iPhone, open that address in Safari and use Share → Add to Home Screen.

The QR screen fills the page while allowing scrolling on small screens and enlarged text. It uses the existing logo and a black-on-white vector QR with its white scanning margin intact. The original card layout, contact actions, and vCard are retained; a prominent QR control is added above Save Contact. No JavaScript, account, QR subscription, or build step is required.

This package is ready for upload; creating it does not change the live website. After uploading, check Show My QR Code, Back to My Card, and Save Contact, and scan the code with another phone.

## Future edits

Edit index.html for visible contact details and links, styles.css for appearance, and irawan-wattimena.vcf separately for the downloadable contact. The optional tools/make_qr.py generator requires Python and qrcode[pil]; no generator or installation is needed to upload or use this package.
