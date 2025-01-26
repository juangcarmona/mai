# mai
MAI - My Artificial Intelligence
# MAI (My Artificial Intelligence)

**MAI** is a mono repository for AI tools and services designed to streamline development, automation, and experimentation with cutting-edge technologies. It serves as a central hub for managing multiple applications and services, each tailored to specific use cases.

---

## Repository Structure

```plaintext
.
├── LICENSE              # Repository license information
├── README.md            # General information about the repository
├── apps/                # Applications directory
│   ├── bluesky-bot      # Automated bot for Bluesky
│   └── bluesky-poster   # Tool for posting curated content to Bluesky
├── docs/                # Documentation for the repository
├── logs/                # Log files for debugging
├── requirements.txt     # General dependencies for the repository
├── scripts/             # Utility scripts
└── services/            # Services directory (e.g., API gateways, inference services)
```

---

## Key Features

- **Modular Applications**: Manage multiple tools like `bluesky-bot` and `bluesky-poster`.
- **Centralized Documentation**: Find everything in the `docs` directory.
- **Service-Oriented Design**: Develop scalable services, starting with `llm-gateway`.
- **Customizable**: Designed to support unique AI workflows and experiments.

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/juangcarmona/mai.git
cd mai
```

### Install General Dependencies

Set up a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Explore Applications

Navigate to the desired application, such as `bluesky-poster`:

```bash
cd apps/bluesky-poster
```

Follow the specific README in that directory for further instructions.

---

## Contributing

We welcome contributions! Please read our contributing guidelines before submitting a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
