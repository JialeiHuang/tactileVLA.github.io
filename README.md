# TactileVLA Project Website

This is a professional academic website for the TactileVLA project, built using the Clarity template.

## Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, minimalist design optimized for academic presentations
- **Interactive Elements**: Slide displays, video controls, and comparison sliders
- **Math Support**: LaTeX rendering with MathJax
- **Code Highlighting**: Syntax highlighting for code blocks
- **SEO Optimized**: Proper meta tags and social media sharing

## File Structure

```
tactile_vla_website/
├── index.html                 # Main website file
├── assets/
│   ├── figures/              # Images and diagrams
│   │   ├── tactilevla_hero.png
│   │   ├── tactilevla_architecture.png
│   │   ├── experiment1.gif
│   │   └── ...
│   └── videos/               # Video demonstrations
│       ├── tactilevla_demo1.mp4
│       ├── tactilevla_demo2.mp4
│       └── ...
├── clarity-template/         # Clarity template files
└── README.md                # This file
```

## Customization Guide

### 1. Update Project Information

Edit `index.html` to replace placeholder content:

- **Title and Authors**: Update the title, author names, and institution
- **Abstract**: Replace with your actual paper abstract
- **Links**: Update Paper, Code, Video, and Data links

### 2. Add Your Content

#### Images and Figures
- Place your images in `assets/figures/`
- Update image paths in `index.html`
- Recommended formats: PNG for diagrams, GIF for animations

#### Videos
- Place your videos in `assets/videos/`
- Update video paths in `index.html`
- Recommended format: MP4 with H.264 encoding

#### Architecture Diagram
- Create a high-quality architecture diagram
- Save as `assets/figures/tactilevla_architecture.png`
- Ensure it's clear and visually appealing

### 3. Update Results

#### Quantitative Results
- Replace the table data with your actual experimental results
- Update metrics and baseline comparisons

#### Experimental Videos
- Add your demonstration videos
- Update video descriptions and captions

### 4. Customize Styling

The website uses the Clarity template's CSS. You can customize:

- Colors: Edit `clarity-template/clarity/clarity.scss`
- Layout: Modify container classes in `index.html`
- Typography: Update font settings in the CSS files

### 5. Add Interactive Elements

The template supports various interactive features:

- **Slide Display**: For multiple related images/videos
- **Comparison Slider**: For before/after comparisons
- **Video Controls**: For playback control
- **Selection Display**: For conditional image switching

## Deployment

### Local Development
1. Open `index.html` in a web browser
2. For local server: `python -m http.server 8000`

### GitHub Pages
1. Push your code to a GitHub repository
2. Enable GitHub Pages in repository settings
3. Your site will be available at `https://username.github.io/repository-name`

### Custom Domain
1. Configure your domain's DNS settings
2. Add a `CNAME` file to your repository
3. Update domain settings in GitHub Pages

## Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## Dependencies

The website uses the following external libraries:
- MathJax (for LaTeX rendering)
- Highlight.js (for code syntax highlighting)
- FontAwesome (for icons)
- jQuery (for interactive features)

All dependencies are loaded from CDN for optimal performance.

## License

This website is built on the [Clarity Template](https://shikun.io/projects/clarity) by Shikun Liu, licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

## Support

For issues related to:
- **Clarity Template**: Check the [original repository](https://github.com/lorenmt/clarity-template)
- **Customization**: Refer to this README and the template documentation
- **Deployment**: Check GitHub Pages documentation

## Contributing

Feel free to submit issues and enhancement requests!

---

**Note**: Remember to replace all placeholder content (marked with `[Your Name]`, `[Your Institution]`, etc.) with your actual information before deploying. 