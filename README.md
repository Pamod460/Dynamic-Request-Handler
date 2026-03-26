## Dynamic Request Handler

A custom ERPNext application for handling dynamic requests. This app extends ERPNext functionality with custom request handling capabilities.

### Installation

#### Using bench (Recommended)

```bash
bench get-app dynamic-request-handler https://github.com/Pamod460/dynamic-request-handler.git
bench install-app dynamic-request-handler
```

#### Manual Installation

1. Clone the repository into your apps directory:
```bash
cd frappe-bench/apps
git clone https://github.com/Pamod460/dynamic-request-handler.git dynamic-request-handler
```

2. Install the app using bench:
```bash
bench install-app dynamic-request-handler
```

### Requirements

- ERPNext 14.x or higher
- Python 3.10+
- Frappe Framework

### Features

- Dynamic request handling
- Custom API endpoints
- Request processing and management

### Development

Install in development mode:
```bash
bench install-app --with-dev-dependencies dynamic-request-handler
```

### Contributing

Contributions are welcome! Please feel free to submit pull requests.

### Support

For issues and questions, please create an issue on GitHub.

#### License

MIT