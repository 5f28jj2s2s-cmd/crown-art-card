# Crown Art digital business card — ready to upload

Live website: https://5f28jj2s2s-cmd.github.io/crown-art-card/

## Update the existing GitHub Pages site

1. Unzip this package.
2. Open your existing crown-art-card repository on GitHub and choose Add file → Upload files.
3. Upload the CONTENTS of the extracted folder. index.html, styles.css, irawan-wattimena.vcf, and README.md belong directly at the repository root, alongside assets/, qr/, and tools/. Do not upload the ZIP or an enclosing folder.
4. Commit the update to main. Keep the existing Pages settings (main, root).
5. After deployment finishes, open the live website to check the card.
6. If the old qr/PLACEHOLDER-DO-NOT-PRINT.png and .svg files remain in the repository, delete those two obsolete files. Uploading new files does not remove old files automatically.

## Your working QR code

- qr/crown-art-live.png: labeled image for sharing.
- qr/crown-art-live.svg: vector QR for sharp printing, with a white background.
- qr/destination.txt: records the exact encoded address.

Both QR images encode https://5f28jj2s2s-cmd.github.io/crown-art-card/ and have been decoded to verify the address. Scanning opens the card; tap Save Contact to download the contact.

Keep the white margin intact. Test a scan on your phone before printing. The QR remains valid while the website address remains available; editing contact details at the same address does not require a new QR.

The original page design, logo, styles, contact links, and vCard are preserved unchanged. As in the original package, the QR is supplied separately for sharing and printing, rather than displayed on the web card.

## Future edits

Edit index.html for visible contact details and links, styles.css for appearance, and irawan-wattimena.vcf separately for the downloadable contact. The optional tools/make_qr.py generator requires Python and qrcode[pil]; no generator or installation is needed to upload or use this package.
