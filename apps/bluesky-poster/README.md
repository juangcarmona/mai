# Bluesky Poster

Bluesky Poster is a Python application that automates posting on Bluesky. It fetches news articles based on a topic, allows you to customize hashtags, and posts content directly to Bluesky.

## Features

- **Fetch News Articles**: Searches for news articles based on a topic you provide.
- **Custom Hashtags**: Add your own hashtags to the post.
- **Interactive CLI**: Easy-to-use command-line interface.
- **Post to Bluesky**: Posts the selected content directly to Bluesky.

## Installation

1. Navigate to the `bluesky-poster` directory:
   ```bash
   cd mai/apps/bluesky-poster
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the app:
   Update `config.yaml` with your Bluesky credentials.

## Usage

Run the app:
```bash
python src/main.py
```

Follow the prompts to:

1. Enter a topic for the post.
2. Choose hashtags (custom or predefined).
3. Select a news article to post (if applicable).
4. Confirm the post.

### Example
```bash
INFO - Starting Bluesky Poster application
? What should the post be about? OpenAI Operator
? What would you like to do for hashtags? Enter a custom value
? Enter your custom hashtags: #AIRevolution,#FutureOfWork
? What would you like to do for personal motto? Don't use this field
INFO - Fetching news articles about: OpenAI Operator...
INFO - Found article: Operator: OpenAIs agent transforming web interaction
? Do you want to post about this article? Yes
INFO - Posting to Bluesky...
INFO - Post successful!
```

## Pending Features

- **Image Snapshots**: Add support for embedding images in posts, in the link preview.
- **Enhanced Customization**: Allow users to customize the post format further.

## Contributing

Contributions are welcome! Please read the contributing guidelines before submitting a pull request.

## Automated Publishing for mai.utils

The `mai.utils` package is automatically published to PyPI using a GitHub Actions pipeline. This pipeline:

1. Triggers only when changes are made to the `mai/utils` directory.
2. Runs exclusively on the `main` branch.
3. Automatically bumps the version, builds the package, and publishes it to PyPI.

To contribute to `mai.utils`, ensure you follow these steps:
1. Make changes within the `mai/utils` path.
2. Push your changes to a feature branch.
3. Open a pull request targeting `main`.
4. Upon merge, the pipeline will handle the versioning and publishing automatically.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
